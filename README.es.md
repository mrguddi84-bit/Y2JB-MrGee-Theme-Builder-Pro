<div align="center">

# 🎮 Y2JB Theme Creator 3.0

**Create · Customize · Upload**

![Version](https://img.shields.io/badge/version-3.0-blue) ![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6) ![Portable](https://img.shields.io/badge/build-portable-success) ![BC7](https://img.shields.io/badge/encoder-BC7-purple)

**Desarrollado por MrGee con ayuda de IA**

[🇩🇪 Deutsch](README.de.md) · [🇬🇧 English](README.md) · **🇪🇸 Español** · [🇫🇷 Français](README.fr.md) · [🇵🇹 Português](README.pt.md)

[**Descarga / Releases**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/releases) · [**Changelog**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/blob/main/CHANGELOG.md) · [**Credits**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/blob/main/CREDITS.md)

</div>

---

## ✨ Crea tus propios temas Y2JB

Convierte tus imágenes PNG en archivos de temas Y2JB, personaliza iconos y fondos 4K y súbelos a una PS5 compatible. Herramienta independiente de homebrew para Windows.

[Funciones](#features) · [Inicio rápido](#quick-start) · [Especificaciones de imágenes](#image-specifications) · [Payloads FTP y requisitos](#ftp-payloads) · [Rendimiento BC7 — resultados medidos](#bc7-benchmarks) · [Tres interfaces](#screenshots) · [Seguridad](#safety) · [Créditos y aviso](#credits)

<a id="features"></a>
## 🚀 Funciones

| | |
|---|---|
| 🎨 | Convertir imágenes PNG en archivos de temas Y2JB |
| 🖼️ | Fondos 4K (3840 × 2160) e iconos de 512 × 512 |
| ⚡ | Codificación BC7 DDS nativa y paralela: Fast y Balanced |
| 📡 | Gestión FTP: zftpd incluido e inicio oficial de ftpsrv |
| 🔍 | Diagnóstico FTP, búsqueda de destino y progreso |
| 🛡️ | Copias de seguridad, restauración y verificación SHA-256 |
| ✏️ | Editar nombres de aplicaciones Y2JB con copias de las bases de datos |
| 🎭 | Tres diseños: Classic, Minimal y Neon |
| 🌍 | Alemán, inglés, español, francés y portugués |

<a id="quick-start"></a>
## 🛠️ Inicio rápido

1. Descarga y extrae la versión portátil de Windows; ejecuta `Y2JBThemeCreator.exe`.
2. Introduce la IP de tu PS5. Inicia zftpd incluido mediante elfldr o ftpsrv oficial desde la aplicación; también puedes usar un servidor FTP ya activo.
3. Selecciona archivos PNG desde **cualquier carpeta de tu PC**.
4. Crea los archivos de tema Y2JB y súbelos por FTP si lo deseas.

<a id="image-specifications"></a>
## 🖼️ Especificaciones de imágenes

| Archivo | Uso | Resolution |
|---|---|---|
| `icon0.png` | Icono del tema | 512 × 512 |
| `pic0.png` | Fondo 1 | 3840 × 2160 |
| `pic1.png` | Fondo 2 | 3840 × 2160 |
| `pic2.png` | Fondo 3 | 3840 × 2160 |

La aplicación adapta automáticamente las imágenes al tamaño de salida. Puedes reutilizar una imagen para varios fondos.

<a id="ftp-payloads"></a>
## 📡 Payloads FTP y requisitos

**zftpd v1.7.0 viene incluido** y puede iniciarse mediante un servicio elfldr accesible. **ftpsrv no viene incluido:** con la función integrada, **la PS5 descarga el ELF oficial directamente de GitHub** y lo inicia mediante elfldr. La PS5 necesita Internet. También puedes iniciar ftpsrv desde un Payload Manager compatible. Después, la aplicación comprueba el FTP.

- [Official ftpsrv repository](https://github.com/ps5-payload-dev/ftpsrv)
- [Official ftpsrv ELF release](https://github.com/ps5-payload-dev/ftpsrv/releases/latest/download/ftpsrv-ps5.elf)
- zftpd v1.7.0: bundled in the Windows build, with its third-party license.

<a id="bc7-benchmarks"></a>
## ⚡ Rendimiento BC7 — resultados medidos

Prueba con imágenes reales en un PC. Fast fue aproximadamente **8,7 veces más rápido con el icono** y **24 % más rápido con el fondo 4K** que el codificador anterior; también obtuvo mayor PSNR en ambas imágenes. Los resultados pueden variar.

### Icono — 512 × 512

| Codificador | Tiempo | Calidad (PSNR) |
|---|---:|---:|
| **Y2JB Fast** | **0,026** s | 35,43 dB |
| Y2JB Balanced | 0,057 s | **36,96** dB |
| Codificador anterior | 0,225 s | 33,78 dB |

### Fondo — 3840 × 2160

| Codificador | Tiempo | Calidad (PSNR) |
|---|---:|---:|
| **Y2JB Fast** | **0,677** s | 45,73 dB |
| Y2JB Balanced | 1,349 s | **46,11** dB |
| Codificador anterior | 0,896 s | 44,51 dB |

![BC7 benchmark comparison](assets/bc7-benchmark.svg)

> Test results are specific to the measured images and hardware. PSNR is a metric, not a universal visual-quality guarantee.

<a id="screenshots"></a>
## 🎭 Tres interfaces

| Classic | Minimal | Neon |
|---|---|---|
| ![Classic](assets/dashboard-classic.png) | ![Minimal](assets/dashboard-minimal.png) | ![Neon](assets/dashboard-neon.png) |

<a id="safety"></a>
## ⚠️ Seguridad

FTP no está cifrado: úsalo solo en una red local de confianza. Guarda copias antes de modificar las bases de datos de PS5. Para iniciar payloads se requiere un entorno homebrew compatible con elfldr.

<a id="credits"></a>
## ❤️ Créditos y aviso

Desarrollado por **MrGee con ayuda de IA**. Gracias a los colaboradores de zftpd, ftpsrv, ispc_texcomp, Pillow, TkinterDnD, Tk/Tcl, Python y Nuitka. Los componentes de terceros conservan sus licencias. Proyecto independiente, sin afiliación con Sony Interactive Entertainment.

Más información: [CHANGELOG.md](CHANGELOG.md) · [CREDITS.md](CREDITS.md) · [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) · [LICENSE](LICENSE)
