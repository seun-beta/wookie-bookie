FROM python:3.10.2-slim-bullseye

WORKDIR /app

ENV PIP_DISABLE_PIP_VERSION_CHECK 1

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY requirements/* ./app/requirements/

RUN pip install -r ./app/requirements/development.txt

COPY . .
