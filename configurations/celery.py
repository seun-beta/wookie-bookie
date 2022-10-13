import os

from celery import Celery

from configurations.settings.base import SETTINGS_FILE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_FILE)

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
