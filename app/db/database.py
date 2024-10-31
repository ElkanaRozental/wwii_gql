from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

from app.models import Base
from app.settings.config import DB_URL

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
