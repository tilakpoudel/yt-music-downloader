# yt-music-downloader

It contains the code to download youtube music including playlist in mp3 format with pytube library

`downloader.py` has the combined logic for mp3 and mp4 with support for download from single music url or playlist

## How to use:
- Go to project directory
- Checkout to `main` branch.
- Execute the script with command :

    ```python3 downloader.py```

- Enter the youtube video / playlist url:
- Choose the format (1= Video , 2=mp3)
- The files will be stored in the project's directory with the playlist name as the folder name {channel_name}-{playlist_name}-{today}