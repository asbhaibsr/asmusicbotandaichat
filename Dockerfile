# Base image with Python 3.10
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies + tzdata(Optional) + build tools
RUN apt-get update && \
    apt-get install -y ffmpeg git gcc libffi-dev libssl-dev python3-dev build-essential tzdata && \
    apt-get clean

# Set timezone (optional, helps time-sync issues)
ENV TZ=Asia/Kolkata

# Copy all project files
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port 8080 for health check
EXPOSE 8080

# Start the bot
CMD ["python3", "main.py"]
