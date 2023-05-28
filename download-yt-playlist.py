import pytube
import os
from datetime import date

# Get the YouTube playlist URL from the user
playlist_url = input("Enter the YouTube playlist URL: ")

# Create a Playlist object
playlist = pytube.Playlist(playlist_url)

# Create a folder for the playlist using the channel name, playlist name, and current date
yt = pytube.YouTube(playlist_url)
channel_name = yt.author
playlist_name = playlist.title
today = date.today().strftime("%Y-%m-%d")
folder_name = f"{channel_name}-{playlist_name}-{today}"
os.makedirs(folder_name, exist_ok=True)

# Print the playlist title
print("Playlist Title:", playlist_name)

# Iterate through each video in the playlist
for video_url in playlist.video_urls:
    try:
        # Create a YouTube object for the video
        yt = pytube.YouTube(video_url)

        # Get the audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio stream
        audio_file = audio_stream.download()

        # Get the title of the video
        title = yt.title

        # Change the extension of the file to .mp3
        new_file_name = title + ".mp3"

        # Move the file to the playlist folder
        new_file_path = os.path.join(folder_name, new_file_name)
        os.rename(audio_file, new_file_path)

        print("Downloaded:", title)
    except Exception as e:
        print("Failed to download:", video_url)
        print("Error:", str(e))

print("Playlist download completed. Files saved in:", folder_name)
