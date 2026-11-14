# Baixar VIDEO E MP3

App de desktop simples (Python + Tkinter + yt-dlp) para baixar o áudio em **MP3** ou o **vídeo em MP4** de um link do YouTube.

![Demonstração](demo.gif)

## Como usar (sem instalar Python)

1. Baixe o app na página de [Releases](../../releases).
2. Instale o FFmpeg: `brew install ffmpeg`
3. Abra o app, cole o link e clique em **MP3** ou **Vídeo**.

No macOS, se aparecer o aviso de desenvolvedor não identificado, vá em
**Ajustes do Sistema > Privacidade e Segurança > Abrir Mesmo Assim**.

Os arquivos são salvos na pasta **Downloads**.

## Rodando pelo código

Requisitos: Python 3.10+ e FFmpeg.

```
pip3 install -r requirements.txt
python3 main.py
```

## Gerando o app

```
pip3 install pyinstaller
pyinstaller --windowed --name "MediaDownloader" main.py
```

O resultado fica na pasta `dist/`.

## Aviso

Projeto para uso pessoal e estudo. Baixar conteúdo do YouTube pode violar os
termos do serviço e direitos autorais. Use apenas com conteúdo que você tem
permissão para baixar.
