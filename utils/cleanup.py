import os
import asyncio

async def cleanup_files(folder="."):
    for file in os.listdir(folder):
        if file.endswith((".mp3", ".mp4")):
            try:
                os.remove(os.path.join(folder, file))
            except:
                pass

# Async loop bilan har 10 daqiqada ishga tushirish mumkin
# asyncio.create_task(periodic_cleanup())
