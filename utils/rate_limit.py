import time
from collections import defaultdict

user_last = defaultdict(lambda: 0)
COOLDOWN = 3  # sekund

def check_rate(user_id):
    now = time.time()
    if now - user_last[user_id] < COOLDOWN:
        return False
    user_last[user_id] = now
    return True
