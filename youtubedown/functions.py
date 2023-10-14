import pytube
import sys
import string



def viddown(url , path):
    yt = pytube.YouTube(url)
    title = yt.title.split()
    vidna = "".join(title[0:4])
    special = string.punctuation

    vidname = vidna.translate(str.maketrans('', '', special))

    
    streamres = yt.streams.filter(progressive=True)
    reslist = []
    for i in streamres:
        reslist.append(i.resolution)
        
    try:
        res = sys.argv[3]
    except:
        res = input(f"enter res between {reslist}:   ")
    stream = yt.streams.filter(res=res, progressive=True).first()
    out = path
    # download video
    try:
        stream.download(output_path=out, filename=f"{vidname}.mp4")
        print("done")

    except Exception as err:
        print(err)
        print("error")
    


def auddown(url , path):
    yt = pytube.YouTube(url)
    title = yt.title.split()
    vidna = "".join(title[0:4])
    special = string.punctuation

    vidname = vidna.translate(str.maketrans('', '', special))
    print(vidname)
    stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    out = path
    # download video
    try:
        stream.download(output_path=out, filename=f"{vidname}.mp3")
        print("done")
    except:
        print("error")