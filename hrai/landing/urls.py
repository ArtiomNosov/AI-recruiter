from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegisterView.as_view(), name='landing'),
    path('connection/', views.ConnectionView.as_view(), name='connection'),
]