FROM python:3.9-slim-buster
ENV PYTHONBUFFERED 1
COPY . app/
WORKDIR app/

RUN apt update \
    && apt upgrade \
    && pip install -r requirements.txt

