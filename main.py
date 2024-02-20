import yt_dlp

url = input("Link do Vídeo: ")

ytdown_opts = {}

with yt_dlp.YoutubeDL(ytdown_opts) as ytdown:
    ytdown.download([url])

print("Download concluído!")
