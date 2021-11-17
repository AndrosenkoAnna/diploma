from django.contrib import admin

from .models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'author', 'content', 'created_at', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'author')


admin.site.register(Books, BooksAdmin)
