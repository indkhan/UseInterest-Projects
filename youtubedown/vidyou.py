from pytube import YouTube
import sys


try:
    va = sys.argv[1]
except:
    va = input("enter aud or vid :   ")
try:
    url = sys.argv[2]
except:
    url = input("enter url :   ")

try:
    res = sys.argv[3]
except:
    res = input("enter resolution :  ")

yt = YouTube(url)
title = yt.title.split()
print(title[0])
if va == "vid":
    stream = yt.streams.filter(res=res, progressive=True).first()

    out = r"C:\Users\mgsuk\Videos\Youtube"
    # download video
    stream.download(output_path=out, filename=f"{title[0]}.mp4")

    print("done")
elif va == "aud":
    stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    out = r"C:\Users\mgsuk\Music"
    # download video
    stream.download(output_path=out, filename=f"{title[0]}.mp3")

    print("done")
else:
    print("choose vid or aud")
