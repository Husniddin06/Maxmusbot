from database import get_all_users
from telegram import Bot

async def send_broadcast(bot: Bot, message: str):
    users = await get_all_users()
    for user_id in users:
        try:
            await bot.send_message(chat_id=user_id, text=message)
        except:
            pass
