import aiosqlite
from config import DB_NAME

# DB yaratish
async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS history (
            user_id INTEGER,
            query TEXT
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS downloads (
            user_id INTEGER,
            file_type TEXT
        )
        """)

        await db.commit()

# user qo‘shish
async def add_user(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id) VALUES (?)",
            (user_id,)
        )
        await db.commit()

# qidiruv saqlash
async def save_history(user_id, query):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO history (user_id, query) VALUES (?, ?)",
            (user_id, query)
        )
        await db.commit()

# download stat
async def save_download(user_id, file_type):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO downloads (user_id, file_type) VALUES (?, ?)",
            (user_id, file_type)
        )
        await db.commit()

# userlar soni
async def get_users_count():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT COUNT(*) FROM users") as cursor:
            result = await cursor.fetchone()
            return result[0]

# barcha userlar (broadcast uchun)
async def get_all_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT user_id FROM users") as cursor:
            return [row[0] async for row in cursor]
