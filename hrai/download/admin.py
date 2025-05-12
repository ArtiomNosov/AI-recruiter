from django.contrib import admin

from django.contrib import admin
from .models import Vacancy, Resume

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'vacancy', 'uploaded_at')
    list_filter  = ('vacancy',)
