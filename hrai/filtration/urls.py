from django.urls import path
from . import views  # Импорт views из текущего каталога

urlpatterns = [
    path('', views.candidate_list, name='candidate_list'),  # Теперь views доступен
    #path('cta/', views.cta_action, name='cta_link'),
    path('candidates/', views.candidate_list, name='candidate_list'),

]
