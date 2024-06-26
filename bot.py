import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.orm import Session
from database import engine, User, SessionLocal
import requests
from bs4 import BeautifulSoup

API_TOKEN = '6990284778:AAE1jrcbF5shViJl2EZ6p4Hy0fOhK6ORBJw'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

logging.basicConfig(level=logging.INFO)


@router.message(Command('start'))
async def send_welcome(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username

    session = SessionLocal()
    user = session.query(User).filter(User.user_id == user_id).first()
    if not user:
        user = User(user_id=user_id, username=username)
        session.add(user)
        session.commit()
    session.close()

    await message.answer("Welcome! Use /news to get the latest news.")


@router.message(Command('news'))
async def fetch_news(message: Message):
    url = "https://kun.uz/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = soup.find_all('div', class_='news-title')[:4]
    news_links = [item.find('a')['href'] for item in news_items]
    news_titles = [item.text.strip() for item in news_items]

    news = ""
    for title, link in zip(news_titles, news_links):
        news += f"{title}\n{link}\n\n"

    await message.answer(news)


def main():
    dp.include_router(router)
    dp.start_polling(bot)


if __name__ == '__main__':
    from celery_app import fetch_jsonplaceholder_data

    fetch_jsonplaceholder_data.delay()
    main()

