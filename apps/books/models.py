from django.db import models

from cloudinary.models import CloudinaryField
from djmoney.models.fields import MoneyField

from apps.users.models import User
from apps.utility.base_model import TimeStampedUUIDModel


class Book(TimeStampedUUIDModel):
    title = models.CharField(max_length=512)
    description = models.TextField()
    cover_image = CloudinaryField(null=True, blank=True)
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency="USD",
        max_digits=12,
    )
    author = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f"{self.title}   {self.author}"
