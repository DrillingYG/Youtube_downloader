import logging
from pytube import YouTube

def ytpytubeStreamObject(yt):
    ytStream=yt.streams
    cnt=0
    for stream in ytStream:
        print(stream)
        if not stream.is_adaptive :

            cnt+=1
    print(cnt)
if __name__ == '__main__':
    path = "C:\\users\\cg398\\Desktop"
    yt = YouTube("https://www.youtube.com/watch?v=IKfkSHpkBpw&feature=youtu.be")
