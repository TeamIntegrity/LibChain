from django.shortcuts import render, redirect
from django.http import HttpResponse

# Importing the BookDescription model
from books.models import BookDescription


def home(request):
    """This is the home page functions"""

    books_for_cse = BookDescription.objects.filter(branch='cse')[:12]

    context = {'books_for_cse': books_for_cse}

    return render(request, 'home.html', context)
