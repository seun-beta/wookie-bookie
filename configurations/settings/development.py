# flake8: noqa
from .base import *
from .base import env

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", default="False")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*", "127.0.0.1:8000"])

ADMIN_URL = env.str("ADMIN_URL", default="admin")

DATABASES = {
    "default": env.db("DATABASE_URL"),
}

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DEBUG_TOOLBAR_CONFIG = {
    "JQUERY_URL": "",
}

INTERNAL_IPS = [
    "127.0.0.1",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "stream": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["stream"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
