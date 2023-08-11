FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir //django-rest

WORKDIR /django-rest

ADD . /django-rest

RUN pip install -r requirements.txt
