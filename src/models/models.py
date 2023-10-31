'''models for work with db'''
from postgres import Base
from sqlalchemy import String, Integer, Column, Date, MetaData
from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime


class Victorina(Base):
    __tablename__ = 'Victorina'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    date = Column(Date)

    metadata = MetaData()


class request(BaseModel):
    questions_num: Optional[int]

class VictorinaResponse(BaseModel):
    id: Optional[int]
    question: Optional[str]
    answer: Optional[str]
    date: Optional[datetime]

class VictorinaListResponse(BaseModel):
    class Config:
        arbitrary_types_allowed = True
    items: List[VictorinaResponse]


