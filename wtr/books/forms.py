from django import forms
from .models import GENRE_CHOICES
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                                help_text='Должен содержать более 8 символов, включать в себя буквы и цифры',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', help_text='Введите пароль повторно',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class BooksForm(forms.Form):
    title = forms.CharField(max_length=150, label="Название",
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label="Описание", widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5
    }))
    author = forms.CharField(max_length=150, label="Автор",
                             widget=forms.TextInput(attrs={"class": "form-control"}))
    genre = forms.ChoiceField(choices=GENRE_CHOICES, label="Жанр",
                              widget=forms.Select(attrs={"class": "form-control"}))
    image = forms.ImageField()







