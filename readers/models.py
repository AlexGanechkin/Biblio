from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from biblio.models import PersonBaseModel
from books.models import Book


class Reader(PersonBaseModel):

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    phone_number = models.CharField(max_length=11, validators=[
        RegexValidator(
            regex=r'7\d{10}',
            message='Не соответствует формату. Формат: 71234567890'
        )
    ])
    is_active = models.BooleanField(default=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
