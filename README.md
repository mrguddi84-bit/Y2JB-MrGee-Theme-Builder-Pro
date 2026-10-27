# 🎨 Y2JB Theme Creator Pro

**Themes erstellen und direkt auf die PS5 übertragen.**

**Version 1.0.1** · [Änderungen / Changelog](CHANGELOG.md)

[🇩🇪 Deutsch](#deutsch) · [🇬🇧 English](#english)

---

## 🇩🇪 Deutsch

Y2JB Theme Creator Pro ist eine Windows-App zum Erstellen und Übertragen von Theme-Dateien für **Y2JB auf der PS5**. Die App bereitet die benötigten Grafiken vor, findet den passenden Y2JB-Ordner und lädt die Dateien per FTP hoch.

### ✨ Funktionen

- Grafiken im **Theme Studio** bearbeiten und vorbereiten
- PNG-Dateien für ein Y2JB-Theme erstellen
- Automatische Suche unter `/user/appmeta` nach den Y2JB-Ordnern `PPSA01650`, `PPSA01651` und `PPSA01652`
- Automatischer FTP-Upload nach der Paketerstellung
- Vorhandene Dateien werden nach Bestätigung mit geprüftem lokalem Backup gesichert und erst dann ersetzt
- FTP-Uploads werden mit Diagnose, Fortschrittsanzeige und SHA-256-Prüfung überwacht
- Dashboard erkennt `icon0.png` und `icon0.dds` und zeigt deren Berechtigungen an; Icons lassen sich entsperren (`644`) oder schützen (`444`)
- PS5-IP und FTP-Port werden nach erfolgreicher Verbindung verschlüsselt mit Windows DPAPI pro Windows-Benutzer gespeichert
- Windows-EXE zum direkten Starten

### 🖥️ Dashboard

**Vor der Verbindung:**

![Y2JB Theme Creator Pro – Dashboard vor der Verbindung](assets/dashboard-de.png)

**Nach erfolgreicher Verbindung:**

![Y2JB Theme Creator Pro – Dashboard nach der Verbindung](assets/dashboard-connected.png)

### 📁 PNG-Dateien im Ordner `EINGABE`

Lege diese Dateien im Ordner `EINGABE` der App ab:

| Grafik | Größe | Dateiname | Anzahl |
|---|---:|---|---:|
| 🎮 Icon | 512 × 512 px | `icon0.png` | 1 |
| 🌌 Hintergrund | 3840 × 2160 px | `pic0.png`, `pic1.png`, `pic2.png` | 3 |

Das Hintergrundbild muss unter allen drei Dateinamen vorhanden sein. Für dasselbe Motiv kannst du die Datei dreimal kopieren und passend benennen.

### 🔌 Voraussetzung für den FTP-Upload

Auf der PS5 muss der **ftpsrv-Payload installiert und gestartet** sein. Installiere oder verwalte ihn im **Payload Manager** unter **Payload Verwaltung**. Der Payload stellt den FTP-Server bereit; der Standardport ist **2121**. Eine kompatible Payload-Umgebung ist erforderlich. Mehr dazu: [ps5-payload-dev/ftpsrv](https://github.com/ps5-payload-dev/ftpsrv).

### 🚀 Installation und Verwendung

1. Lade das Windows-Paket unter **Releases** herunter und entpacke es in einen beschreibbaren Ordner.
2. Starte `Y2JBThemeCreator.exe`.
3. Installiere und starte `ftpsrv` auf der PS5.
4. Verbinde PC und PS5 mit demselben vertrauenswürdigen lokalen Netzwerk. Trage die PS5-IP-Adresse und den FTP-Port ein (Standard: `2121`). Nach erfolgreicher Verbindung speichert die App beide Werte lokal verschlüsselt mit Windows DPAPI.
5. Wähle die Grafiken im Theme Studio aus und erstelle das Paket. Die App durchsucht `/user/appmeta` automatisch nach den Ordnern `PPSA01650`, `PPSA01651` und `PPSA01652` und startet anschließend den FTP-Upload. Bestätige gegebenenfalls das Überschreiben vorhandener Dateien.

### ⚠️ Sicherheit

FTP ist unverschlüsselt. Nutze den Upload nur in einem vertrauenswürdigen lokalen Netzwerk und veröffentliche den FTP-Dienst nicht im Internet. Ändere nur Systeme und Dateien, zu deren Änderung du berechtigt bist.

### 📜 Rechte und Hinweise

© 2026 MrGee. Alle Rechte vorbehalten. Der Anwendungscode und die originalen Y2JB-Grafiken sind **proprietär**. Die Veröffentlichung des Quellcodes erteilt keine Open-Source-Lizenz. Details: [LICENSE](LICENSE). Drittanbieterkomponenten haben eigene Lizenzen und Herkunftshinweise: [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) und [CREDITS.md](CREDITS.md).

Dieses Projekt ist **inoffiziell** und weder mit Sony Interactive Entertainment verbunden noch von Sony unterstützt. Das Y2JB-Logo gehört dem Projektinhaber. Die Beispielgrafiken wurden nach dessen Angaben mit ChatGPT erstellt. Marken Dritter gehören ihren jeweiligen Inhabern.

### 🛠️ Build-Hinweis

Die Windows-EXE ist ein stabiler Launcher und lädt die versionierte Anwendung aus dem benachbarten Ordner `app`. Version 1.0.1 aktualisiert den Python-Quellcode, ohne den Launcher neu zu bauen. Verbindungsdaten werden pro Windows-Benutzer mit DPAPI verschlüsselt gespeichert.

---

## 🇬🇧 English

Y2JB Theme Creator Pro is a Windows app for creating and transferring theme files for **Y2JB on PS5**. It prepares the required artwork, finds the matching Y2JB folder, and uploads the files over FTP.

### ✨ Features

- Prepare and edit graphics in **Theme Studio**
- Create the PNG files required for a Y2JB theme
- Automatically search `/user/appmeta` for Y2JB folders `PPSA01650`, `PPSA01651`, and `PPSA01652`
- Automatically upload files over FTP after package creation
- Existing files are backed up locally and verified before replacement after confirmation
- FTP uploads show diagnostics and progress and are verified with SHA-256
- The dashboard detects `icon0.png` and `icon0.dds` and shows their permissions; icons can be unlocked (`644`) or protected (`444`)
- The PS5 IP and FTP port are saved locally after a successful connection using Windows DPAPI encryption for the current Windows user
- Ready-to-run Windows executable

### 🖥️ Dashboard

**Before connecting:**

![Y2JB Theme Creator Pro dashboard before connecting](assets/dashboard-en.png)

### 📁 PNG files in the `EINGABE` folder

Place these files in the app's `EINGABE` folder:

| Graphic | Dimensions | Filename | Count |
|---|---:|---|---:|
| 🎮 Icon | 512 × 512 px | `icon0.png` | 1 |
| 🌌 Background | 3840 × 2160 px | `pic0.png`, `pic1.png`, `pic2.png` | 3 |

The background must be present under all three filenames. To use the same artwork for each one, copy the image three times and name each copy accordingly.

### 🔌 FTP upload requirement

The **ftpsrv payload must be installed and running on the PS5**. Install or manage it in **Payload Manager** under **Payload Verwaltung** (Payload Management). It provides the FTP server and uses port **2121** by default. A compatible payload environment is required. See [ps5-payload-dev/ftpsrv](https://github.com/ps5-payload-dev/ftpsrv).

### 🚀 Installation and usage

1. Download the Windows package from **Releases** and extract it to a writable folder.
2. Launch `Y2JBThemeCreator.exe`.
3. Install and start `ftpsrv` on the PS5.
4. Connect the PC and PS5 to the same trusted local network. Enter the PS5 IP address and FTP port in the app (default: `2121`). After a successful connection, both values are stored locally using Windows DPAPI encryption.
5. Select your graphics in Theme Studio and create the package. The app automatically scans `/user/appmeta` for folders `PPSA01650`, `PPSA01651`, and `PPSA01652`, then starts the FTP upload. Confirm if existing files need to be overwritten.

### ⚠️ Security

FTP is unencrypted. Use uploads only on a trusted local network and do not expose the FTP service to the internet. Only modify systems and files you are authorized to manage.

### 📜 Rights and notices

© 2026 MrGee. All rights reserved. The application source and original Y2JB artwork are **proprietary**. Public source availability does not grant an open-source license. See [LICENSE](LICENSE). Third-party components retain their own licenses and attribution: [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) and [CREDITS.md](CREDITS.md).

This is an **unofficial** project and is not affiliated with or endorsed by Sony Interactive Entertainment. The Y2JB logo belongs to the project owner. The sample graphics were reportedly generated using ChatGPT. Third-party trademarks remain the property of their respective owners.

### 🛠️ Build note

The Windows executable is a stable launcher that loads the versioned application from the adjacent `app` folder. Version 1.0.1 updates the Python source without rebuilding the launcher. Connection settings are stored per Windows user using DPAPI.

---

## 🖼️ Beispiel-Theme / Example theme

**Deutsch:** Bild 1 ist das Icon, Bild 2 der Hintergrund. Für die Verwendung in der App gelten die oben genannten PNG-Größen.

**English:** Image 1 is the icon; image 2 is the background. The PNG dimensions listed above still apply when using files in the app.

<p align="center">
  <img src="assets/file_000000008d0082118dce526bd96d0303.png" alt="Icon – Bild 1 / image 1" width="240">
  <img src="assets/file_00000000f9748210917ae68e43114c88.png" alt="Hintergrund – Bild 2 / background image 2" width="480">
</p>
