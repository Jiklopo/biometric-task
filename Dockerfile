FROM python:3.9-alpine
ENV PYTHONBUFFERED 1
COPY . app/
WORKDIR app/

RUN apk -U upgrade \
    && apk add build-base

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN python manage.py migrate