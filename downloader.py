import pytube
import os
from datetime import date

# Get the YouTube video or playlist URL from the user
url = input("Enter the YouTube URL: ")

isPlaylist = "playlist?" in url

# Check if the URL is for a playlist and download
if isPlaylist:
    # Create a Playlist object
    playlist = pytube.Playlist(url)

    # Create a folder for the playlist using the channel name, playlist name, and current date
    channel_name = playlist.owner.split()[0] if playlist.owner else ""
    playlist_name = playlist.title
    today = date.today().strftime("%Y-%m-%d")
    folder_name = f"{channel_name}-{playlist_name}-{today}"
    os.makedirs(folder_name, exist_ok=True)

    # Print the playlist title
    print("Playlist Title:", playlist_name)

    # Prompt the user to choose the format for downloading
    format_choice = input("Choose the format (1 - MP4, 2 - MP3): ")

    # Iterate through each video in the playlist
    for video in playlist.videos:
        try:
            # Get the selected format stream
            if format_choice == '1':
                # Get the video stream
                stream = video.streams.get_highest_resolution()
            elif format_choice == '2':
                # Get the audio stream
                stream = video.streams.filter(only_audio=True).first()
            else:
                print("Invalid format choice. Skipping video:", video.title)
                continue

            # Download the stream
            file_path = stream.download(output_path=folder_name)

            # Get the title of the video
            title = video.title

            # Change the file extension based on the format choice
            if format_choice == '1':
                new_file_name = title + ".mp4"
            else:
                new_file_name = title + ".mp3"

            # Rename the file
            new_file_path = os.path.join(folder_name, new_file_name)
            os.rename(file_path, new_file_path)

            print("Downloaded:", title)
        except Exception as e:
            print("Failed to download:", video.title)
            print("Error:", str(e))

    print("Playlist download completed. Files saved in:", folder_name)
else:
    try:
        # Create a YouTube object
        yt = pytube.YouTube(url)

        # Prompt the user to choose the format for downloading
        format_choice = input("Choose the format (1 - MP4, 2 - MP3): ")

        # Get the selected format stream
        if format_choice == '1':
            # Get the video stream
            stream = yt.streams.get_highest_resolution()
        elif format_choice == '2':
            # Get the audio stream
            stream = yt.streams.filter(only_audio=True).first()
        else:
            print("Invalid format choice. Exiting...")
            exit()

        # Download the stream
        file_path = stream.download()

        # Get the title of the video
        title = yt.title

        # Create a folder using the channel name and current date
        channel_name = yt.author
        today = date.today().strftime("%Y-%m-%d")
        folder_name = f"{channel_name}-{today}"
        os.makedirs(folder_name, exist_ok=True)

        # Change the file extension based on the format choice
        if format_choice == '1':
            new_file_name = title + ".mp4"
        else:
            new_file_name = title + ".mp3"

        # Move the file to the channel folder
        new_file_path = os.path.join(folder_name, new_file_name)
        os.rename(file_path, new_file_path)

        print("Downloaded:", title)
        print("File saved in:", folder_name)
    except Exception as e:
        print("Failed to download the video.")
        print("Error:", str(e))
