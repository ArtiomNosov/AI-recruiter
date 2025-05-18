# payment/models.py
from django.db import models

class Tariff(models.Model):
    name = models.CharField("Название тарифа", max_length=100)
    slug = models.SlugField(unique=True, default='temp-slug')
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    duration_days = models.IntegerField("Срок действия (дней)")
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

# payment/models.py
from django.contrib.auth.models import User

class UserTariff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tariff')
    tariff = models.ForeignKey(Tariff, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField("Дата начала", auto_now_add=True)
    end_date = models.DateTimeField("Дата окончания")

    def __str__(self):
        return f"{self.user.username} - {self.tariff.name}"