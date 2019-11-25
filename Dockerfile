FROM python:3.8.0-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
