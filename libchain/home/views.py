from django.shortcuts import render, redirect
from django.http import HttpResponse

from api.views import get_base, get_vars

# Importing the book models
from books.models import BookDescription

# Importing department models
from department.models import Department, Semester, Subject

# Importing user models
from users.models import Student, UserProfile

# Global variables to be used in each methods
semesters, departments, subjects = get_vars()



def home(request):
    """This is the home page functions"""

    base = get_base(request)

    first_row = None
    second_row = None
    third_row = None
    sem = None
    department = None

    if request.user.is_authenticated:
        userprofile = UserProfile.objects.get(user=request.user)

        if userprofile.entity == "student":
            student = Student.objects.get(userprofile=userprofile)
            sem = student.semester
            department = student.department_name

            first_row = BookDescription.objects.filter(department=department, semester=sem)[:6]
            second_row = BookDescription.objects.filter(department=department)[:6]
            third_row = BookDescription.objects.filter(semester=sem)[:6]

    # Books for branches
    books_for_cse = BookDescription.objects.filter(department__name = "Computer Science & Engineering")[:6]
    books_for_civil = BookDescription.objects.filter(department__name = "Civil Engineering")[:6]
    books_for_mech = BookDescription.objects.filter(department__name = "Mechanical Engineering")[:6]
    books_for_et = BookDescription.objects.filter(department__name = "Electronics & Telecommunications Engineering")[:6]
    books_for_eee = BookDescription.objects.filter(department__name = "Electrical & Electronics Engineering")[:6]

    # Books for subjects
    books_for_maths = BookDescription.objects.filter(subject__name = "Mathematics")
    books_for_physics = BookDescription.objects.filter(subject__name = "Physics")
    books_for_chemistry = BookDescription.objects.filter(subject__name = "Chemistry")


    context = {'books_for_cse': books_for_cse, 'books_for_civil': books_for_civil,
                'books_for_mech': books_for_mech, "books_for_et": books_for_et,
                "books_for_eee": books_for_eee, "base": base, 'semesters': semesters,
                'departments': departments, 'subjects': subjects, "first_row": first_row,
                "second_row": second_row, "third_row": third_row, "sem": sem, "branch": department, "books_for_maths": books_for_maths,
                "books_for_chemistry": books_for_chemistry, "books_for_physics": books_for_physics}

    return render(request, 'home.html', context)
