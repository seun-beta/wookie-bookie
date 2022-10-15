from django.core.files import File
from django.core.files.storage import FileSystemStorage

from djmoney.serializers import MoneyField
from rest_framework import serializers

from apps.books.models import Book
from apps.books.tasks import upload_cover_image_task


class BookListSerializer(serializers.ModelSerializer):

    """Serializer for list of books for unauthenticated users"""

    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        exclude = ["created_at", "updated_at", "author", "pkid"]

    def get_author_name(self, attrs):
        return attrs.author.get_full_name


class BookSerializer(serializers.ModelSerializer):

    """Serializer for creating of books for authenticated users"""

    price = MoneyField()
    cover_image = serializers.ImageField()

    class Meta:
        model = Book
        exclude = ["created_at", "updated_at", "author"]

    def create(self, validated_data):

        cover_image = validated_data.pop("cover_image")
        storage = FileSystemStorage()
        cover_image.name = storage.get_available_name(cover_image.name)
        storage.save(cover_image.name, File(cover_image))

        book = Book.objects.create(**validated_data)
        upload_cover_image_task.delay(
            path=storage.path(cover_image.name),
            file_name=cover_image.name,
            id=book.id,
        )
        return book

    def update(self, instance, validated_data):
        # breakpoint()
        cover_image = validated_data.get("cover_image")

        if cover_image:
            cover_image = validated_data.pop("cover_image")
            storage = FileSystemStorage()
            cover_image.name = storage.get_available_name(cover_image.name)
            storage.save(cover_image.name, File(cover_image))

            upload_cover_image_task.delay(
                path=storage.path(cover_image.name),
                file_name=cover_image.name,
                id=instance.id,
            )
        instance.title = validated_data.pop("title", instance.title)
        instance.description = validated_data.pop("description", instance.description)
        instance.price = validated_data.pop("price", instance.price)
        instance.save()

        return instance
