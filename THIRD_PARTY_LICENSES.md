# Third-party licenses and attribution

The original Y2JB application is proprietary (see `LICENSE`). Third-party code retains its own permissions and notices.

| Included component | Evidence in distributed EXE | Accompanying notice |
| --- | --- | --- |
| Microsoft DirectXTex `texconv.exe` | Owner confirms official GitHub download; exact release not authenticated | `licenses/DirectXTex-MIT.txt` |
| CPython runtime | PyInstaller archive identifies `python312.dll` / Python 3.12 | Official PSF license: https://github.com/python/cpython/blob/3.12/LICENSE (exact patch and bundled notices not independently recovered) |
| Pillow 13.0.0 | Embedded `pillow-13.0.0.dist-info` | `licenses/Pillow-13.0.0-LICENSE.txt`, `licenses/Pillow-13.0.0-SBOM.json` |
| tkinterdnd2 0.7.0 | Embedded `tkinterdnd2-0.7.0.dist-info` | `licenses/TkinterDnD2-0.7.0-MIT.txt` |
| TkDnD 2.10.3 binaries | Embedded filenames including `libtkdnd2.10.3.dll` | `licenses/TkDnD-upstream-license.terms` (upstream copyright and permission notice; exact 2.10.3 package provenance not independently authenticated) |
| Tcl/Tk 8.6 | `tcl86t.dll`, `tk86t.dll`, Tk data | `licenses/TclTk-license.terms` (extracted from embedded Tk data) |
| Vendored importlib_metadata 8.7.1 | Embedded setuptools vendor metadata | `licenses/importlib_metadata-8.7.1-LICENSE.txt` |
| PyInstaller | Verified PyInstaller one-file archive; exact PyInstaller version not recovered | https://pyinstaller.org/en/stable/license.html (special exception for bundled proprietary applications) |

Pillow's embedded license document contains multiple third-party notices, and the embedded CycloneDX SBOM inventories image-codec dependencies. These are included unchanged. The upstream TkDnD and Python license links should be retained; the corresponding exact historical files could not be authenticated from the EXE alone. The present inventory is not a legal certification or antivirus scan.

PlayStation and PS5 are trademarks of their respective owners. This independent community project is not affiliated with or endorsed by Sony Interactive Entertainment.


## Binary provenance update (26 October 2026)

- `tools/texconv.exe`: embedded Windows file/product version **2026.4.1.1** (Microsoft DirectXTex March 2026 release family); Microsoft source: https://github.com/microsoft/DirectXTex/releases/tag/mar2026 . Official asset hash matching remains unverified.
- `TkDnD 2.10.3`: Georgios Petasis et al.; upstream project https://github.com/petasis/tkdnd ; upstream BSD-style terms and copyright notice must be retained for distribution. Version-matched notice inside the binary not yet established.
- Python 3.12 and PyInstaller: exact patch/build versions are not established from the supplied materials; this alone does not preclude proprietary redistribution.

## TkDnD copyright notice

The upstream license notice by Georgios Petasis (including the Kevin Walzer/WordTech attribution) is included verbatim at `licenses/TkDnD-upstream-license.terms`. The upstream text requires preserving existing copyright notices and including this notice in distributions. Source: https://github.com/petasis/tkdnd/blob/master/license.terms . The bundled 2.10.3 binary has not been hash-matched against a corresponding original distribution.


Official tkinterdnd2 0.7.0 wheel: https://pypi.org/project/tkinterdnd2/0.7.0/ (SHA-256 f93d4f5ad439648ba1673f15db3e271cdd08f075c87f43553ffcdde4e634a717). The published wheel itself was not available for binary hash matching in this review; see PROVENANCE_STATUS.md.
