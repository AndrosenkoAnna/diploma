# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Books
from .forms import BooksForm, UserRegisterForm, UserLoginForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, logout


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


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'books/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'books/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')
