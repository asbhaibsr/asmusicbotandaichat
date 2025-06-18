# Base image with Python 3.10
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies + tzdata for Telegram time sync
RUN apt-get update && \
    apt-get install -y ffmpeg git gcc libffi-dev libssl-dev python3-dev build-essential tzdata && \
    apt-get clean

# Set Timezone to Asia/Kolkata to fix Telegram BadMsgNotification error
ENV TZ=Asia/Kolkata

# Copy all files to container
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run the bot
CMD ["python3", "bot.py"]
