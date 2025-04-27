from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    paswword = forms.CharField(label='Пароль', widget=forms.PasswordInput)
