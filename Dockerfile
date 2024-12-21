FROM python:3.11-alpine

WORKDIR /app

COPY ../universal_template/backend/requirements.txt /app
RUN pip3 install --upgrade pip -r requirements.txt
COPY ../universal_template/backend /app

EXPOSE 8000