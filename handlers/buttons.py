from telegram import Update
from telegram.ext import ContextTypes
from downloader import download_audio, download_video
from database import save_download

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data  # misol: audio|link yoki video|link
    action, value = data.split("|")

    user_id = query.from_user.id

    try:
        if action == "audio":
            file_path = await download_audio(value)
            await query.message.reply_audio(
                audio=open(file_path, 'rb'),
                title="Your Audio"
            )
            await save_download(user_id, "audio")

        elif action == "video":
            file_path = await download_video(value)
            await query.message.reply_video(
                video=open(file_path, 'rb'),
                caption="Your Video"
            )
            await save_download(user_id, "video")

    except Exception as e:
        await query.message.reply_text("❌ Xatolik yuz berdi")
        print(e)
