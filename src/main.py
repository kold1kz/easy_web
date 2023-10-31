'''main file'''
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List
from postgres import Session, get_db, SessionLocal, desc
from models.models import Victorina, request, VictorinaResponse
from httpx import AsyncClient
import logging
# import uvicorn


# Инициализация FastAPI
app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """home page"""
    info = {"text": "some text"}
    return templates.TemplateResponse("index.html",
                                      {"request": request, "data": info})


@app.post("/question", response_model=VictorinaResponse)
async def question(data: request, db: Session = Depends(get_db)) -> VictorinaResponse:
    """question request"""
    if data.questions_num == 0:
        return Victorina()
    try:
        for _ in range(data.questions_num):
            question = await do_response(db)
            # questions.append(question)
            await save_question(question)
        return question
    except Exception as e:
        logging.error("Произошла ошибка в работе функции question: %s", str(e))
        raise HTTPException(
            status_code=500, detail="Произошла ошибка в работе функции")


@app.get("/do_response/")
async def do_response(db: Session = Depends(get_db)) -> VictorinaResponse:
    '''do request to random'''
    async with AsyncClient() as client:
        url = f'https://jservice.io/api/random?count=1'
        try:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                item = VictorinaResponse(
                    id=data[0]["id"], question=data[0]["question"], answer=data[0]['answer'], date=data[0]["created_at"])
                if item is None:
                    raise HTTPException(
                        status_code=404, detail="Объект не определен")
                elif await get_object_by_id(data[0]["id"], db) is False:
                    await do_response(db)
            else:
                raise HTTPException(
                    status_code=505, detail="Проблемы с ответом (httpx)")
            return item
        except Exception as e:
            logging.error(
                "Произошла ошибка в работе функции do_response: %s", str(e))
            raise HTTPException(
                status_code=500, detail="Произошла ошибка при проверке объекта")


@app.get("/get_object_by_id/")
async def get_object_by_id(id: int, db: Session = Depends(get_db)) -> bool:
    """get todo by id"""
    try:
        return db.query(Victorina).filter(
            Victorina.id == id).first() is None
    except Exception as e:
        logging.error(
            "Произошла ошибка в работе функции get_object_by_id: %s", str(e))
        raise HTTPException(
            status_code=500, detail="Произошла ошибка при работе с бд")


@app.get("/save_question/")
async def save_question(item: VictorinaResponse) -> None:
    """save question in db and return answer"""
    try:
        session = SessionLocal()
        try:
            with session.begin() as transaction:
                victorina_item = Victorina(
                    id=item.id,
                    question=item.question,
                    answer=item.answer,
                    date=item.date
                )
                session.add(victorina_item)
                transaction.commit()
            # await db.flush()
        except Exception as e:
            logging.error(
                "Произошла ошибка в работе функции save_question: %s", str(e))
            transaction.rollback()
        finally:
            session.close()
    except Exception as e:
        logging.error(
            "Произошла ошибка в работе функции save_question: %s", str(e))
        raise HTTPException(
            status_code=500, detail="Произошла ошибка при добавлении объекта")


@app.get("/last_answer/")
async def last_answer(db: Session = Depends(get_db)) -> VictorinaResponse:
    """return last answer was saved"""
    try:
        answer = db.query(Victorina).order_by(
            desc(Victorina.date)).first()
        if answer is None:
            answer = Victorina()
        return answer
    except Exception as e:
        logging.error(
            "Произошла ошибка в работе функции last_answer: %s", str(e))
        raise HTTPException(
            status_code=500, detail="Произошла ошибка при добавлении объекта")
