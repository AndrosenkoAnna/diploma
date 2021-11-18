# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Books


def index(request):
    books = Books.objects.all()
    context = {
        'books': books,
        'title': 'Список книг'
    }
    return render(request, template_name='books/index.html', context=context)

def view_books(request, books_id):
    books_item = Books.objects.get(pk=books_id)
    return render(request, 'books/view_books.html', {"books_item": books_item})
