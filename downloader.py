import yt_dlp
import asyncio
import os
from utils.cache import get_cache, set_cache


# AUDIO yuklash (MP3)
async def download_audio(query: str):
    cached = await get_cache(query)
    if cached and os.path.exists(cached):
        return cached

    filename = f"audio_{abs(hash(query))}"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{filename}.%(ext)s',
        'quiet': True,
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    loop = asyncio.get_event_loop()
    await loop.run_in_executor(
        None,
        lambda: yt_dlp.YoutubeDL(ydl_opts).download([query])
    )

    file_path = f"{filename}.mp3"

    await set_cache(query, file_path)

    return file_path


# VIDEO yuklash
async def download_video(url: str):
    filename = f"video_{abs(hash(url))}"

    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{filename}.%(ext)s',
        'quiet': True
    }

    loop = asyncio.get_event_loop()
    await loop.run_in_executor(
        None,
        lambda: yt_dlp.YoutubeDL(ydl_opts).download([url])
    )

    file_path = f"{filename}.mp4"

    return file_path
