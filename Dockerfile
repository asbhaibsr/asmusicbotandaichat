# Base Image
FROM python:3.10-slim

# Set environment
ENV TZ=Asia/Kolkata
ENV PIP_NO_CACHE_DIR=1

# Working directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    && apt-get clean

# Copy all files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port (Koyeb default)
EXPOSE 8080

# Start the bot
CMD ["python3", "bot.py"]
