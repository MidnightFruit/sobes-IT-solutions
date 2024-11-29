FROM python:3.12-slim

WORKDIR /app

COPY requarement.txt /

RUN pip install -r /requarement.txt --no-cache-dir

COPY . .
