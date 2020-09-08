FROM python:3.7-alpine

RUN apk add --no-cache --update \
    build-base \
    postgresql-dev \
    bash \
    && rm -rf /var/cache/apk/*

RUN mkdir /django_chat
RUN mkdir /static
WORKDIR /django_chat

COPY requirements.txt /django_chat

RUN pip install --upgrade pip \
    && pip install -r requirements.txt