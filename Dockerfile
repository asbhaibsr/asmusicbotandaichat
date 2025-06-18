# Base image with Python 3.10
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies + tzdata for time sync fix
RUN apt-get update && \
    apt-get install -y ffmpeg git gcc libffi-dev libssl-dev python3-dev build-essential tzdata && \
    apt-get clean

# Set timezone to match Telegram server
ENV TZ=Asia/Kolkata

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Start the bot
CMD ["python3", "main.py"]
