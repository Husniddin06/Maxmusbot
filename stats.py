from database import get_users_count

async def bot_stats():
    total_users = await get_users_count()
    return f"📊 Bot foydalanuvchilari: {total_users}"
