from django.shortcuts import render, redirect
from django.http import HttpResponse

from api.views import get_base

# Importing the book models
from books.models import BookDescription

# Importing department models
from department.models import Department, Semester, Subject

# Importing user models
from users.models import Student, UserProfile

def home(request):
    """This is the home page functions"""

    base = get_base(request)

    books_for_cse = BookDescription.objects.filter(department__name = "COMPUTER SCIENCE AND ENGINEERING")[:5]
    books_for_civil = BookDescription.objects.filter(department__name = "CIVIL ENGINEERING")[:5]
    books_for_mech = BookDescription.objects.filter(department__name = "MECHANICAL ENGINEERING")[:5]

    semesters = Semester.objects.all()
    departments = Department.objects.all()[:5]
    subjects = Subject.objects.all()
    
    context = {'books_for_cse': books_for_cse, 'books_for_civil': books_for_civil,
                'books_for_mech': books_for_mech, "base": base, 'semesters': semesters,
                'departments': departments, 'subjects': subjects}

    return render(request, 'home.html', context)
