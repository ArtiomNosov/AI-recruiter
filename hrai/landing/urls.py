from django.urls import path
from . import views
from .views import ProfileView

urlpatterns = [
    path('', views.RegisterView.as_view(), name='landing'),
    path('connection/', views.ConnectionView.as_view(), name='connection'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
]
