from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'