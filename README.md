# Y2JB MrGee Theme Builder Pro

**Deutsch** | [English](#english)

## Deutsch

**Y2JB MrGee Theme Builder Pro** ist eine Windows-Anwendung zum Erstellen von PS5-Theme-Paketen. Der Theme Creator sucht automatisch nach dem passenden Y2JB-Verzeichnis auf der PS5 und lädt das fertige Paket anschließend automatisch per FTP hoch.

### Funktionen
- Theme Studio zur Bearbeitung und Vorbereitung von Grafiken
- Bildkonvertierung für die benötigten Theme-Dateien
- Erstellung eines PS5-Theme-Pakets
- Automatische Suche nach dem richtigen Y2JB-Verzeichnis auf der PS5
- Automatischer FTP-Upload nach erfolgreicher Paketerstellung; vorhandene Dateien werden nur nach Bestätigung überschrieben
- Windows-EXE zum direkten Starten

### Voraussetzung: ftpsrv-Payload auf der PS5
Für den automatischen FTP-Transfer muss auf der PS5 der **ftpsrv-Payload installiert und gestartet** sein. Installiere bzw. verwalte ihn im **Payload Manager** unter **Payload Verwaltung**. Der Payload stellt den FTP-Server auf der PS5 bereit; der Standardport ist **2121**. Er setzt eine kompatible Payload-Umgebung auf der PS5 voraus. Weitere Informationen: [ps5-payload-dev/ftpsrv](https://github.com/ps5-payload-dev/ftpsrv).

### Installation und Verwendung
1. Lade das Windows-Paket aus den **Releases** herunter und entpacke es in einen beschreibbaren Ordner.
2. Starte `Y2JB_Theme_Creator_MrGee.exe`.
3. Installiere und starte `ftpsrv` auf der PS5 über den Payload Manager unter **Payload Verwaltung**.
4. Verbinde PC und PS5 mit demselben vertrauenswürdigen lokalen Netzwerk und trage in der App die IP-Adresse der PS5 sowie den FTP-Port ein (Standard: `2121`).
5. Wähle die Grafiken im Theme Studio aus und erstelle das PS5-Paket. Der Creator findet das Y2JB-Verzeichnis automatisch und beginnt den FTP-Upload automatisch. Bestätige die Abfrage, falls Dateien überschrieben werden sollen.

**Sicherheit:** FTP ist unverschlüsselt. Nutze den Upload nur in einem vertrauenswürdigen lokalen Netzwerk und veröffentliche den FTP-Dienst nicht im Internet. Änderungen an Zieldateien erfolgen auf eigene Verantwortung und nur auf Systemen, zu deren Änderung du berechtigt bist.

### Rechte und Hinweise
© 2026 MrGee. Alle Rechte vorbehalten. Der eigene Anwendungscode und die originalen Y2JB-Grafiken sind **proprietär**. Die öffentliche Bereitstellung des Quellcodes ist keine Open-Source-Lizenz. Details in [LICENSE](LICENSE). Drittanbieterkomponenten haben eigene Lizenzen; siehe [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md), [CREDITS.md](CREDITS.md) und [DEPENDENCY_AUDIT.md](DEPENDENCY_AUDIT.md).

Dieses Projekt ist **inoffiziell** und weder mit Sony Interactive Entertainment verbunden noch von Sony unterstützt. Das Y2JB-Logo stammt vom Projektinhaber; die mitgelieferten Beispielgrafiken wurden nach dessen Angaben mit ChatGPT erzeugt. Marken Dritter gehören ihren jeweiligen Inhabern.

**Build-Hinweis:** Die vorhandene Windows-EXE wurde für die GitHub-Vorbereitung nicht verändert oder neu gebaut. Ihre gespeicherte Standard-IP kann von der des veröffentlichten Python-Codes abweichen. Eine vollständig reproduzierbare Build-Konfiguration ist nicht enthalten. Offene Nachweise zu Drittanbieter-Binärdateien sind in [PROVENANCE_STATUS.md](PROVENANCE_STATUS.md) dokumentiert.

---

## English

**Y2JB MrGee Theme Builder Pro** is a Windows application for creating PS5 theme packages. Theme Creator automatically scans the PS5 for the correct Y2JB directory and automatically uploads the finished package over FTP.

### Features
- Theme Studio for preparing and editing graphics
- Image conversion for the required theme assets
- PS5 theme package creation
- Automatic detection of the correct Y2JB directory on the PS5
- Automatic FTP upload after package creation; existing files are overwritten only after confirmation
- Ready-to-run Windows executable

### Requirement: ftpsrv payload on the PS5
For automatic FTP transfer, the **ftpsrv payload must be installed and running on the PS5**. Install or manage it in **Payload Manager** under **Payload Verwaltung** (Payload Management). The payload provides the FTP server on the PS5 and uses port **2121** by default. A compatible payload environment is required. See [ps5-payload-dev/ftpsrv](https://github.com/ps5-payload-dev/ftpsrv) for details.

### Installation and usage
1. Download the Windows package from **Releases** and extract it into a writable folder.
2. Launch `Y2JB_Theme_Creator_MrGee.exe`.
3. Install and start `ftpsrv` on the PS5 through Payload Manager under **Payload Verwaltung** (Payload Management).
4. Connect the PC and PS5 to the same trusted local network, then enter the PS5 IP address and FTP port in the app (default: `2121`).
5. Select your images in Theme Studio and create the PS5 package. Theme Creator automatically finds the Y2JB directory and starts the FTP upload. Confirm if existing files need to be overwritten.

**Security:** FTP is unencrypted. Use uploads only on a trusted local network; do not expose the FTP service to the internet. Only modify systems and files you are authorized to manage.

### Rights and notices
© 2026 MrGee. All rights reserved. The original application source and Y2JB artwork are **proprietary**. Public source availability does not grant an open-source license. See [LICENSE](LICENSE). Third-party components retain their own licenses; see [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md), [CREDITS.md](CREDITS.md), and [DEPENDENCY_AUDIT.md](DEPENDENCY_AUDIT.md).

This is an **unofficial** project and is not affiliated with or endorsed by Sony Interactive Entertainment. The Y2JB logo belongs to the project owner; the included sample images were reportedly generated using ChatGPT. Third-party trademarks remain the property of their respective owners.

**Build note:** The existing Windows executable was not modified or rebuilt for GitHub publication. Its saved default IP may differ from the published Python source. A fully reproducible build configuration is not provided. Outstanding binary provenance checks are documented in [PROVENANCE_STATUS.md](PROVENANCE_STATUS.md).
