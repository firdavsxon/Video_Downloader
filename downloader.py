from pytube import YouTube, Playlist
import os
import re
import requests
from bs4 import BeautifulSoup

def download_audio(url, destination):
    if 'http' not in url:
        url = 'https://www.youtube.com/watch?v=%s' % url
    yt = YouTube(url)
    dw = yt.streams.filter(only_audio=True).first()
    title = yt.title
    print(f"{title} downloading ...")
    try:
        dw.download(destination)
        print("Done!")
    except:
        print(f"Downloading {title} failed")

def download_audio_from_user_input():
    url = input("Enter your url to download: ")
    if 'http' not in url:
        url = 'https://www.youtube.com/watch?v=%s' % url
    yt = YouTube(url)
    dw = yt.streams.filter(only_audio=True).first()
    title = yt.title
    print(f"{title} downloading ...")
    dw.download('/Users/akilov/Desktop/mp3/Pytube_Download')
    print("Done!")

def download_video_from_user_input():
    url = input("Enter your YouTube video link to download video: ")
    if 'http' not in url:
        url = 'https://www.youtube.com/watch?v=%s' % url
    yt = YouTube(url)
    dw = yt.streams.first()
    title = yt.title
    print(f"{title} downloading ..")
    dw.download('/Users/akilov/Desktop/mp3/Pytube_Download')
    print("Done!")


def download_video(url, destination):
    if 'http' not in url:
        url = 'https://www.youtube.com/watch?v=%s' % url
    yt = YouTube(url)
    dw = yt.streams.first()
    title = yt.title
    print(f"{title} downloading ..")
    try:
        dw.download(destination)
        print("Done!")
    except:
        print(f"Downloading {title} failed")

def download_from_list():
    video_list = ['https://youtu.be/5wyW-w1ikK0?list=PLjzeyhEA84sS6ogo2mXWdcTrL2HRfJUv8',
                  'https://youtu.be/2zToEPpFEN8?list=PLjzeyhEA84sS6ogo2mXWdcTrL2HRfJUv8']
    user = int(input("Choose which format you want to download.\n"
                     "1. Audio\n2. Video\n Choose: "))

    if user == 1:
        for i in video_list:
            yt = YouTube(i)
            dw = yt.streams.filter(only_audio=True).first()
            title = yt.title
            dw.download('/Users/akilov/Desktop/mp3/Pytube_Download')
            print(f" Audio - {title}  ..... Downloaded")
    elif user == 2:
        for i in video_list:
            yt = YouTube(i)
            title = yt.title
            yt.streams.first().download('/Users/akilov/Desktop/mp3/Pytube_Download')
            print(f" Video with views - {title}  .....Downloaded")
    return

def download_playlist():
    pl_list = input("Enter playlist url: ")
    playlist = Playlist(pl_list)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    page = requests.get(pl_list)
    soup = BeautifulSoup(page.content, 'html.parser')
    playlist_name = soup.find('title').text.strip(' - YouTube')
    MYDIR = (f"/Users/akilov/Desktop/mp3/Pytube_Download/{playlist_name}")
    CHECK_FOLDER = os.path.isdir(MYDIR)
    if not CHECK_FOLDER:
        os.makedirs(MYDIR)
        print("created folder : ", MYDIR)
    else:
        print(MYDIR, "folder already exists.")
    audio_or_video = int(input("Download video as\n 1. Audio\n 2. Video?\n"
                           "Please choose format: "))
    if audio_or_video == 1:
        for url in playlist:
            download_audio(url, MYDIR)
    elif audio_or_video == 2:
        for url in playlist:
            download_video(url, MYDIR)





# download_audio_from_user_input()
# download_video_from_user_input()
# download_from_list()
download_playlist()