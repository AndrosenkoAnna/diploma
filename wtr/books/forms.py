from django import forms
from .models import GENRE_CHOICES


class BooksForm(forms.Form):
    title = forms.CharField(max_length=150, label="Название",
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label="Описание", widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5
    }))
    genre = forms.ChoiceField(choices=GENRE_CHOICES, label="Жанр",
                              widget=forms.Select(attrs={"class": "form-control"}))
