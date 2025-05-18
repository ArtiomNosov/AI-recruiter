from django.urls import path
from . import views



urlpatterns = [
    path('', views.payment_page, name='payment'),
    path('select-tariff/', views.select_tariff, name='select_tariff'),
    path('confirm-tariff/<str:tariff_slug>/', views.confirm_tariff, name='confirm_tariff'),
]