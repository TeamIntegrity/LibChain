from django.shortcuts import render, redirect

from api.views import get_base, get_vars

# Importing Django's default User model class for users
from django.contrib.auth.models import User

# Importing search utility tool Q
from django.db.models import Q

from users.models import Student, UserProfile, Staff

from department.models import Department, Semester

# Register, Login and Logout views
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Importing from transactions app
from transactions.models import Transaction

# Global variables to be used in each methods
semesters, departments, subjects = get_vars()



def register(request):
    """This is the register function"""

    base = get_base(request)

    # After use submits its credentials
    if request.method=='POST':

        email = request.POST.get('email')
        rollno = request.POST.get('rollno')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        # Checks for missing form fieds
        if not email:
            message = "Please provide a valid email"
            return render(request, "login_error.html", {"message": message, "base": base, 'semesters': semesters,
            'departments': departments, 'subjects': subjects})

        if not password1 or not password2:
            message = "Passwords do not match"
            return render(request, "login_error.html", {"message": message, "base": base, 'semesters': semesters,
            'departments': departments, 'subjects': subjects})

        if not first_name:
            message = "Please provide your name"
            return render(request, "login_error.html", {"message": message, "base": base, 'semesters': semesters,
            'departments': departments, 'subjects': subjects})

        if not last_name:
            last_name = ""

        if not rollno:
            message = "Please provide your roll number"
            return render(request, "login_error.html", {"message": message, "base": base, 'semesters': semesters,
            'departments': departments, 'subjects': subjects})


        # Checks for invalid form fields
        invalid = []
        if "@" not in email or "." not in email:
            message = "Please provide a valid email."
            return render(request, "login_error.html", {"message": message, "base": base, 'semesters': semesters,
            'departments': departments, 'subjects': subjects})


        # Check for duplicate email
        try:
            already_user = User.objects.get(username=rollno)
        except:
            already_user = None

        if already_user != None:
            message = "The roll number entered already has an account"
            return render(request, "login_error.html", {"message":message, "base": base, 'semesters': semesters,
            'departments': departments, 'subjects': subjects})



        if password1==password2:

            # Creating a user on the platform
            user_created = User.objects.create_user(email=email, username=rollno,
                password=password1, first_name=first_name, last_name=last_name)

            userprofile = UserProfile()
            userprofile.user = user_created
            #userprofile.name = user_created.first_name +" "+ user_created.last_name
            userprofile.save()

            userprofile = UserProfile.objects.get(user=user_created)

            student = Student()
            student.userprofile = userprofile
            student.rollno = rollno
            student.save()

            user = authenticate(username=rollno, password=password1)

            # The user can be inactive
            if user.is_active:
                auth_login(request, user)
                return redirect('/home/')
            else:
                message = """The user is not active.
                            Kindly contact the administrator"""
                return render(request, 'login_error.html', {"message": message, "base": base, 'semesters': semesters,
                'departments': departments, 'subjects': subjects})

        else:
            message = "Passwords do not match"
            return render(request, "login_error.html", {"message": message, "base": base, 'semesters': semesters,
                            'departments': departments, 'subjects': subjects})

    return render(request, "register.html", {"base": base, 'semesters': semesters,
                    'departments': departments, 'subjects': subjects})



def login(request):
    """This is the login function"""
    base = get_base(request)

    # After the user enters the credentials
    if request.method=='POST':

        rollno = request.POST.get('rollno')
        password = request.POST.get('password')
        user = authenticate(username=rollno, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                entity = UserProfile.objects.get(user=user).entity
                if entity == "staff":
                    return redirect('/users/admin/dashboard/')
                else:
                    return redirect('/home/')
            else:
                message = """The user is not active.
                            Kindly contact the administrator"""
                return render(request, 'login_error.html', {"message": message, "base": base, 'semesters': semesters,
                'departments': departments, 'subjects': subjects})

        else:
            message = """The user could not be found.
                        Kindly ensure the email and
                        password entered are correct."""
            return render(request, 'login_error.html', {"message": message, "base": base, 'semesters': semesters,
            'departments': departments, 'subjects': subjects})

    return render(request, 'login.html', {"base": base, 'semesters': semesters,
    'departments': departments, 'subjects': subjects})



def logout(request):
    """This is the logout function"""

    # The user logs out
    auth_logout(request)
    return redirect('/home/')



def profile(request):
    """This function will show the user their profile details"""
    user = User.objects.get(id=request.user.id)
    base = get_base(request)

    userprofile = UserProfile.objects.get(user=user)

    if userprofile.entity == 'student':
        student = Student.objects.get(userprofile=userprofile)
        context = {"student": student, 'base': base, 'profile': 'student', 'semesters': semesters,
        'departments': departments, 'subjects': subjects}
    elif userprofile.entity == 'staff':
        staff = Staff.objects.get(userprofile=userprofile)
        context = {"staff": staff, 'base': base, 'profile': 'staff', 'semesters': semesters,
        'departments': departments, 'subjects': subjects}

    return render(request, "profile.html", context)



def edit(request):
    """This function will let the user edit their details"""
    base = get_base(request)

    userprofile = UserProfile.objects.get(user=request.user)

    if request.method=="POST":
        if userprofile.entity == 'student':
            student = Student.objects.get(userprofile=userprofile)
            branch = request.POST.get('branch')
            semester = request.POST.get('semester')
            libcard = request.POST.get('libcard')
            phone = request.POST.get('phone')

            if phone:
                userprofile.phone = phone
            userprofile.save()

            if branch:
                student.department_name = Department.objects.get(name=branch)
            if semester:
                student.semester = Semester.objects.get(semester=semester)
            if libcard:
                student.libcard = libcard
            student.save()
        else:
            pass

        return redirect("/users/profile/")

    if userprofile.entity == 'student':
        student = Student.objects.get(userprofile=userprofile)
        context = {"student": student, "base": base, "profile": "student", 'semesters': semesters,
        'departments': departments, 'subjects': subjects}
    elif userprofile.entity == 'staff':
        staff = Staff.objects.get(userprofile=userprofile)
        context = {"staff": staff, "base": base, "profile": "staff", 'semesters': semesters,
        'departments': departments, 'subjects': subjects}
    return render(request, "edit.html", context)



def dashboard(request):
    """ This method will render the dashboard for the admin """
    base = get_base(request)

    context = {'base': base, 'semesters': semesters, 'departments': departments, 'subjects': subjects}
    return render(request, "dashboard.html", context)



def student_details(request, libcard):
    """
    This will act as the link for the admins to find details about the student
    """

    base = get_base(request)

    try:
        student = Student.objects.get(libcard=libcard)
    except:
        return render(request, "error.html", {"message": "No user could be found with that card number", "base": base})

    tx_details = student.transaction_set.all()
    context = {"base": base, "student": student, "tx_details": tx_details, 'semesters': semesters,
    'departments': departments, 'subjects': subjects}
    return render(request, "student_details.html", context)


def student_search(request):
    """
    This will act as the link for the admins to find details about the student
    """
    base = get_base(request)

    if request.method == "POST":
        query = request.POST.get('query')

        if query.isdecimal():
            try:
                student = Student.objects.get(libcard=query)
            except:
                try:
                    student = Student.objects.get(rollno=query)
                    notfound = False
                except:
                    student = None
                    notfound = True
            context = {"base": base, "student": student, "notfound": notfound, 'semesters': semesters,
            'departments': departments, 'subjects': subjects}
        else:
            students = Student.objects.filter(
                Q(userprofile__user__first_name__icontains=query) |
                Q(userprofile__user__last_name__icontains=query)
                ).filter(userprofile__entity="student")

            context = {"base": base, "students": students, 'semesters': semesters,
            'departments': departments, 'subjects': subjects}
    else:
        context = {"base": base, 'semesters': semesters, 'departments': departments, 'subjects': subjects}
    return render(request, "student_search.html", context)
