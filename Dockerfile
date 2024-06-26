FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV API_TOKEN your_telegram_bot_token

CMD ["python", "bot.py"]

