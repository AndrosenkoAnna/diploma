# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Books
from .forms import BooksForm
from django.core.files.storage import FileSystemStorage


def index(request):
    books = Books.objects.all()
    context = {
        'books': books,
        'title': 'ЧтоЧитать'
    }
    return render(request, template_name='books/index.html', context=context)

def view_books(request, books_id):
    books_item = Books.objects.get(pk=books_id)
    return render(request, 'books/view_books.html', {"books_item": books_item})


def add_books(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            Books.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = BooksForm()
    return render(request, 'books/add_books.html', {'form': form})
