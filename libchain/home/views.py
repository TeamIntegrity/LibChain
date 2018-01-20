from django.shortcuts import render, redirect
from django.http import HttpResponse

# Importing the book models
from books.models import BookDescription

# Importing department models
from department.models import Department

# Importing user models
from users.models import Student, UserProfile

def home(request):
    """This is the home page functions"""

    # Check to see if the user is logged in
    try:
        student = Student.objects.get(userprofile=UserProfile.objects.get(user=request.user))
    except:
        student = None

    # If user is logged in show the home page according to the user data
    if student != None:
        books_for_cse = BookDescription.objects.filter(department=student.department_name)
        context = {'books_for_cse': books_for_cse}

    else:
        books_for_cse = BookDescription.objects.all()
        context = {'books_for_cse': books_for_cse}

    return render(request, 'home.html', context)
