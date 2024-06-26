from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"
Base = declarative_base()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class User(Base):
    tablename = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)
    username = Column(String, index=True)


Base.metadata.create_all(bind=engine)



from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.orm import Session
from database import engine, User, SessionLocal
import requests
from bs4 import BeautifulSoup

API_TOKEN = '6990284778:AAE1jrcbF5shViJl2EZ6p4Hy0fOhK6ORBJw'

logging.basicConfig(level=logging.INFO)


# Start command handler
@router.message(Command('start'))
async def send_welcome(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username

    # Save user to the database
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


if name == 'main':
    from celery_app import fetch_jsonplaceholder_data

    fetch_jsonplaceholder_data.delay()
    main()
Celery
Configuration(celery_app.py)
Ensure
the
celery_app.py
file
remains
the
same

python
Копировать
код
from celery import Celery
import requests
import json

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def fetch_jsonplaceholder_data():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    data = {}
    for url in urls:
        response = requests.get(url)
        key = url.split('/')[-1]
        data[key] = response.json()

    with open('data.json', 'w') as f:
        json.dump(data, f)

    return "Data saved successfully!"


SQLAlchemy
Configuration(database.py)
Ensure
the
database.py
file
remains
the
same

python
Копировать
код
