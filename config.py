import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost")

DB_NAME = "bot.db"
