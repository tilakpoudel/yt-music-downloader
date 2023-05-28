import pytube
import os

# Get the YouTube video URL from the user
video_url = input("Enter the YouTube video URL: ")

# Create a YouTube object
yt = pytube.YouTube(video_url)

# Get the audio stream
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio stream
audio_file = audio_stream.download()

# Get the title of the video
title = yt.title

# Change the extension of the file to .mp3
new_file_name = title + ".mp3"

# Rename the file
os.rename(audio_file, new_file_name)

# Print a success message
print("The audio file has been successfully downloaded.")
