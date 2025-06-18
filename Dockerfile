FROM python:3.10

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y ffmpeg gcc libffi-dev libssl-dev python3-dev build-essential && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python3", "bot.py"]
