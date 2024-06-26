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


# import unittest
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# DATABASE_URL = "sqlite:///./test.db"
# Base = declarative_base()
#
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
# class User(Base):
#     tablename = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, unique=True, index=True)
#     username = Column(String, index=True)
#
#
# Base.metadata.create_all(bind=engine)
# Running
# the
# Components
# Start
# the
# Redis
# server
# bash
# Копировать
# код
# redis - server
# Run
# the
# Celery
# worker
# bash
# Копировать
# код
# celery - A
# celery_app
# # worker - -loglevel = info
# Run
# the
# bot
# bash
# Копировать
# код
# python
# bot.py
# Replace
# 'YOUR_BOT_API_TOKEN'
# # with your actual Telegram bot API token.
#
# This
# updated
# version
# uses
# aiogram
# 3.0 and includes
# a
# bot
# that
# handles
# start and news
# commands, integrating
# Celery
# # for background tasks and SQLAlchemy for database interactions.