FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install --upgrade pip -r requirements.txt
COPY .. /app

EXPOSE 8000