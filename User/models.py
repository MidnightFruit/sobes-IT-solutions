from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    USERNAME_FIELD = 'email'
   
    email = models.EmailField(unique=True, verbose_name="почта", null=False, blank=False)

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'