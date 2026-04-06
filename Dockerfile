# Python 3.11 image
FROM python:3.11-slim

# Ish papkasi
WORKDIR /app

# Requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App copy
COPY . .

# Redis oson ishlashi uchun
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Botni ishga tushirish
CMD ["python", "main.py"]
