<div align="center">

# 🎮 Y2JB Theme Creator 3.0

**Create · Customize · Upload**

![Version](https://img.shields.io/badge/version-3.0-blue) ![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6) ![Portable](https://img.shields.io/badge/build-portable-success) ![BC7](https://img.shields.io/badge/encoder-BC7-purple)

**Entwickelt von MrGee mit KI-Unterstützung**

**🇩🇪 Deutsch** · [🇬🇧 English](README.md) · [🇪🇸 Español](README.es.md) · [🇫🇷 Français](README.fr.md) · [🇵🇹 Português](README.pt.md)

[**Download / Releases**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/releases) · [**Changelog**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/blob/main/CHANGELOG.md) · [**Credits**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/blob/main/CREDITS.md)

</div>

---

## ✨ Erstelle deine eigenen Y2JB-Themes

Wandle eigene PNG-Grafiken in Y2JB-Theme-Dateien um, gestalte Icons und 4K-Hintergründe und übertrage alles auf eine kompatible PS5. Y2JB Theme Creator ist ein unabhängiges Windows-Homebrew-Tool.

[Funktionen](#features) · [Schnellstart](#quick-start) · [Bildvorgaben](#image-specifications) · [FTP-Payloads und Voraussetzungen](#ftp-payloads) · [BC7-Performance – unsere Messwerte](#bc7-benchmarks) · [Drei Oberflächen](#screenshots) · [Sicherheitshinweise](#safety) · [Credits und Hinweise](#credits)

<a id="features"></a>
## 🚀 Funktionen

| | |
|---|---|
| 🎨 | Eigene PNG-Grafiken in Y2JB-Theme-Dateien umwandeln |
| 🖼️ | 4K-Hintergründe (3840 × 2160) und Icons mit 512 × 512 Pixeln |
| ⚡ | Native parallele BC7-DDS-Konvertierung mit Fast- und Balanced-Profil |
| 📡 | FTP-Verwaltung: mitgelieferter zftpd und offizieller ftpsrv-Start |
| 🔍 | FTP-Diagnose, Zielordnersuche und Upload-Fortschritt |
| 🛡️ | Backups, Wiederherstellung und SHA-256-Upload-Prüfung |
| ✏️ | Y2JB App-Namen bearbeiten mit Datenbank-Backup und Wiederherstellung |
| 🎭 | Drei Designs: Classic, Minimal und Neon |
| 🌍 | Deutsch, Englisch, Spanisch, Französisch und Portugiesisch |

<a id="quick-start"></a>
## 🛠️ Schnellstart

1. Portable Windows-Version herunterladen, entpacken und `Y2JBThemeCreator.exe` starten.
2. PS5-IP eingeben. Mitgelieferten zftpd über einen erreichbaren elfldr-Dienst starten oder offiziellen ftpsrv direkt über die App laden und starten. Ein bereits laufender FTP-Server ist ebenfalls möglich.
3. PNG-Bilder im Theme Creator von **einem beliebigen Speicherort auf dem PC** auswählen.
4. Y2JB-Theme-Dateien erstellen und auf Wunsch per FTP hochladen.

<a id="image-specifications"></a>
## 🖼️ Bildvorgaben

| Datei | Verwendung | Resolution |
|---|---|---|
| `icon0.png` | Theme-Icon | 512 × 512 |
| `pic0.png` | Hintergrund 1 | 3840 × 2160 |
| `pic1.png` | Hintergrund 2 | 3840 × 2160 |
| `pic2.png` | Hintergrund 3 | 3840 × 2160 |

Die Anwendung passt Grafiken automatisch auf die benötigten Zielgrößen an. Ein Motiv kann mehrfach verwendet werden.

<a id="ftp-payloads"></a>
## 📡 FTP-Payloads und Voraussetzungen

**zftpd v1.7.0 ist im Programmpaket enthalten** und kann über einen erreichbaren elfldr-Dienst gestartet werden. **ftpsrv ist nicht enthalten:** Über die integrierte ftpsrv-Funktion lädt **die PS5 die offizielle ELF-Datei direkt aus dem GitHub-Release** und startet sie über elfldr. Dafür benötigt die PS5 Internetzugang. Alternativ lässt sich ftpsrv über einen kompatiblen Payload Manager starten. Anschließend prüft die App die FTP-Erreichbarkeit.

- [Official ftpsrv repository](https://github.com/ps5-payload-dev/ftpsrv)
- [Official ftpsrv ELF release](https://github.com/ps5-payload-dev/ftpsrv/releases/latest/download/ftpsrv-ps5.elf)
- zftpd v1.7.0: bundled in the Windows build, with its third-party license.

<a id="bc7-benchmarks"></a>
## ⚡ BC7-Performance – unsere Messwerte

Vergleich mit echten Grafiken auf einem Test-PC. Fast war beim Icon etwa **8,7-mal schneller** und beim 4K-Hintergrund rund **24 % schneller** als der bisherige Encoder. Bei beiden Testmotiven war auch der PSNR höher. Die Ergebnisse können je nach CPU, Motiv und Einstellungen abweichen.

### Icon – 512 × 512

| Encoder | Zeit | Qualität (PSNR) |
|---|---:|---:|
| **Y2JB Fast** | **0,026** s | 35,43 dB |
| Y2JB Balanced | 0,057 s | **36,96** dB |
| Bisheriger Encoder | 0,225 s | 33,78 dB |

### Hintergrund – 3840 × 2160

| Encoder | Zeit | Qualität (PSNR) |
|---|---:|---:|
| **Y2JB Fast** | **0,677** s | 45,73 dB |
| Y2JB Balanced | 1,349 s | **46,11** dB |
| Bisheriger Encoder | 0,896 s | 44,51 dB |

![BC7 benchmark comparison](assets/bc7-benchmark.svg)

> Test results are specific to the measured images and hardware. PSNR is a metric, not a universal visual-quality guarantee.

<a id="screenshots"></a>
## 🎭 Drei Oberflächen

| Classic | Minimal | Neon |
|---|---|---|
| ![Classic](assets/dashboard-classic.png) | ![Minimal](assets/dashboard-minimal.png) | ![Neon](assets/dashboard-neon.png) |

<a id="safety"></a>
## ⚠️ Sicherheitshinweise

FTP ist unverschlüsselt und sollte nur im vertrauenswürdigen lokalen Netzwerk verwendet werden. Änderungen an PS5-Datenbanken sind sensibel: Backups aufbewahren und Zieldateien prüfen. Für das Starten von Payloads wird eine kompatible PS5-Homebrew-Umgebung mit elfldr benötigt.

<a id="credits"></a>
## ❤️ Credits und Hinweise

**Entwickelt von MrGee mit KI-Unterstützung.** Vielen Dank an die Mitwirkenden von zftpd, ftpsrv, ispc_texcomp, Pillow, TkinterDnD, Tk/Tcl, Python und Nuitka. Für Drittanbieterkomponenten gelten deren eigene Lizenzen. Unabhängiges Homebrew-Projekt, nicht mit Sony Interactive Entertainment verbunden oder von Sony unterstützt.

Weitere Informationen: [CHANGELOG.md](CHANGELOG.md) · [CREDITS.md](CREDITS.md) · [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) · [LICENSE](LICENSE)
