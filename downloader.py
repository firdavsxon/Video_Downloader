from pytube import YouTube
from bs4 import BeautifulSoup
import requests
from pytube import Playlist

def scrap_info(url):
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    title = s.find('title').text.strip('- YouTube')
    # views = s.find("div", class_="watch-view-count").text
    # likes = s.find("span", class_="like-button-renderer").span.button.text
    data = {'title': title}
    return title

def download_audio_from_user_input():
    url = input("Enter your url to download: ")
    yt = YouTube(url)
    print(yt.streams.filter(only_audio=True))
    user_input = input("Choose itag number to download: ")
    dw = yt.streams.filter(only_audio=True).get_by_itag(user_input)
    print("Downloading ..")
    dw.download('/Users/akilov/Desktop/mp3/Pytube_Download')
    print("Done!")

def download_video_from_user_input():
    url = input("Enter your YouTube video link to download video: ")
    yt = YouTube(url)
    print(yt.streams)
    user_input = int(input("Choose resolution number to download: "))
    dw = yt.streams.get_by_itag(user_input)
    print("Downloading ..")
    dw.download('/Users/akilov/Desktop/mp3/Pytube_Download')
    print("Done!")

def download_from_list():
    video_list = ['https://youtu.be/5wyW-w1ikK0?list=PLjzeyhEA84sS6ogo2mXWdcTrL2HRfJUv8',
                  'https://youtu.be/2zToEPpFEN8?list=PLjzeyhEA84sS6ogo2mXWdcTrL2HRfJUv8']
    user = int(input("1. Audio\n2. Video\n Choose: "))

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

# def download_playlist():
#     pl_list = input("Enter playlist url: ")
#     playlist = Playlist(pl_list)
#     # pl.download_all()
#     # or if you want to download in a specific directory
#     print(playlist)
#     print(playlist.video_urls)
#     # pl.download_all()

# download_audio_from_user_input()
# download_video_from_user_input()
download_from_list()
# download_playlist()