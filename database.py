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
