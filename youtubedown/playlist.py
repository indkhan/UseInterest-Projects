
import pytube
import sys
import os

# get playlist url
try:
    playaudvid = sys.argv[1]
except:
    playaudvid = input("enter aud or vid :   ")
try:
    playlist_url = sys.argv[2]
except:
    playlist_url = input("enter url :   ")

try:
    res = sys.argv[3]
except:
    res = input("enter resolution :  ")


p = pytube.Playlist(playlist_url)

print(f'Downloading: {p.title}')
for url in p.video_urls:
    try:
        yt = pytube.YouTube(url)
        title = yt.title.split()
        if playaudvid == "vid":
                
            if not os.path.exists(rf"C:\Users\mgsuk\Videos\Youtube\{p.title}"):
                os.makedirs(rf"C:\Users\mgsuk\Videos\Youtube\{p.title}")
            stream = yt.streams.filter(res=res, progressive=True).first()

            out = rf"C:\Users\mgsuk\Videos\Youtube\{p.title}"

            stream.download(output_path=out, filename=f"{title[0]}.mp4")
            print(f"downloaded {title[0]}")

        elif playaudvid == "aud":
            if not os.path.exists(rf"C:\Users\mgsuk\Music\{p.title}"):
                os.makedirs(rf"C:\Users\mgsuk\Music\{p.title}")
            stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

            out = rf"C:\Users\mgsuk\Music\{p.title}"
            
            stream.download(output_path=out, filename=f"{title[0]}.mp3")

        print(f"downloaded {title[0]}")

    except Exception as e:
        print(f'Error Downloading: {url}')
  