from django.shortcuts import render, redirect
from django.http import HttpResponse

from api.views import get_base

# Importing the book models
from books.models import BookDescription

# Importing department models
from department.models import Department

# Importing user models
from users.models import Student, UserProfile

def home(request):
    """This is the home page functions"""

    base = get_base(request)

    # Check to see if the user is logged in
    try:
        student = Student.objects.get(userprofile=UserProfile.objects.get(user=request.user))
    except:
        student = None

    # If user is logged in show the home page according to the user data
    if student != None:
        books_for_cse = BookDescription.objects.filter(department=student.department_name)
        context = {'books_for_cse': books_for_cse, "base": base}

    else:
        books_for_cse = BookDescription.objects.filter(department__name = "COMPUTER SCIENCE AND ENGINEERING")[:4]
        books_for_civil = BookDescription.objects.filter(department__name = "CIVIL ENGINEERING")[:4]
        books_for_mech = BookDescription.objects.filter(department__name = "MECHANICAL ENGINEERING")[:4]
        context = {'books_for_cse': books_for_cse, "books_for_civil": books_for_civil, "books_for_mech": books_for_mech, "base": base}

    return render(request, 'home.html', context)
