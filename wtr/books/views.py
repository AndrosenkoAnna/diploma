# from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    book = Book.objects.all()
    res = "<h1>All Books</h1>"
    for item in book:
        res += f"<div>{item.title}\n{item.content}</div>"
    return HttpResponse(res)

