FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install -r /requirements.txt

RUN apk del .tmp-build-deps

RUN mkdir -p /usr/src

WORKDIR /usr/src

COPY ./src /usr/src

RUN adduser -D user

USER user

#FROM python:3.9-alpine
#
## create and set working directory
#RUN mkdir /app
#WORKDIR /app
#
## Add current directory code to working directory
#ADD . /app
#
## set default environment variables
#ENV PYTHONUNBUFFERED 1
#ENV LANG C.UTF-8
#ENV DEBIAN_FRONTEND=noninteractive
#
#ENV PORT=8888
#
#RUN pip install --upgrade pip
#
#COPY ./requirements.txt /app/requirements.txt
#
#RUN pip install -r requirements.txt
#
#RUN pip3 install psycopg2
#RUN pip3 install django-heroku
## set project environment variables
## grab these via the Python os.environ
## these are 100% optional here
## $PORT is set by Heroku
#
#
## Install system dependencies with OpenCV
##RUN apt-get update && apt-get install -y --no-install-recommends \
##        tzdata \
##        python3-setuptools \
##        python3-pip \
##        python3-dev \
##        python3-venv \
##        git \
##        && \
##    apt-get clean && \
##    rm -rf /var/lib/apt/lists/*
#
#
## install environment dependencies
#
##RUN pip3 install pipenv
#
## Install project dependencies
##RUN pipenv install --skip-lock --system --dev
#
## Expose is NOT supported by Heroku
## EXPOSE 8000
#CMD gunicorn rest.wsgi:application --bind 0.0.0.0:$PORT

#FROM python:3.9-alpine
#
#RUN mkdir -p /app
#WORKDIR /app
#
#COPY requirements.txt /app/requirements.txt
#
## Configure server
#RUN set -ex \
#    && pip install --upgrade pip \
#    && pip install --no-cache-dir -r /app/requirements.txt
#
## Working directory
#ADD . .
#
## EXPOSE 8000
#
## CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "core.wsgi:application"]
#
#CMD gunicorn rest.wsgi:application --bind 0.0.0.0:$PORT