from telegram import Update
from telegram.ext import ContextTypes
from database import add_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    await add_user(user_id)

    text = (
        "🎧 Salom!\n\n"
        "Men kuchli media botman 🚀\n\n"
        "🔍 Qo‘shiq nomini yoz — topib beraman\n"
        "🔗 Yoki link yubor — yuklab beraman\n\n"
        "🔥 Buyruqlar:\n"
        "/start - qayta boshlash\n"
    )

    await update.message.reply_text(text)
