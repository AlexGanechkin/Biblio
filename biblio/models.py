from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")

    class Meta:
        abstract = True


class PersonBaseModel(BaseModel):
    first_name = models.CharField(verbose_name="Имя", max_length=100)
    last_name = models.CharField(verbose_name="Фамилия", max_length=200)

    class Meta:
        abstract = True
