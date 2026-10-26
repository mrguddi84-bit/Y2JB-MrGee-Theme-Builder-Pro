# Provenance and verification status — 2026-10-26

## TkinterDnD2 / TkDnD

The application binary inventory includes `tkinterdnd2` and TkDnD 2.10.3 files. The official PyPI release `tkinterdnd2 0.7.0` (published 2026-10-25) is identified and lists the wheel `tkinterdnd2-0.7.0-py3-none-any.whl` with SHA-256:

`f93d4f5ad439648ba1673f15db3e271cdd08f075c87f43553ffcdde4e634a717`

Source: https://pypi.org/project/tkinterdnd2/0.7.0/

The PyPI publisher states that its TkDnD binaries come from Georgios Petasis's TkDnD releases and builds by Squiblydoo. The publisher's PyInstaller hook bundles TkDnD files automatically. This matches the user's autobuilder workflow. The wrapper is listed as MIT; TkDnD upstream copyright and redistribution conditions are included in `licenses/TkDnD-upstream-license.terms`.

**Verification boundary:** A direct download of the PyPI wheel failed in this environment. Consequently the embedded DLL has NOT been hash-matched to the wheel, and an independent, byte-for-byte binary provenance assertion cannot be made. PyPI also reports no uploaded provenance attestations for this wheel. Do not describe the DLL as hash-verified.

## Other components

- DirectXTex `texconv.exe`: the user confirms it came from Microsoft's GitHub release. Windows version metadata `2026.4.1.1`; official release SHA-256 match not independently established. MIT notice included.
- Python 3.12, Pillow 13.0.0, Tcl/Tk 8.6, tkinterdnd2 0.7.0 and TkDnD 2.10.3 are indicated by embedded inventory and metadata.
- Exact Python patch and PyInstaller bootloader versions are not independently established; not inherently mandatory for redistribution rights.

## Scope

Original EXE, code, icons, images and application layout are preserved without modifications. This documentation is a provenance review, not a security certification or legal opinion.
