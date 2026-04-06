import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from config import BOT_TOKEN
from database import init_db
from utils.cache import init_redis

# Handlers
from handlers.start import start
from handlers.message import handle_message
from handlers.buttons import button_handler

async def main():
    # DB va Redis init
    await init_db()
    await init_redis()

    # Bot ishga tushurish
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Inline buttons
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🚀 Bot ishga tushdi...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
