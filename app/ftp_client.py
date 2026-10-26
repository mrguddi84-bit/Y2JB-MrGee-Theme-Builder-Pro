"""FTP client for the user-started ftpsrv payload on port 2121."""
from contextlib import contextmanager
from ftplib import FTP, error_perm
from pathlib import Path
import ipaddress
import posixpath


class FTPError(RuntimeError):
    pass


class FTPClient:
    def __init__(self, host, port=2121, timeout=12):
        self.host = str(host).strip()
        self.port = int(port)
        self.timeout = timeout
        if not 1 <= self.port <= 65535:
            raise FTPError('Ungültiger FTP-Port')
        try:
            ipaddress.ip_address(self.host)
        except ValueError as exc:
            raise FTPError('Bitte eine gültige IP-Adresse eingeben') from exc

    @contextmanager
    def connect(self):
        ftp = FTP()
        try:
            ftp.connect(self.host, self.port, timeout=self.timeout)
            ftp.login()
            ftp.set_pasv(True)
            yield ftp
        except Exception as exc:
            raise FTPError(f'FTP {self.host}:{self.port}: {exc}') from exc
        finally:
            try:
                ftp.quit()
            except Exception:
                ftp.close()

    @staticmethod
    def clean_path(path):
        path = str(path or '/').strip()
        if not path.startswith('/') or '\\' in path or '\x00' in path:
            raise FTPError('Bitte einen absoluten FTP-Pfad mit / eingeben')
        clean = posixpath.normpath(path)
        if any(part == '..' for part in path.split('/')):
            raise FTPError('Pfadwechsel mit .. ist gesperrt')
        return clean

    @staticmethod
    def clean_name(name):
        if not name or name in ('.', '..') or '/' in name or '\\' in name or '\x00' in name:
            raise FTPError('Ungültiger Datei- oder Ordnername')
        return name

    @staticmethod
    def _sort(records):
        return sorted(records, key=lambda x: (not x['is_dir'], x['name'].lower()))

    def list(self, path):
        path = self.clean_path(path)
        with self.connect() as ftp:
            ftp.cwd(path)
            records = []
            try:
                for name, meta in ftp.mlsd():
                    name = posixpath.basename(name.rstrip('/'))
                    if name in ('.', '..', ''):
                        continue
                    records.append({'name': name, 'is_dir': meta.get('type', '').lower() in ('dir', 'cdir', 'pdir'),
                                    'size': int(meta['size']) if meta.get('size', '').isdigit() else None})
                return self._sort(records)
            except (error_perm, AttributeError, EOFError, OSError, ValueError):
                pass
            lines = []
            try:
                ftp.retrlines('LIST', lines.append)
                for line in lines:
                    fields = line.split(maxsplit=8)
                    if len(fields) < 9:
                        continue
                    name = fields[8]
                    if name in ('.', '..'):
                        continue
                    is_dir = fields[0].startswith('d')
                    size = int(fields[4]) if fields[4].isdigit() and not is_dir else None
                    records.append({'name': name, 'is_dir': is_dir, 'size': size})
                if records:
                    return self._sort(records)
            except (error_perm, EOFError, OSError):
                pass
            try:
                names = ftp.nlst()
            except (error_perm, EOFError, OSError) as exc:
                raise FTPError(f'FTP-Verzeichnis kann nicht aufgelistet werden: {exc}') from exc
            for item in names:
                name = posixpath.basename(item.rstrip('/'))
                if name in ('.', '..', ''):
                    continue
                try:
                    ftp.cwd(name)
                    is_dir = True
                    ftp.cwd(path)
                except error_perm:
                    is_dir = False
                    try:
                        ftp.cwd(path)
                    except error_perm:
                        pass
                size = None
                if not is_dir:
                    try:
                        size = ftp.size(name)
                    except Exception:
                        pass
                records.append({'name': name, 'is_dir': is_dir, 'size': size})
            return self._sort(records)

    def mkdir(self, path):
        path = self.clean_path(path)
        if path == '/':
            raise FTPError('Der FTP-Wurzelordner kann nicht neu angelegt werden')
        with self.connect() as ftp:
            ftp.mkd(path)
        return path

    def remote_size(self, remote):
        remote = self.clean_path(remote)
        with self.connect() as ftp:
            try:
                return ftp.size(remote)
            except Exception:
                return None

    def upload(self, local, directory, overwrite=False, progress=None):
        directory = self.clean_path(directory)
        src = Path(local)
        if not src.is_file():
            raise FTPError('Lokale Datei nicht gefunden')
        name = self.clean_name(src.name)
        remote = posixpath.join(directory, name)
        with self.connect() as ftp:
            ftp.cwd(directory)
            entries = self._list_connected(ftp)
            existing = next((item for item in entries if item['name'] == name), None)
            if existing and existing['is_dir']:
                raise FTPError(f'Im Ziel liegt bereits ein Ordner mit diesem Namen: {remote}')
            if existing and not overwrite:
                raise FTPError(f'Zieldatei existiert bereits. Überschreiben blockiert: {remote}')
            total = src.stat().st_size
            sent = 0
            def report(block):
                nonlocal sent
                sent += len(block)
                if progress:
                    progress(sent, total)
            with src.open('rb') as file:
                ftp.storbinary('STOR ' + name, file, blocksize=128 * 1024, callback=report)
        remote_size = self.remote_size(remote)
        if remote_size is not None and remote_size != src.stat().st_size:
            raise FTPError(f'Upload-Prüfung fehlgeschlagen: {remote_size} statt {src.stat().st_size} Bytes')
        if remote_size is None:
            entries = self.list(directory)
            stored = next((item for item in entries if item['name'] == name and not item['is_dir']), None)
            if stored is None:
                raise FTPError(f'Upload-Prüfung fehlgeschlagen: {remote} fehlt in der aktualisierten Dateiliste')
            if stored['size'] is not None and stored['size'] != src.stat().st_size:
                raise FTPError(f'Upload-Prüfung fehlgeschlagen: {stored["size"]} statt {src.stat().st_size} Bytes')
        return remote

    def _list_connected(self, ftp):
        records = []
        try:
            for name, meta in ftp.mlsd():
                name = posixpath.basename(name.rstrip('/'))
                if name not in ('', '.', '..'):
                    records.append({'name': name, 'is_dir': meta.get('type', '').lower() in ('dir', 'cdir', 'pdir'),
                                    'size': int(meta['size']) if meta.get('size', '').isdigit() else None})
            return records
        except (error_perm, AttributeError, EOFError, OSError, ValueError):
            lines = []
            try:
                ftp.retrlines('LIST', lines.append)
                for line in lines:
                    fields = line.split(maxsplit=8)
                    if len(fields) >= 9:
                        records.append({'name': fields[8], 'is_dir': fields[0].startswith('d'), 'size': None})
                    elif line.strip():
                        raise FTPError('Unbekanntes LIST-Format; Upload aus Sicherheitsgründen gestoppt')
                return records
            except (error_perm, EOFError, OSError) as exc:
                try:
                    return [{'name': posixpath.basename(n.rstrip('/')), 'is_dir': False, 'size': None} for n in ftp.nlst()]
                except Exception as last:
                    raise FTPError(f'Zielordner konnte nicht sicher geprüft werden: {exc}; {last}') from last

    def delete_file(self, remote):
        remote = self.clean_path(remote)
        if remote == '/':
            raise FTPError('Ungültiger Dateipfad')
        directory, name = posixpath.split(remote)
        self.clean_name(name)
        records = self.list(directory or '/')
        match = next((item for item in records if item['name'] == name), None)
        if not match:
            raise FTPError('Datei nicht gefunden. Bitte Liste aktualisieren.')
        if match['is_dir']:
            raise FTPError('Ordner können mit dieser Funktion nicht gelöscht werden.')
        with self.connect() as ftp:
            ftp.cwd(directory or '/')
            ftp.delete(name)
        return remote

    def download(self, remote, local, expected_size=None, progress=None):
        remote = self.clean_path(remote)
        if remote == '/':
            raise FTPError('Ungültiger Remote-Dateipfad')
        dst = Path(local)
        if dst.exists():
            raise FTPError('Lokale Zieldatei existiert bereits')
        actual_size = self.remote_size(remote) if expected_size is None else expected_size
        received = 0
        created = False
        def write(block):
            nonlocal received
            out.write(block)
            received += len(block)
            if progress:
                progress(received, actual_size)
        try:
            with self.connect() as ftp:
                with dst.open('xb') as out:
                    created = True
                    ftp.retrbinary('RETR ' + remote, write, blocksize=128 * 1024)
            if actual_size is not None and dst.stat().st_size != actual_size:
                raise FTPError(f'Download-Prüfung fehlgeschlagen: {dst.stat().st_size} statt {actual_size} Bytes')
        except Exception:
            if created:
                dst.unlink(missing_ok=True)
            raise
        return str(dst)
