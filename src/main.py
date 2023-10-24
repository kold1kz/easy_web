from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
# from pydantic import BaseModel
# from sqlalchemy import create_engine, Column, Integer, String, DateTime, text
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
# import httpx
import uvicorn

# Инициализация FastAPI
app = FastAPI()


# # Инициализация SQLAlchemy
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

@app.get("/")
async def home():
    """home page"""
    return FileResponse('index.html')


# # Запуск FastAPI приложения
# if __name__ == "__main__":
#     uvicorn.run("main:app", host='localhost', port=8000, reload=True, workers=3)
