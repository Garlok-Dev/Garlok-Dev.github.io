from pytube import YouTube

#Here we ask for the URL
yt = YouTube(input("Insert here the URL, plz :) = "))

#Downloading video...
print("Downloading ' " + yt.title + " '...")
stream = yt.streams.first()
stream.download()
print("\n")
print("Ready now you can enjoy your video, until next time :)")

#The video is downloaded to the same location where the code.py file is located