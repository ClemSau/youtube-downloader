from __future__ import unicode_literals
import youtube_dl
import os 
import time

print("Initialisation...\n")

VIDEO_URL = input("\nPlease, past the link of the video : \n")

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([VIDEO_URL])

print("Download complete")
time.sleep(3)