<div align="center">

# 🎮 Y2JB Theme Creator 3.0

**Create · Customize · Upload**

![Version](https://img.shields.io/badge/version-3.0-blue) ![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6) ![Portable](https://img.shields.io/badge/build-portable-success) ![BC7](https://img.shields.io/badge/encoder-BC7-purple)

**Développé par MrGee avec assistance IA**

[🇩🇪 Deutsch](README.de.md) · [🇬🇧 English](README.md) · [🇪🇸 Español](README.es.md) · **🇫🇷 Français** · [🇵🇹 Português](README.pt.md)

[**Téléchargement / Releases**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/releases) · [**Changelog**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/blob/main/CHANGELOG.md) · [**Credits**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/blob/main/CREDITS.md)

</div>

---

## ✨ Créez vos propres thèmes Y2JB

Transformez vos images PNG en fichiers de thèmes Y2JB, personnalisez icônes et fonds 4K, puis envoyez-les vers une PS5 compatible. Utilitaire homebrew Windows indépendant.

[Fonctionnalités](#features) · [Démarrage rapide](#quick-start) · [Formats des images](#image-specifications) · [Payloads FTP et prérequis](#ftp-payloads) · [Performances BC7 — mesures](#bc7-benchmarks) · [Trois interfaces](#screenshots) · [Sécurité](#safety) · [Crédits et avertissement](#credits)

<a id="features"></a>
## 🚀 Fonctionnalités

| | |
|---|---|
| 🎨 | Convertir des images PNG en fichiers de thèmes Y2JB |
| 🖼️ | Fonds 4K (3840 × 2160) et icônes 512 × 512 |
| ⚡ | Encodage BC7 DDS natif et parallèle : Fast et Balanced |
| 📡 | Gestion FTP : zftpd inclus et démarrage officiel de ftpsrv |
| 🔍 | Diagnostic FTP, détection du dossier cible et progression |
| 🛡️ | Sauvegarde, restauration et vérification SHA-256 |
| ✏️ | Modifier les noms des applications Y2JB avec sauvegarde des bases |
| 🎭 | Trois styles : Classic, Minimal et Neon |
| 🌍 | Allemand, anglais, espagnol, français et portugais |

<a id="quick-start"></a>
## 🛠️ Démarrage rapide

1. Téléchargez et décompressez la version portable Windows, puis lancez `Y2JBThemeCreator.exe`.
2. Saisissez l’adresse IP de la PS5. Démarrez zftpd inclus via elfldr ou ftpsrv officiel depuis l’application ; un serveur FTP déjà actif convient aussi.
3. Choisissez vos PNG depuis **n’importe quel dossier de votre PC**.
4. Créez les fichiers de thème Y2JB et transférez-les éventuellement par FTP.

<a id="image-specifications"></a>
## 🖼️ Formats des images

| Fichier | Utilisation | Resolution |
|---|---|---|
| `icon0.png` | Icône du thème | 512 × 512 |
| `pic0.png` | Fond 1 | 3840 × 2160 |
| `pic1.png` | Fond 2 | 3840 × 2160 |
| `pic2.png` | Fond 3 | 3840 × 2160 |

L’application redimensionne automatiquement les images. Une image peut être réutilisée pour plusieurs fonds.

<a id="ftp-payloads"></a>
## 📡 Payloads FTP et prérequis

**zftpd v1.7.0 est inclus** et peut être démarré via un service elfldr accessible. **ftpsrv n’est pas inclus :** avec la fonction intégrée, **la PS5 récupère directement le fichier ELF officiel depuis GitHub** et le démarre via elfldr. La PS5 doit avoir accès à Internet. Un Payload Manager compatible peut aussi lancer ftpsrv. L’application vérifie ensuite le FTP.

- [Official ftpsrv repository](https://github.com/ps5-payload-dev/ftpsrv)
- [Official ftpsrv ELF release](https://github.com/ps5-payload-dev/ftpsrv/releases/latest/download/ftpsrv-ps5.elf)
- zftpd v1.7.0: bundled in the Windows build, with its third-party license.

<a id="bc7-benchmarks"></a>
## ⚡ Performances BC7 — mesures

Essai sur des images réelles et un PC de test. Fast était environ **8,7 fois plus rapide pour l’icône** et **24 % plus rapide pour le fond 4K** que l’ancien encodeur, avec un PSNR supérieur pour les deux images. Les résultats peuvent varier.

### Icône — 512 × 512

| Encodeur | Durée | Qualité (PSNR) |
|---|---:|---:|
| **Y2JB Fast** | **0,026** s | 35,43 dB |
| Y2JB Balanced | 0,057 s | **36,96** dB |
| Ancien encodeur | 0,225 s | 33,78 dB |

### Fond — 3840 × 2160

| Encodeur | Durée | Qualité (PSNR) |
|---|---:|---:|
| **Y2JB Fast** | **0,677** s | 45,73 dB |
| Y2JB Balanced | 1,349 s | **46,11** dB |
| Ancien encodeur | 0,896 s | 44,51 dB |

![BC7 benchmark comparison](assets/bc7-benchmark.svg)

> Test results are specific to the measured images and hardware. PSNR is a metric, not a universal visual-quality guarantee.

<a id="screenshots"></a>
## 🎭 Trois interfaces

| Classic | Minimal | Neon |
|---|---|---|
| ![Classic](assets/dashboard-classic.png) | ![Minimal](assets/dashboard-minimal.png) | ![Neon](assets/dashboard-neon.png) |

<a id="safety"></a>
## ⚠️ Sécurité

FTP n’est pas chiffré : utilisez-le uniquement sur un réseau local fiable. Sauvegardez les bases de données PS5 avant modification. Un environnement homebrew compatible avec elfldr est nécessaire au lancement des payloads.

<a id="credits"></a>
## ❤️ Crédits et avertissement

Développé par **MrGee avec assistance IA**. Merci aux contributeurs de zftpd, ftpsrv, ispc_texcomp, Pillow, TkinterDnD, Tk/Tcl, Python et Nuitka. Les licences des composants tiers restent applicables. Projet indépendant sans affiliation à Sony Interactive Entertainment.

En savoir plus: [CHANGELOG.md](CHANGELOG.md) · [CREDITS.md](CREDITS.md) · [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) · [LICENSE](LICENSE)
