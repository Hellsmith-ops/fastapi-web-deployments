from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./database/booksapp.db'

#create engine from sqlalchemy(url, arguments)
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}) # tell fastapi to check multiple threads

#create local session from sessionmaker(no automatic actions from database, full manual control)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #bind to engine

#create an object to control database
Base = declarative_base()