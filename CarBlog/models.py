from django.db import models
from User.models import User

class Car(models.Model):
    make = models.CharField(verbose_name="марка автомобиля", max_length=32)
    model = models.CharField(verbose_name="модель автомобиля", max_length=32)
    year = models.PositiveSmallIntegerField(verbose_name="год выпуска")
    description = models.TextField(verbose_name="описание автомобиля")
    created_at = models.DateTimeField(verbose_name="дата и время создания записи", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="дата и время последнего обновления записи", auto_now=True)
    owner = models.ForeignKey(User, verbose_name="пользователь, который создал запись", null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'


class Comment(models.Model):
    content = models.TextField(verbose_name="содержание комментария")
    created_at = models.DateTimeField(verbose_name="дата и время создания комментария", auto_now_add=True)
    car = models.ForeignKey(Car, verbose_name="автомобиль к которому оставлен комментарий", null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="автор комментария", null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'