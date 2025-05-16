from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('<int:resume_id>/', views.resume_detail, name='resume_detail'),  # Это критически важно
    path('<int:resume_id>/like/', views.like_resume, name='like_resume'),
    path('upload/', views.upload_resume, name='upload_resume'),
]