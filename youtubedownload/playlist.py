import pytube
import sys
import os
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time as a string
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
# get playlist url
try:
    playaudvid = sys.argv[1]
except:
    playaudvid = input("enter aud or vid :   ")

if playaudvid == "vid":
    try:
        res = sys.argv[3]
    except:
        res = input("enter resolution :  ")
try:
    playlist_url = sys.argv[2]
except:
    playlist_url = input("enter url :   ")


p = pytube.Playlist(playlist_url)

print(f"Downloading: {p.title}")
for url in p.video_urls:
    try:
        yt = pytube.YouTube(url)
        title = yt.title.split()
        if playaudvid == "vid":

            if not os.path.exists(rf"C:\Users\mgsuk\Videos\Youtube"):
                os.makedirs(rf"C:\Users\mgsuk\Videos\Youtube")

            stream = yt.streams.filter(res=res, progressive=True).first()

            out = rf"C:\Users\mgsuk\Videos\Youtube"

            stream.download(output_path=out, filename=f"{title[2]}{timestamp}.mp4")
            print(f"downloaded {title[2]}")

        elif playaudvid == "aud":
            if not os.path.exists(rf"C:\Users\mgsuk\Music"):
                os.makedirs(rf"C:\Users\mgsuk\Music")
            stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()

            out = rf"C:\Users\mgsuk\Music"

            stream.download(output_path=out, filename=f"{title[2].replace(",", "")}{timestamp}.mp3")

        print(f"downloaded {title[0]}")

    except Exception as e:
        print(f"Error Downloading: {url}")
        print(e)
