import pytube
import sys
import string
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time as a string
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

def viddown(url, path="", res="720p"):
    yt = pytube.YouTube(url)
    title = yt.title.split()
    vidna = "".join(title[0:4])
    special = string.punctuation

    vidname = vidna.translate(str.maketrans('', '', special))

    streamres = yt.streams.filter(progressive=True)
    reslist = []
    for i in streamres:
        reslist.append(i.resolution)

    # try:
    #    res = sys.argv[3]
    # except:
    #    res = input(f"enter res between {reslist}:   ")
    stream = yt.streams.filter(res=res, progressive=True).first()

    # download video
    try:
        if path != "":
            out = path
            stream.download(output_path=out, filename=f"{vidname}{timestamp}.mp4")
            print("done")
        else:
            stream.download(filename=f"{vidname}{timestamp}.mp4")
            print("done")

    except Exception as err:
        print(err)
        print("error")


def auddown(url, path=""):
    yt = pytube.YouTube(url)
    title = yt.title.split()
    vidna = "".join(title[0:4])
    special = string.punctuation

    vidname = vidna.translate(str.maketrans('', '', special))
    print(vidname)
    stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    # download video
    try:
        if path != "":
            out = path
            stream.download(output_path=out, filename=f"{vidname}{timestamp}.mp3")
            print("done")
        else:
            stream.download(filename=f"{vidname}{timestamp}.mp3")
            print("done")
    except:
        print("error")
