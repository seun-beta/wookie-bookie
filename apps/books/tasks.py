from pathlib import Path

from django.core.files import File
from django.core.files.storage import FileSystemStorage

from celery import shared_task
from cloudinary.uploader import upload_image

from apps.books.models import Book


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=5,
    retry_jitter=True,
    retry_kwargs={"max_retries": 5},
)
def upload_cover_image_task(self, file_name, path, id):

    storage = FileSystemStorage()
    path_object = Path(path)

    with path_object.open(mode="rb") as file:
        cover_image = File(file, name=path_object.name)
        cover_image_url = upload_image(cover_image)

    storage.delete(file_name)
    book = Book.objects.get(id=id)
    book.cover_image = cover_image_url
    book.save()
