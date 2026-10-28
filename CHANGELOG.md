# Changelog — Y2JB Theme Creator

## v2.0 — 2026-10-28 (current)

### Deutsch
- Theme Studio mit kompakterem Layout und überarbeitetem Ablauf.
- Theme-Paket-Erstellung und FTP-Upload mit Statusanzeige im Dashboard.
- Vorhandene Dateien werden nur nach Bestätigung überschrieben.
- Vereinfachte Anwendungsstruktur mit `EINGABE` und `PS5_Upload`.
- Überarbeiteter Windows-Installer mit auswählbarem Installationsverzeichnis.
- Kostenlose proprietäre Veröffentlichung ohne öffentlichen v2.0-Python-Quellcode.

### English
- More compact Theme Studio layout and updated workflow.
- Theme package creation and FTP uploads with status shown in the Dashboard.
- Existing files are overwritten only after confirmation.
- Simplified application structure with `EINGABE` and `PS5_Upload`.
- Revised Windows installer with a selectable installation directory.
- Free proprietary release; no v2.0 Python source code is publicly distributed.

## v1.0.1 — archived history

### Deutsch
- FTP-Upload und Überschreiben vorhandener Dateien verbessert; FTP-Antwort `226 File deleted` behandelt.
- Backup, Upload-Diagnose, Fortschrittsanzeige und SHA-256-Prüfung verbessert.
- Automatischer Scan von `icon0.png` und `icon0.dds` sowie Berechtigungsanzeige im Dashboard.
- Icons über FTP freigeben (`644`) und sperren (`444`), optionaler Schreibschutz nach Upload.
- Theme-Paket-Upload aus Dashboard und Theme Studio.
- PS5-IP und FTP-Port werden nach erfolgreicher Verbindung lokal mit Windows DPAPI verschlüsselt gespeichert.

### English
- Improved FTP uploads and replacement of existing files, including handling `226 File deleted`.
- Improved backups, upload diagnostics, progress display, and SHA-256 verification.
- Automatic detection of `icon0.png` and `icon0.dds` with permissions shown in the Dashboard.
- Unlock (`644`) and protect (`444`) icons over FTP, with optional protection after upload.
- Theme package upload from Dashboard and Theme Studio.
- PS5 IP and FTP port are saved locally using Windows DPAPI after a successful connection.

## v1.0.0 — initial release (archived history)

### Deutsch
- Erste öffentliche Version zum Erstellen der für Y2JB auf PS5 benötigten Theme-Dateien.
- Automatische Suche nach den passenden Y2JB-Ordnern und FTP-Upload.
- Vorhandene Dateien werden nur nach Bestätigung überschrieben.

### English
- First public release for creating theme files used by Y2JB on PS5.
- Automatic detection of the matching Y2JB folders and FTP upload.
- Existing files are overwritten only after confirmation.
