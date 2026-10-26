# Binary dependency audit — 2026-10-26

## Method

Read the PyInstaller CArchive cookie and table of contents directly from the provided `Y2JB_Theme_Creator_MrGee.exe`, without executing or changing the application. Archive contains **1,222 entries**. Decompressed selected embedded package license files and the Pillow CycloneDX SBOM; these files are included under `licenses/`. Full archive listing is provided in `PYINSTALLER_ARCHIVE_INVENTORY.txt`.

## Confirmed by embedded filenames/metadata

- Python **3.12** (`python312.dll`), patch version not established.
- **Pillow 13.0.0** (embedded distribution metadata and full license document).
- **tkinterdnd2 0.7.0** (embedded distribution metadata and MIT license).
- **TkDnD 2.10.3** (multiple architecture-specific bundled library filenames, including Windows x64).
- **Tcl/Tk 8.6** (runtime DLL names, license.terms extracted from Tk data).
- **importlib_metadata 8.7.1**, vendored under setuptools, license included.
- PyInstaller one-file executable format, exact bootloader version not established.

Pillow 13.0.0 embedded SBOM lists bundled codec libraries (FreeType, HarfBuzz, libavif, libjpeg-turbo, libwebp, OpenJPEG, zlib and others). See `licenses/Pillow-13.0.0-SBOM.json` and the original license bundle for notices. These components do **not** imply that their separate source code is part of the proprietary Y2JB source.

## Remaining limitations

- The embedded Windows VERSIONINFO identifies texconv FileVersion and ProductVersion as **2026.4.1.1**, consistent with Microsoft DirectXTex March 2026 (NuGet 2026.4.1). The binary has **not** been byte-for-byte matched against an official Microsoft asset; origin is user-attested. SHA-256: `563d9eca9882207438fe9bf39a03802c987692360da86f1aacab361f40ba904c`.
- The exact CPython 3.12 patch release and PyInstaller version are not recovered.
- TkDnD **2.10.3** is identified in embedded file paths. Its upstream is Georgios Petasis’s TkDND project, described as BSD-licensed; the exact license text for this packaged 2.10.3 build has **not** been extracted from the embedded EXE. Preserve the upstream copyright notice and consult https://github.com/petasis/tkdnd for the authoritative terms.
- No malware analysis, Windows execution, or legal certification was performed here; the owner reports a successful Windows functional test.

## Integrity

The supplied Windows EXE, all existing images/icons, and application source files are retained byte-for-byte. Only documentation and extracted notices are added. `SHA256SUMS.txt` covers all files except itself.

## Publication decision

Version granularity for CPython and PyInstaller is **not itself a separate license requirement**. Licensing obligations attach to the actual distributed components, including their notices. This review does not certify complete third-party compliance or establish byte-for-byte provenance of every binary.

### TkDnD licensing follow-up
Upstream `petasis/tkdnd/license.terms` verified and reproduced in `licenses/TkDnD-upstream-license.terms`. Redistribution is permitted provided existing copyright notices are retained and the notice is included verbatim. The embedded TkDnD 2.10.3 binary was not matched against an independently obtained historical binary.
