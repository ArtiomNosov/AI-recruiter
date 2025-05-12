from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify 

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    registration_step = models.IntegerField(default=1)
    temp_session_key = models.CharField(max_length=40, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.username:
            # Генерируем username из email (до символа @)
            base_username = slugify(self.email.split('@')[0])
            self.username = base_username
            # Делаем username уникальным, добавляя число если нужно
            counter = 1
            while CustomUser.objects.filter(username=self.username).exists():
                self.username = f"{base_username}{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email