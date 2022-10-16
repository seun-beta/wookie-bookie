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
├── Dockerfile
├── LICENSE
├── README.md
├── apps
│   ├── books
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tasks.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── test_image.png
│   │   │   ├── test_models.py
│   │   │   └── test_views.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── users
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── managers.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_alter_user_author_pseudonym.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── test_models.py
│   │   │   └── test_views.py
│   │   ├── urls.py
│   │   └── views.py
│   └── utility
│       ├── base_model.py
│       ├── filters.py
│       ├── pagination.py
│       └── permissions.py
├── configurations
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── settings
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── test.py
│   ├── swagger_scheme_generator.py
│   ├── urls.py
│   └── wsgi.py
├── local.yml
├── logs
│   └── debug.log
├── makefile
├── manage.py
├── requirements
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
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

### Run without docker compose
Now, make sure to have 4 terminals/command prompts for the following commands:
1) To run the redis server: `redis-server`
2) Start the app with `python manage.py runserver`
3) To run celery: `python -m celery -A configurations worker`
4) To run flower: `celery -A configurations flower`

### Run with docker compose
1) Run `make build` to build all the container images
2) Run  `make up` to run the images in seperate containers
3) Run `make test` to run all tests in the multi-container environment

### Swagger Documentation
1) The Swagger documentation can be found here http://127.0.0.1:8000/swagger
2) The Swagger documentation export can be found here http://127.0.0.1:8000/swagger.json  OR http://127.0.0.1:8000/swagger.yaml

## Author <a name = "author"></a>
This software was created by Seunfunmi Adegoke, a Backend & Cloud Engineer