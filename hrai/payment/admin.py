# payment/admin.py
from django.contrib import admin
from .models import Tariff, UserTariff

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "duration_days")

@admin.register(UserTariff)
class UserTariffAdmin(admin.ModelAdmin):
    list_display = ("user", "tariff", "start_date", "end_date")