from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from utils.filters import is_url, detect_platform
from downloader import download_audio, download_video
from database import add_user, save_history, save_download


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id

    await add_user(user_id)
    await save_history(user_id, text)

    # LINK BO‘LSA
    if is_url(text):
        platform = detect_platform(text)

        keyboard = [[
            InlineKeyboardButton("🎧 Audio", callback_data=f"audio|{text}"),
            InlineKeyboardButton("🎥 Video", callback_data=f"video|{text}")
        ]]

        await update.message.reply_text(
            f"🔗 Link aniqlandi ({platform})\nVariant tanlang:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    # TEXT BO‘LSA (SEARCH)
    await update.message.reply_text("🔍 Qidiryapman...")

    try:
        query = f"ytsearch1:{text}"

        file_path = await download_audio(query)

        await update.message.reply_audio(
            audio=open(file_path, 'rb'),
            title=text
        )

        await save_download(user_id, "audio")

    except Exception as e:
        await update.message.reply_text("❌ Xatolik yuz berdi")
        print(e)
