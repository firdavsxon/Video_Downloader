from pytube import YouTube
from lxml import etree

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
            print("Downloading ....")
            dw.download('/Users/akilov/Desktop/mp3/Pytube_Download')
            print("Done!")
    elif user == 2:
        for i in video_list:
            yt = YouTube(i)
            print("Downloading....")
            yt.streams.first().download('/Users/akilov/Desktop/mp3/Pytube_Download')
            print("Done!")
    return

# download_audio_from_user_input()
# download_video_from_user_input()
download_from_list()