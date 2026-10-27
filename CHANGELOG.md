# Y2JB Theme Creator ©MrGee — v1.0.1

## Deutsch
- FTP-Upload und Überschreiben vorhandener Dateien verbessert; FTP-Antwort `226 File deleted` behandelt.
- Backup, Upload-Diagnose, Fortschrittsanzeige und SHA-256-Prüfung verbessert.
- Automatischer Scan von `icon0.png` und `icon0.dds` sowie Berechtigungsanzeige im Dashboard.
- Icons über FTP freigeben (644) und sperren (444), optionaler Schreibschutz nach Upload.
- Theme-Paket-Upload aus Dashboard und Theme Studio.
- PS5-IP und FTP-Port werden nach erfolgreicher Verbindung lokal mit Windows DPAPI verschlüsselt gespeichert.

## English
- Improved FTP uploads and replacement of existing files, including handling `226 File deleted`.
- Improved backups, upload diagnostics, progress display and SHA-256 verification.
- Automatic detection of `icon0.png` and `icon0.dds` with permissions shown in the dashboard.
- Unlock (644) and protect (444) icons over FTP, with optional protection after upload.
- Theme package upload from Dashboard and Theme Studio.
- PS5 IP and FTP port saved locally using Windows DPAPI after successful connection.

## Installation / Installation
Extract the entire ZIP to a folder, then run `Y2JBThemeCreator.exe`. Keep the `app`, `assets`, `tools` and `EINGABE` folders alongside the EXE. Windows 64-bit required. Start ftpsrv on the PS5 separately.

## Verification note
Source files passed Python syntax compilation and archive integrity checks. Windows GUI/PS5 end-to-end testing was performed by the project user, not by this release preparation environment.
