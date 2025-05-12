from django.urls import path
from . import views
from django.views.generic import RedirectView  
from .views import ResumeUploadView, ResumeToolsView, ResumeDeleteView


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='resume_upload', permanent=False), name='download_index'),
    path('upload/', views.ResumeUploadView.as_view(), name='resume_upload'),
    path('tools/', views.ResumeToolsView.as_view(), name='resume_tools'),
    path('delete/<int:pk>/', ResumeDeleteView.as_view(), name='resume_delete'),
]
