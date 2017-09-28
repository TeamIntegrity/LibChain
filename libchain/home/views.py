from django.shortcuts import render, redirect
from django.http import HttpResponse

# Importing the BookDescription model
from books.models import BookDescription

# Importing search utility tool Q
from django.db.models import Q



def home(request):
    """This is the home page functions"""

    books_for_cse = BookDescription.objects.filter(branch='cse')[:12]

    context = {'books_for_cse': books_for_cse}

    return render(request, 'home.html', context)



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
