FROM python:3.9

RUN mkdir /fastapi

WORKDIR /fastapi

COPY req.txt .

RUN pip install -r req.txt

COPY . .

WORKDIR src
