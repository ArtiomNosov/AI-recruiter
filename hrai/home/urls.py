from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('use-cases/', views.use_cases, name='use_cases'),
    path('resources/', views.resources, name='resources'),
]