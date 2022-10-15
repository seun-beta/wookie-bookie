# flake8: noqa
from .base import *
from .base import env

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG", default="False")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

ADMIN_URL = env.str("ADMIN_URL")

DATABASES = {"default": env.db("DATABASE_URL")}

DATABASES["default"]["ATOMIC_REQUESTS"] = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 60

SECURE_HSTS_PRELOAD = env.bool("SECURE_HSTS_PRELOAD", default=True)

SECURE_CONTENT_TYPE_NOSNIFF = env.bool("SECURE_CONTENT_TYPE_NOSNIFF", default=True)

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)


CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.wookie-bookie\.com$",
]
