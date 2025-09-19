import os
from pytubefix import YouTube

def getURL():
    input_url = input("Input YouTube URL: ")
    stripped_url = input_url.strip()
    return stripped_url

def converter(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    filepath = stream.download(output_path="output")
    print(f"Video downloaded to: {filepath}")
    return filepath

if __name__ == "__main__":
    url = getURL()
    converter(url)
        