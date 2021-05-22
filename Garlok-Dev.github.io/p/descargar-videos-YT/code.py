from pytube import YouTube

#Aquí preguntamos la URL del video
yt = YouTube(input("Inserta aquí la URL, porfi :) = "))

#Descargando video...
print("Descargando ' " + yt.title + " '...")
stream = yt.streams.first()
stream.download()
print("")
print("Listo ya puedes disfrutar de tu video, hasta la proxima :)")

#El video se descargara en la misma ubucacion donde se ubique el archivo code.py