# Third-party licenses / Lizenzen Dritter — Y2JB Theme Creator 3.0

This inventory describes the components used by the current v3.0 portable Windows app. The Y2JB Theme Creator application remains proprietary; third-party components retain their own copyright and license terms.

Diese Übersicht beschreibt die Komponenten der aktuellen portablen Windows-App v3.0. Die Y2JB-Theme-Creator-Anwendung bleibt proprietär; für Drittanbieterkomponenten gelten deren jeweilige Urheber- und Lizenzbedingungen.

| Component / Komponente | Use in the app / Verwendung | License / Lizenz and source / Lizenz und Quelle |
| --- | --- | --- |
| CPython 3.12.10 | Application runtime and standard library / Laufzeit und Standardbibliothek | PSF License 2 and applicable historical component terms / PSF-Lizenz 2 und geltende Komponentenbedingungen — [Python license](https://docs.python.org/3.12/license.html) |
| Tcl/Tk 8.6 | Tkinter GUI / Tkinter-Oberfläche | Tcl/Tk BSD-style terms / BSD-artige Bedingungen — [Tcl/Tk license](https://www.tcl.tk/software/tcltk/license.html) |
| Pillow 13.0.0 | Image processing, resizing and PNG handling / Bildverarbeitung, Skalierung und PNG | MIT-CMU and included third-party notices / MIT-CMU und enthaltene Drittanbieterhinweise — [Pillow](https://github.com/python-pillow/Pillow) |
| tkinterdnd2 0.7.0 | Drag-and-drop integration / Drag-and-drop-Integration | MIT — [tkinterdnd2](https://github.com/Eliav2/tkinterdnd2) |
| TkDnD 2.10.3 | Native drag-and-drop components for Tk / Native Drag-and-drop-Komponenten für Tk | BSD-style upstream terms / BSD-artige Upstream-Bedingungen — [TkDnD](https://github.com/petasis/tkdnd) |
| ispc_texcomp 1.0.1 | Native BC7 texture encoding / Native BC7-Texturcodierung | MIT — [Python bindings](https://github.com/K0lb3/ispc_texcomp_py) |
| zftpd payload 1.7.0 | Included PS5 FTP payload, started through an available elfldr service / Enthaltener PS5-FTP-Payload, Start über einen verfügbaren elfldr-Dienst | MIT, copyright Seregon — [zftpd](https://github.com/seregonwar/zftpd) |
| Nuitka 4.3.1 | Compiler used for the portable Windows build / Compiler für den portablen Windows-Build | AGPLv3 compiler with runtime exception for compiled applications — [Nuitka runtime exception](https://github.com/Nuitka/Nuitka/blob/develop/LICENSE-RUNTIME.txt) |
| ftpsrv | Optional official PS5 FTP payload. It is fetched by the PS5 from the upstream release when launched in the app; it is not included in the Windows app / Optionaler offizieller PS5-FTP-Payload. Beim App-Start lädt ihn die PS5 aus dem Upstream-Release; er ist nicht in der Windows-App enthalten. | Upstream license applies to that separately downloaded payload / Für den separat heruntergeladenen Payload gilt die Upstream-Lizenz — [ps5-payload-dev/ftpsrv](https://github.com/ps5-payload-dev/ftpsrv) |

### Redistribution / Weitergabe

Retain the applicable copyright notices and full license texts when redistributing third-party components or payloads. The MIT, BSD-style, Tcl/Tk and PSF terms do not require publishing the Y2JB application source code. Nuitka's runtime exception applies to the compiled application; it does not change the license of the Nuitka compiler itself.

Bei der Weitergabe von Drittanbieterkomponenten oder Payloads müssen die geltenden Urheberhinweise und vollständigen Lizenztexte erhalten bleiben. Die MIT-, BSD-artigen, Tcl/Tk- und PSF-Bedingungen verlangen nicht die Veröffentlichung des Y2JB-Anwendungscodes. Nuitkas Runtime Exception gilt für die kompilierte Anwendung; die Lizenz des Nuitka-Compilers selbst bleibt davon unberührt.

Windows, PlayStation and PS5 are trademarks of their respective owners. This independent project is not affiliated with or endorsed by Sony Interactive Entertainment.

Windows, PlayStation und PS5 sind Marken der jeweiligen Rechteinhaber. Dieses unabhängige Projekt ist nicht mit Sony Interactive Entertainment verbunden und wird nicht von Sony unterstützt.

**Inventory reviewed:** 31 October 2026, based on the v3.0 app and supplied component inventory. License obligations are summarized for attribution and are not a legal opinion.

**Prüfstand:** 31. Oktober 2026, basierend auf der App v3.0 und der bereitgestellten Komponentenliste. Die Lizenzpflichten sind zu Informationszwecken zusammengefasst und stellen keine Rechtsberatung dar.
