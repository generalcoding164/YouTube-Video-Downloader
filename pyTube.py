# At first, install these modules

from pytube import *#for dowloading
from pyttsx3 import *#for the voice

# make a func to download the video
def Download(link: str):
    # formality
    speak("Thanks for using me! Your video is being downloaded.")
    
    # get the object
    youtubeVideo=YouTube(link)
    # make sure to get the highest resolution
    youtubeVideo=youtubeVideo.streams.get_highest_resolution()
    # download
    youtubeVideo.download()

    # formality
    print("Download completed successfully !")
    speak("Download completed successfully !")
    print("PLease check the folder where this Python file is located")
    speak("PLease check the folder where this Python file is located")

# take the link as input
link=input("Enter your link : ")

# trigger the func you made earlier
Download(link)