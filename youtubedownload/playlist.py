import re
import pytube
import sys
import os

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

def clean_youtube_title(title):
    # Remove leading/trailing whitespace
    #title = title.strip()

    # Replace multiple spaces with a single underscore
    title = re.sub(r'\s+', '_', title)

    # Remove invalid characters for filenames
    title = re.sub(r'[^a-zA-Z0-9_\-\.]', '', title)

    return title

p = pytube.Playlist(playlist_url)

print(f"Downloading: {p.title}")
for url in p.video_urls:
    try:
        yt = pytube.YouTube(url)
        title = yt.title.split()
        title_str = ''.join(title)
        cleantitle = clean_youtube_title(title_str)
        if playaudvid == "vid":

            if not os.path.exists(rf"C:\Users\mgsuk\Videos\Youtube"):
                os.makedirs(rf"C:\Users\mgsuk\Videos\Youtube")

            stream = yt.streams.filter(res=res, progressive=True).first()

            out = rf"C:\Users\mgsuk\Videos\Youtube"

            print(f"downloading {cleantitle}")
            stream.download(output_path=out, filename=f"{cleantitle}.mp4")

        elif playaudvid == "aud":
            if not os.path.exists(rf"C:\Users\mgsuk\Music"):
                os.makedirs(rf"C:\Users\mgsuk\Music")

            stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()

            out = rf"C:\Users\mgsuk\Music"

            print(f"downloading {cleantitle}")
            stream.download(output_path=out, filename=f"{cleantitle}.mp3")

        print(f"downloaded {cleantitle}")

    except Exception as e:
        print(f"Error Downloading: {url}")
        print(e)
