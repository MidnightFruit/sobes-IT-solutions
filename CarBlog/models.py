from django.db import models
from User.models import User

class Car(models.Model):
    make = models.CharField(verbose_name="марка автомобиля", max_length=32)
    model = models.CharField(verbose_name="модель автомобиля", max_length=32)
    year = models.PositiveSmallIntegerField(verbose_name="год выпуска")
    description = models.CharField(verbose_name="описание автомобиля", max_length=1024)
    created_at = models.DateTimeField(verbose_name="дата и время создания записи", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="дата и время последнего обновления записи", auto_now=True)
    owner = models.ForeignKey(User, verbose_name="пользователь, который создал запись", on_delete=models.CASCADE)
    

class Comment(models.Model):
    content = models.TextField(verbose_name="содержание комментария")
    created_at = models.DateTimeField(verbose_name="дата и время создания комментария", auto_now_add=True)
    car = models.ForeignKey(Car, verbose_name="автомобиль к которому оставлен комментарий", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="автор комментария", on_delete=models.CASCADE)
    