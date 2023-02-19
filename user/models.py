from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(verbose_name="Изображение", upload_to="users_images", null=True, blank=True)
    birth_date = models.DateTimeField(verbose_name="Дата рождения", blank=True)