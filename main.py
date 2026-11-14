import threading
import tkinter as tk
from tkinter import messagebox

import os
os.environ["PATH"] += ":/opt/homebrew/bin:/usr/local/bin"
import yt_dlp


class Downloader:
    def __init__(self, pasta=os.path.expanduser("~/Downloads")):
        self.pasta = pasta

    def baixar_mp3(self, link):
        opcoes = {
            "format": "bestaudio/best",
            "outtmpl": f"{self.pasta}/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([link])

    def baixar_video(self, link):
        opcoes = {
            "format": "bv*[vcodec^=avc1]+ba[ext=m4a]/b[ext=mp4]",
            "outtmpl": f"{self.pasta}/%(title)s.%(ext)s",
            "merge_output_format": "mp4",
        }
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([link])


class App:
    def __init__(self, janela):
        self.downloader = Downloader()
        janela.title("Baixar do YouTube")
        janela.geometry("400x160")

        tk.Label(janela, text="Link do YouTube:").pack(pady=(15, 5))
        self.entrada = tk.Entry(janela, width=50)
        self.entrada.pack()

        frame = tk.Frame(janela)
        frame.pack(pady=10)
        self.botao_mp3 = tk.Button(
            frame, text="Baixar MP3",
            command=lambda: self.iniciar(self.downloader.baixar_mp3))
        self.botao_mp3.pack(side="left", padx=5)
        self.botao_video = tk.Button(
            frame, text="Baixar Vídeo",
            command=lambda: self.iniciar(self.downloader.baixar_video))
        self.botao_video.pack(side="left", padx=5)

        self.status = tk.Label(janela, text="")
        self.status.pack()

    def iniciar(self, acao):
        link = self.entrada.get().strip()
        if not link:
            messagebox.showwarning("Aviso", "Cole um link primeiro.")
            return
        self.mudar_botoes("disabled")
        self.status.config(text="Baixando...")
        threading.Thread(target=self.executar, args=(acao, link), daemon=True).start()

    def executar(self, acao, link):
        try:
            acao(link)
            self.status.config(text="Pronto! Salvo na pasta Downloads.")
        except Exception as erro:
            self.status.config(text="Erro ao baixar.")
            print(erro)
        finally:
            self.mudar_botoes("normal")

    def mudar_botoes(self, estado):
        self.botao_mp3.config(state=estado)
        self.botao_video.config(state=estado)


if __name__ == "__main__":
    janela = tk.Tk()
    App(janela)
    janela.mainloop()
