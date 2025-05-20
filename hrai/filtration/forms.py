from django import forms
from .models import Resume


class ResumeFilterForm(forms.Form):
    skills = forms.CharField(
        label='Ключевые навыки',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Введите навыки через запятую'})
    )

    experience = forms.ChoiceField(
        label='Опыт работы',
        choices=Resume.EXPERIENCE_CHOICES,
        required=False
    )

    desired_salary = forms.ChoiceField(
        label='Зарплатные ожидания',
        choices=Resume.SALARY_CHOICES,
        required=False
    )