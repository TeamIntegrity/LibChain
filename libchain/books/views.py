from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

import datetime

# Importing students model
from users.models import UserProfile, Student, Staff

# Importing transaction models
from transactions.models import Transaction

# Importing the BookDescription model
from .models import BookDescription, Book

# Importing department models
from department.models import Department, Semester, Subject

# Importing search utility tool Q
from django.db.models import Q

# Importing base template method from api
from api.views import get_base, get_vars

# Global variables to be used in each methods
semesters, departments, subjects = get_vars()


def by_semester(request, sem):
    """This will show the books by semester"""

    base = get_base(request)

    semester = Semester.objects.get(semester=sem)
    books_query = BookDescription.objects.filter(semester=semester)

    context = {'books_query': books_query, "query": "semester "+sem, "base": base, "semesters": semesters,
                "departments": departments, "subjects": subjects}

    return render(request, "bookquery.html", context)



def by_branch(request, b):
    """This will show the books by branch name"""
    branch = ' '.join(b.split('-'))

    department = Department.objects.get(name=branch.upper())
    books_query = BookDescription.objects.filter(department=department)

    base = get_base(request)

    context = {'books_query': books_query, "base": base, "query": b, "semesters": semesters,
                "departments": departments, "subjects": subjects}

    return render(request, "bookquery.html", context)


def by_branch_sem(request, b, sem):
    """This will show the books by branch & sem"""
    branch = ' '.join(b.split('-'))

    department = Department.objects.get(name=branch.upper())
    books_query = BookDescription.objects.filter(department=department, semester=sem)

    base = get_base(request)

    context = {'books_query': books_query, "base": base, "query": b, "query2": sem, "semesters": semesters,
                "departments": departments, "subjects": subjects}

    return render(request, "bookquery.html", context)



def by_subject(request, sub):
    """This will show the books based on the subject"""
    subj = ' '.join(sub.split('-'))

    subject = Subject.objects.get(name=subj.upper())
    books_query = BookDescription.objects.filter(subject=subject)

    base = get_base(request)

    context = {'books_query': books_query, "base": base, "base": base, "query": sub, "semesters": semesters,
                "departments": departments, "subjects": subjects}

    return render(request, 'bookquery.html', context)




def description(request, id):
    """This will show the book's description based on the id"""
    book = BookDescription.objects.get(id=id)
    available_nos = len(list(Book.objects.filter(details=book, available=True)))
    if available_nos > 0:
        available = True
    else:
        available = False
    base = get_base(request)
    context = {"book": book, "base": base, "semesters": semesters,
                "departments": departments, "subjects": subjects, "available": available}

    return render(request, "bookdescription.html", context)



def search(request):
    """This method will search the entire database for the suggested books"""
    base = get_base(request)

    if request.method == 'POST':
        query =  request.POST.get('param')
        if not query:
            return render(request, "search.html")


        books_by_name = BookDescription.objects.filter(
            Q(name__icontains=query) | Q(author__icontains=query)
            | Q(description__icontains=query) | Q(department__name__icontains=query)
            | Q(subject__name__icontains=query)
        )

        try:
            books_by_num = Book.objects.get(book_number=query)
        except:
            books_by_num = None

        context={"base": base, "semesters": semesters, "departments": departments,
                "subjects": subjects, "query": query, "books_by_name": books_by_name,
                "books_by_num": books_by_num}
        return render(request, "search.html", context)

    return redirect("/home/")


@login_required
def details(request):
    """ Find a books history """
    base = get_base(request)

    if UserProfile.objects.get(user=request.user).entity != 'staff':
        return redirect('/home/')

    if request.method == "POST":
        query = request.POST.get('query')

        if query.isdecimal():
            try:
                book = Book.objects.get(book_number=query)
            except:
                book = None
            context = {"base": base, "semesters": semesters, "departments": departments,
                    "subjects": subjects, "book": book}
        else:
            books = BookDescription.objects.filter(
                Q(name__icontains=query) | Q(author__icontains=query)
                | Q(description__icontains=query) | Q(department__name__icontains=query)
                | Q(subject__name__icontains=query)
            )

            context = {"base": base, "semesters": semesters, "departments": departments,
                    "subjects": subjects, "books": books}
    else:
        context = {"base": base, "semesters": semesters, "departments": departments, "subjects": subjects}
    return render(request, "book_details.html", context)


@login_required
def details_by_num(request, num):
    """This will show the book's description based on the id"""
    if UserProfile.objects.get(user=request.user).entity != 'staff':
        return redirect('/home/')
    book = BookDescription.objects.get(id=num)
    base = get_base(request)
    book_tx = Transaction.objects.filter(book__details=book).order_by('-id')
    total_stock = len(list(Book.objects.filter(details=book)))
    available_nos = len(list(Book.objects.filter(details=book, available=True)))
    if available_nos > 0:
        available = available_nos
    else:
        available = False
    context = {"book": book, "base": base, "semesters": semesters, "available": available,
                "total_stock": total_stock, "departments": departments, "subjects": subjects, "book_tx": book_tx}

    return render(request, "book_details_num.html", context)


@login_required
def add_books(request):
    """ This method will let the admins add books to the database """
    base = get_base(request)
    if UserProfile.objects.get(user=request.user).entity != 'staff':
        return redirect('/home/')

    if request.method == "POST":
        book_name = request.POST.get("book_name")
        book_author = request.POST.get("book_author")
        book_description = request.POST.get("book_description")

        book_number_init = int(request.POST.get("book_number_init"))
        book_number_end = int(request.POST.get("book_number_end"))

        initial_stock = (book_number_end - book_number_init)+1

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

    context = {"departments": departments, "semesters": semesters,
                "subjects": subjects, "base": base}
    return render(request, "add_books.html", context)


@login_required
def issue(request):
    """ This method will allow admin to issue books to the student """
    base = get_base(request)
    if UserProfile.objects.get(user=request.user).entity != 'staff':
        return redirect('/home/')

    if request.method == "POST":
        book_number = request.POST.get("book_number")
        library_card_num = request.POST.get("library_card_num")

        book = Book.objects.get(book_number=book_number)
        if book.available == False:
            context = {"book": book, "available": False, "base": base, "semesters": semesters,
                        "departments": departments, "subjects": subjects}
            return render(request, "issue_confirm.html", context)

        student = Student.objects.get(libcard=library_card_num)
        context = {"book": book, "available": True, "student": student, "base": base, "semesters": semesters,
                    "departments": departments, "subjects": subjects}
        return render(request, "issue_confirm.html", context)

    return render(request, "issue.html", {"base": base, "semesters": semesters,
                "departments": departments, "subjects": subjects})


@login_required
def issue_confirm(request):
    """ This method will show details about the book and student and confirm the issue """
    base = get_base(request)
    if UserProfile.objects.get(user=request.user).entity != 'staff':
        return redirect('/home/')

    if request.method == "POST":
        book_number = request.POST.get("book_number")
        libcard = request.POST.get("libcard")

        book = Book.objects.get(book_number=book_number)
        student = Student.objects.get(libcard=libcard)

        staff = Staff.objects.get(userprofile__user=request.user)

        Transaction.objects.create(staff=staff, student=student, book=book, issued=True, issue_time=datetime.datetime.now())
        book.available = False
        book.save()
        return redirect("/books/issue/")


@login_required
def return_book(request):
    """ This method will allow admin to take books back from students """
    base = get_base(request)
    if UserProfile.objects.get(user=request.user).entity != 'staff':
        return redirect('/home/')

    if request.method == "POST":
        book_number = request.POST.get("book_number")
        library_card_num = request.POST.get("library_card_num")

        book = Book.objects.get(book_number=book_number, available=False)
        student = Student.objects.get(libcard=library_card_num)
        tx_detail = Transaction.objects.get(book=book, student=student, issued=True, returned=False)
        context = {"book": book, "student": student, "tx_detail": tx_detail, "base": base, "semesters": semesters,
                    "departments": departments, "subjects": subjects}
        return render(request, "return_confirm.html", context)

    return render(request, "return.html", {"base": base, "semesters": semesters,
                "departments": departments, "subjects": subjects})


@login_required
def return_confirm(request):
    """ This method will show details about the book and student and confirm the return """
    base = get_base(request)
    if UserProfile.objects.get(user=request.user).entity != 'staff':
        return redirect('/home/')

    if request.method == "POST":
        book_number = request.POST.get("book_number")
        libcard = request.POST.get("libcard")

        book = Book.objects.get(book_number=book_number)
        student = Student.objects.get(libcard=libcard)

        tx = Transaction.objects.get(student=student, book=book, issued=True, returned=False)

        tx.returned = True
        tx.return_time = datetime.datetime.now()

        tx.save()
        book.available = True
        book.save()

        return redirect("/books/return/")
