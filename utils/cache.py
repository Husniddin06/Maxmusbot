import aioredis
from config import REDIS_URL

redis = None

# Redis ulanish
async def init_redis():
    global redis
    redis = await aioredis.from_url(REDIS_URL, decode_responses=True)


# Cache olish
async def get_cache(key: str):
    if redis:
        return await redis.get(key)
    return None


# Cache saqlash
async def set_cache(key: str, value: str, expire: int = 3600):
    if redis:
        await redis.set(key, value, ex=expire)
