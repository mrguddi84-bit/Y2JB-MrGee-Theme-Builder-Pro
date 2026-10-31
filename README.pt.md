<div align="center">

# 🎮 Y2JB Theme Creator 3.0

**Create · Customize · Upload**

![Version](https://img.shields.io/badge/version-3.0-blue) ![Windows](https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6) ![Portable](https://img.shields.io/badge/build-portable-success) ![BC7](https://img.shields.io/badge/encoder-BC7-purple)

**Desenvolvido por MrGee com assistência de IA**

[🇩🇪 Deutsch](README.de.md) · [🇬🇧 English](README.md) · [🇪🇸 Español](README.es.md) · [🇫🇷 Français](README.fr.md) · **🇵🇹 Português**

[**Descarregar / Releases**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/releases) · [**Changelog**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/blob/main/CHANGELOG.md) · [**Credits**](https://github.com/mrguddi84-bit/Y2JB-MrGee-Theme-Builder-Pro/blob/main/CREDITS.md)

</div>

---

## ✨ Crie os seus próprios temas Y2JB

Converta imagens PNG em ficheiros de temas Y2JB, personalize ícones e fundos 4K e envie-os para uma PS5 compatível. Ferramenta homebrew independente para Windows.

[Funcionalidades](#features) · [Início rápido](#quick-start) · [Especificações das imagens](#image-specifications) · [Payloads FTP e requisitos](#ftp-payloads) · [Desempenho BC7 — resultados medidos](#bc7-benchmarks) · [Três interfaces](#screenshots) · [Segurança](#safety) · [Créditos e aviso](#credits)

<a id="features"></a>
## 🚀 Funcionalidades

| | |
|---|---|
| 🎨 | Converter imagens PNG em ficheiros de temas Y2JB |
| 🖼️ | Fundos 4K (3840 × 2160) e ícones de 512 × 512 |
| ⚡ | Codificação BC7 DDS nativa e paralela: Fast e Balanced |
| 📡 | Gestão FTP: zftpd incluído e arranque oficial de ftpsrv |
| 🔍 | Diagnóstico FTP, localização do destino e progresso |
| 🛡️ | Cópias de segurança, restauro e verificação SHA-256 |
| ✏️ | Editar nomes de aplicações Y2JB com cópias das bases de dados |
| 🎭 | Três estilos: Classic, Minimal e Neon |
| 🌍 | Alemão, inglês, espanhol, francês e português |

<a id="quick-start"></a>
## 🛠️ Início rápido

1. Descarregue e extraia a versão portátil para Windows e execute `Y2JBThemeCreator.exe`.
2. Introduza o IP da PS5. Inicie o zftpd incluído via elfldr ou o ftpsrv oficial pela aplicação; também pode utilizar um servidor FTP já ativo.
3. Selecione imagens PNG de **qualquer pasta do computador**.
4. Crie os ficheiros de tema Y2JB e, se desejar, envie-os por FTP.

<a id="image-specifications"></a>
## 🖼️ Especificações das imagens

| Ficheiro | Utilização | Resolution |
|---|---|---|
| `icon0.png` | Ícone do tema | 512 × 512 |
| `pic0.png` | Fundo 1 | 3840 × 2160 |
| `pic1.png` | Fundo 2 | 3840 × 2160 |
| `pic2.png` | Fundo 3 | 3840 × 2160 |

A aplicação redimensiona automaticamente as imagens. Pode reutilizar a mesma imagem em vários fundos.

<a id="ftp-payloads"></a>
## 📡 Payloads FTP e requisitos

**zftpd v1.7.0 está incluído** e pode ser iniciado através de um serviço elfldr acessível. **ftpsrv não está incluído:** com a função integrada, **a PS5 descarrega o ELF oficial diretamente do GitHub** e inicia-o via elfldr. A PS5 precisa de Internet. Também pode iniciar ftpsrv num Payload Manager compatível. A aplicação verifica depois o FTP.

- [Official ftpsrv repository](https://github.com/ps5-payload-dev/ftpsrv)
- [Official ftpsrv ELF release](https://github.com/ps5-payload-dev/ftpsrv/releases/latest/download/ftpsrv-ps5.elf)
- zftpd v1.7.0: bundled in the Windows build, with its third-party license.

<a id="bc7-benchmarks"></a>
## ⚡ Desempenho BC7 — resultados medidos

Teste com imagens reais num PC. Fast foi aproximadamente **8,7 vezes mais rápido para o ícone** e **24% mais rápido para o fundo 4K** do que o codificador anterior, com PSNR superior em ambas as imagens. Os resultados podem variar.

### Ícone — 512 × 512

| Codificador | Tempo | Qualidade (PSNR) |
|---|---:|---:|
| **Y2JB Fast** | **0,026** s | 35,43 dB |
| Y2JB Balanced | 0,057 s | **36,96** dB |
| Codificador anterior | 0,225 s | 33,78 dB |

### Fundo — 3840 × 2160

| Codificador | Tempo | Qualidade (PSNR) |
|---|---:|---:|
| **Y2JB Fast** | **0,677** s | 45,73 dB |
| Y2JB Balanced | 1,349 s | **46,11** dB |
| Codificador anterior | 0,896 s | 44,51 dB |

![BC7 benchmark comparison](assets/bc7-benchmark.svg)

> Test results are specific to the measured images and hardware. PSNR is a metric, not a universal visual-quality guarantee.

<a id="screenshots"></a>
## 🎭 Três interfaces

| Classic | Minimal | Neon |
|---|---|---|
| ![Classic](assets/dashboard-classic.png) | ![Minimal](assets/dashboard-minimal.png) | ![Neon](assets/dashboard-neon.png) |

<a id="safety"></a>
## ⚠️ Segurança

FTP não é encriptado: utilize apenas numa rede local de confiança. Faça cópias das bases de dados PS5 antes de as alterar. É necessário um ambiente homebrew compatível com elfldr para iniciar payloads.

<a id="credits"></a>
## ❤️ Créditos e aviso

Desenvolvido por **MrGee com assistência de IA**. Obrigado aos contribuidores de zftpd, ftpsrv, ispc_texcomp, Pillow, TkinterDnD, Tk/Tcl, Python e Nuitka. Aplicam-se as licenças dos componentes de terceiros. Projeto independente, sem ligação à Sony Interactive Entertainment.

Mais informações: [CHANGELOG.md](CHANGELOG.md) · [CREDITS.md](CREDITS.md) · [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md) · [LICENSE](LICENSE)
