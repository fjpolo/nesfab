import yt_dlp

ydl_opts = {
    'format': 'best[ext=mp4]/best',
    'outtmpl': 'assets/original_cinematic.mp4',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=BOkrmItaBic'])
    print("Download successful!")
except Exception as e:
    print("Error during download:", e)
