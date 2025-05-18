from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Resume(models.Model):
    # Определение полей модели
    full_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    desired_salary = models.DecimalField(max_digits=10, decimal_places=2)
    skills = models.TextField()
    score = models.IntegerField()
    resume_file = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Определение класса Meta
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"
        ordering = ['created_at']  # Пример: сортировка по дате создания

    # Определение выбора для полей (если необходимо)
    EXPERIENCE_CHOICES = [
        ('1-2 years', '1-2 years'),
        ('3-5 years', '3-5 years'),
        ('5+ years', '5+ years'),
    ]

    SALARY_CHOICES = [
        ('<30k', '<30k'),
        ('30k-50k', '30k-50k'),
        ('50k-70k', '50k-70k'),
        ('70k+', '70k+'),
    ]

    full_name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    experience = models.CharField(max_length=10, choices=EXPERIENCE_CHOICES)
    desired_salary = models.CharField(max_length=10, choices=SALARY_CHOICES)
    skills = models.TextField(help_text="Навыки через запятую")
    score = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    resume_file = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


from django.db import models

# Create your models here.
