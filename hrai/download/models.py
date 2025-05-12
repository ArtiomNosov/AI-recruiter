from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Vacancy(models.Model):
    title = models.CharField("Вакансия", max_length=200)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    FORMAT_CHOICES = [
        ('pdf', 'PDF'),
        ('doc', 'DOC/DOCX'),
    ]

    user    = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name="Вакансия")
    file    = models.FileField("Файл резюме", upload_to='resumes/')
    fmt     = models.CharField("Формат", max_length=4, choices=FORMAT_CHOICES)
    uploaded_at = models.DateTimeField("Дата загрузки", auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.vacancy.title}"
