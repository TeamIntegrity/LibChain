from django.shortcuts import render, redirect

import datetime

# Importing students model
from users.models import Student, Staff

# Importing transaction models
from transactions.models import Transaction

# Importing the BookDescription model
from .models import BookDescription, Book

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

        if query.isdecimal():
            results = Book.objects.filter(
                Q(book_number__icontains=query)
            )
            number = True
        else:
            results = BookDescription.objects.filter(
                Q(name__icontains=query) | Q(author__icontains=query)
            )
            number = False
        context={'results':results, 'number': number}
        return render(request, "search.html", context)

    return redirect("/home/")



def add_books(request):
    """ This method will let the admins add books to the database """

    if request.method == "POST":
        book_name = request.POST.get("book_name")
        book_author = request.POST.get("book_author")
        book_description = request.POST.get("book_description")

        book_number_init = int(request.POST.get("book_number_init"))
        book_number_end = int(request.POST.get("book_number_end"))

        initial_stock = (book_number_end - book_number_init)+1

        departments = request.POST.getlist("department")
        subjects = request.POST.getlist("subject")
        semesters = request.POST.getlist("semester")

        book = BookDescription.objects.create(name=book_name, author=book_author,
                description=book_description, initial_stock=initial_stock, available_stock=initial_stock)

        for department in departments:
            dprt = Department.objects.get(name=department)
            book.department.add(dprt)

        for subject in subjects:
            sub = Subject.objects.get(name=subject)
            book.subject.add(sub)

        for semester in semesters:
            sem = Semester.objects.get(semester=semester)
            book.semester.add(sem)

        for i in range(book_number_init, book_number_end+1):
            Book.objects.create(details=book, book_number=i)

        return redirect("/books/add/")

    departments = Department.objects.all()
    semesters = Semester.objects.all()
    subjects = Subject.objects.all()

    context = {"departments": departments, "semesters": semesters,
                "subjects": subjects}
    return render(request, "add_books.html", context)



def issue(request):
    """ This method will allow admin to issue books to the student """

    if request.method == "POST":
        book_number = request.POST.get("book_number")
        library_card_num = request.POST.get("library_card_num")

        book = Book.objects.get(book_number=book_number)
        student = Student.objects.get(libcard=library_card_num)
        context = {"book": book, "student": student}
        return render(request, "issue_confirm.html", context)

    return render(request, "issue.html")



def issue_confirm(request):
    """ This method will show details about the book and student and confirm the issue """

    if request.method == "POST":
        book_number = request.POST.get("book_number")
        libcard = request.POST.get("libcard")

        book = Book.objects.get(book_number=book_number)
        student = Student.objects.get(libcard=libcard)

        staff = Staff.objects.get(userprofile__user=request.user)

        Transaction.objects.create(staff=staff, student=student, book=book, issued=True, issue_time=datetime.datetime.now())

        return redirect("/books/issue/")



def return_book(request):
    """ This method will allow admin to take books back from students """

    if request.method == "POST":
        book_number = request.POST.get("book_number")
        library_card_num = request.POST.get("library_card_num")

        book = Book.objects.get(book_number=book_number)
        student = Student.objects.get(libcard=library_card_num)
        tx_detail = Transaction.objects.get(book=book, student=student, issued=True, returned=False)
        context = {"book": book, "student": student, "tx_detail": tx_detail}
        return render(request, "return_confirm.html", context)

    return render(request, "return.html")



def return_confirm(request):
    """ This method will show details about the book and student and confirm the return """

    if request.method == "POST":
        book_number = request.POST.get("book_number")
        libcard = request.POST.get("libcard")

        book = Book.objects.get(book_number=book_number)
        student = Student.objects.get(libcard=libcard)

        tx = Transaction.objects.get(student=student, book=book, issued=True, returned=False)

        tx.returned = True
        tx.return_time = datetime.datetime.now()

        tx.save()

        return redirect("/books/return/")
