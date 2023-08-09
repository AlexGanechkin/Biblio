from django.db import models

from biblio.models import BaseModel, PersonBaseModel


class Author(PersonBaseModel):

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(BaseModel):

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    title = models.CharField(verbose_name="Название", max_length=200)
    description = models.CharField(verbose_name="Описание", max_length=1000)
    page_number = models.PositiveSmallIntegerField()
    author = models.ForeignKey(Author, verbose_name="Пользователь", on_delete=models.CASCADE, null=True)
    books_number = models.PositiveBigIntegerField()

    def __str__(self):
        return self.title
