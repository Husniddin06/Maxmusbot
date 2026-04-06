import re

# URL aniqlash
def is_url(text: str) -> bool:
    return re.match(r'https?://', text) is not None


# Platform aniqlash
def detect_platform(url: str) -> str:
    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"
    elif "instagram.com" in url:
        return "instagram"
    elif "tiktok.com" in url:
        return "tiktok"
    elif "vk.com" in url:
        return "vk"
    else:
        return "unknown"
