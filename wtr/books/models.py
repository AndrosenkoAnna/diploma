from django.db import models
from django.urls import reverse

GENRE_CHOICES = (("Детектив", "детектив"), ("Фантастика", "фантастика"), ("Политика", "политика"),
                 ("Ужасы", "ужасы"), ("Роман", "роман"), ("Психология", "психология"),
                 ("Наука", "наука"), ("Детская", "детская"), ("Юмор", "юмор"))


class Books(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    author = models.CharField(max_length=100, default="Неизвестен", verbose_name="Автор")
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES,
                             default="Неизвестен", verbose_name="Жанр")
    content = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")
    image = models.ImageField(null=True, blank=True, upload_to='media', verbose_name="Изображение")

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('view_books', kwargs={"books_id": self.pk})
