from django.db import models

GENRE_CHOICES = (("Детектив", "детектив"), ("Фантастика", "фантастика"), ("Политика", "политика"),
                 ("Ужасы", "ужасы"), ("Роман", "роман"), ("Психология", "психология"),
                 ("Наука", "наука"), ("Детская", "детская"), ("Юмор", "юмор"))


class Book(models.Model):
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, default="Неизвестен")
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
