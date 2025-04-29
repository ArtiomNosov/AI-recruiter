from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CandidateSignUpForm(UserCreationForm):
    email = forms.EmailField(
        label='Почта',
        error_messages={
            'required': 'Пожалуйста, введите адрес электронной почты',
            'invalid': 'Введите корректный email, например name@example.com',
        }
    )
    phone = forms.CharField(
        label='Телефон',
        help_text='Введите 11 цифр, например 79001234567',
        error_messages={
            'required': 'Пожалуйста, введите номер телефона',
            'invalid': 'Номер телефона должен содержать 11 цифр',
        }
    )
   
    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['username'].label = 'Логин'
        self.fields['username'].error_messages = {
            'required': 'Пожалуйста, введите логин'
        }
        self.fields['email'].label = 'Почта'
        self.fields['phone'].label = 'Телефон'
        self.fields['password1'].label = 'Пароль'
        self.fields['password1'].error_messages.update({
            'required': 'Пожалуйста, введите пароль',
            'password_mismatch': 'Пароли не совпадают'
        })
        self.fields['password2'].label = 'Повторите пароль'
        self.fields['password2'].error_messages.update({
            'required': 'Пожалуйста, повторите пароль'
        })