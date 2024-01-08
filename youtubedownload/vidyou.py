from pytube import YouTube
import sys
import functions


try:
    va = sys.argv[1]
except:
    va = input("enter aud or vid :   ")
if va == "vid":
    try:
        res = sys.argv[3]
    except:
        res = input("enter resolution :  ")
try:
    url = sys.argv[2]
except:
    url = input("enter url :   ")

pathvid = r"C:\Users\mgsuk\Videos\Youtube"
pathaud = r"C:\Users\mgsuk\Music"

if va == "vid":
    functions.viddown(url, pathvid, res)
elif va == "aud":
    functions.auddown(url, pathaud)


else:
    print("choose vid or aud")
