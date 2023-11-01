FROM python:3.9

RUN mkdir /fastapi

WORKDIR /fastapi

COPY req.txt .

RUN pip install -r req.txt

COPY . .

WORKDIR src

CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
