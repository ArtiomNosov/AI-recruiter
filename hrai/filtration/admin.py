from django.contrib import admin
from .models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'location', 'experience', 'desired_salary', 'score')
    list_filter = ('experience', 'desired_salary')
    search_fields = ('full_name', 'skills')


admin.site.site_header = "AI-Recruiter Administration"
from django.contrib import admin

# Register your models here.
