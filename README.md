# Wookie Bookie


## Table of Contents

- [About](#about)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Author](#author)

## About <a name = "about"></a>

Wookie Bookie

## Project Structure <a name = "project-structure"></a>


```bash

.
├── Dockerfile
├── LICENSE
├── README.md
├── apps
│   ├── books
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── users
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── managers.py
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   └── __init__.py
│       ├── models.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── configurations
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── swagger_scheme_generator.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── logs
│   └── debug.log
├── makefile
├── manage.py
├── pyproject.toml
├── requirements
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
├── runtime.txt
└── setup.cfg

```

## Prerequisites <a name = "prerequisites"></a>

- Python 3.10
- PostgreSQL 14
- Redis

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

 - Run `git clone https://github.com/seun-beta/wookie-bookie` to clone the project locally.
 - Create a local postgres database locally and add it's url to the DATBASE_URL env variable.
 - Run `pip install -r requirements/development.txt`
 - Run migration with `python manage.py migrate`.


Now, make sure to have 3 extra terminals/command prompts for the following commands:
1) To run the redis server: `redis-server`
2) Start the app with `python manage.py runserver`
3) To run celery: `python -m celery -A core worker`
4) To run flower: `celery -A core flower`


## Author <a name = "author"></a>
This software was created by Seunfunmi Adegoke, a Backend & Cloud Engineer