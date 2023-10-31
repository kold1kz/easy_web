'''postgres'''
from sqlalchemy import create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from databases import Database

SQLALCHEMY_DATABASE_URL = "postgresql://root:root@pg_db:5432/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

database = Database(SQLALCHEMY_DATABASE_URL)

Base.metadata.create_all(bind=engine)

def get_db():
    '''connect to db'''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


