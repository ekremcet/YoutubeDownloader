import os
import subprocess
from pytube import YouTube


def main(link, audio_only=False):
    os.makedirs("./download/", exist_ok = True)
    path = "./download/"
    yt = YouTube(link)
    if audio_only:
        audio = yt.streams.filter(only_audio=True)[0]
        audio.download(path)
        file_name = audio.default_filename
        mp3_name = file_name[:-4] + ".mp3"
        # convert to mp3
        subprocess.run(["ffmpeg", "-i", os.path.join(path, file_name), os.path.join(path, mp3_name)])
        # remove the video file
        os.remove(os.path.join(path, file_name))
    else:
        yt.streams.get_highest_resolution().download(path)


if __name__ == '__main__':
    main("https://www.youtube.com/watch?v=QfRU-1T8q4g&",  audio_only=True)
