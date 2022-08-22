import os
import shutil

from pytube import YouTube


def main(link, audio_only=False):
    os.makedirs("./download/", exist_ok = True)
    path = "./download/"
    yt = YouTube(link)
    if audio_only:
        audio = yt.streams.filter(only_audio=True)[0].download(path)
    else:
        video = yt.streams.get_highest_resolution().download(path)


if __name__ == '__main__':
    main("https://www.youtube.com/watch?v=fdGyoJXeWrI",  audio_only=True)