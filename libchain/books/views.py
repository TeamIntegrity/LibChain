from django.shortcuts import render, redirect

# Importing the BookDescription model
from .models import BookDescription

# Importing search utility tool Q
from django.db.models import Q


def by_semester(request, sem):
    """This will show the books by semester"""
    pass

def by_branch(request, b):
    """This will show the books by branch name"""
    pass

def by_subject(request, sub):
    """This will show the books based on the subject"""
    pass

def description(request, id):
    """This will show the book's description based on the id"""
    pass


def search(request):
    """This method will search the entire database for the suggested books"""

    if request.method == 'POST':
        query =  str(request.POST.get('param'))
        results = BookDescription.objects.filter(
            Q(name__icontains=query) | Q(branch__icontains=query) |
            Q(subject__icontains=query) | Q(author__icontains=query)
        )
        context={'results':results}
        return render(request, "search.html", context)

    return redirect("/home/")
