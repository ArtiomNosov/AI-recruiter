# download/forms.py
from django import forms
from .models import Resume, Vacancy

class ResumeUploadForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('vacancy', 'file')
        widgets = {
            'vacancy': forms.Select(attrs={
                'class': 'vacancy-select'
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'resume-file-input',
                'accept': '.pdf,.doc,.docx'      # ← браузерный фильтр
            }),
        }

    def clean_file(self):
        f = self.cleaned_data['file']
        # базовая проверка расширения на всякий случай
        ext = f.name.lower().rsplit('.', 1)[-1]
        if ext not in ('pdf', 'doc', 'docx'):
            raise forms.ValidationError("Разрешены только файлы PDF и DOC(X).")
        return f
