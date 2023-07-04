# this is a simple YouTube video downloader

from pytube import YouTube

link = input("please insert video url:")
yt = YouTube(link)


print(f"video title is: {yt.title}")
print(f"video view is: {yt.views}")

ref = input("\nDo you want to download this? (y or n)")

if ref == "y":
    yd = yt.streams.get_highest_resolution()
    yd.download("/Users/erfan/Desktop/tube-download1")
else:
    exit()
