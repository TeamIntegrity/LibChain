from django.shortcuts import render, redirect

# Importing the BookDescription model
from .models import BookDescription

# Importing department models
from department.models import Department, Semester, Subject

# Importing search utility tool Q
from django.db.models import Q


def by_semester(request, sem):
    """This will show the books by semester"""

    semester = Semester.objects.get(semester=sem)
    books_query = BookDescription.objects.filter(semester=semester)

    context = {'books_query': books_query}

    return render(request, "bookquery.html", context)



def by_branch(request, b):
    """This will show the books by branch name"""

    department = Department.objects.get(name=b)
    books_query = BookDescription.objects.filter(department=department)

    context = {'books_query': books_query}

    return render(request, "bookquery.html", context)



def by_subject(request, sub):
    """This will show the books based on the subject"""

    subject = Subject.objects.filter(subject=sub)
    books_query = BookDescription.objects.filter(subject=subject)

    context = {'books_query': books_query}

    return render(request, 'bookquery.html', context)




def description(request, id):
    """This will show the book's description based on the id"""
    book = BookDescription.objects.get(id=id)
    context = {"book": book}

    return render(request, "bookdescription.html", context)



def search(request):
    """This method will search the entire database for the suggested books"""

    if request.method == 'POST':
        query =  str(request.POST.get('param'))
        if not query:
            return render(request, "search.html")
        results = BookDescription.objects.filter(
            Q(name__icontains=query) | Q(author__icontains=query)
        )
        context={'results':results}
        return render(request, "search.html", context)

    return redirect("/home/")



def add_books(request):
    """ This method will let the admins add books to the database """

    if request.method == "POST":
        book_name = request.POST.get("book_name")
        book_author = request.POST.get("book_author")
        book_description = request.POST.get("book_description")

        departments = request.POST.getlist("department")
        subjects = request.POST.getlist("subject")
        semesters = request.POST.getlist("semester")

        book = BookDescription.objects.create(name=book_name, author=book_author,
                description=book_description, initial_stock=0, available_stock=0)

        for department in departments:
            dprt = Department.objects.get(name=department)
            book.department.add(dprt)

        for subject in subjects:
            sub = Subject.objects.get(name=subject)
            book.subject.add(sub)

        for semester in semesters:
            sem = Semester.objects.get(semester=semester)
            book.semester.add(sem)

        return redirect("/books/add/")

    departments = Department.objects.all()
    semesters = Semester.objects.all()
    subjects = Subject.objects.all()

    context = {"departments": departments, "semesters": semesters,
                "subjects": subjects}
    return render(request, "add_books.html", context)
