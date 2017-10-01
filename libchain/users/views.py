from django.shortcuts import render, redirect

# Importing Django's default User model class for users
from django.contrib.auth.models import User

from users.models import Student, UserProfile

from department.models import Department

# Register, Login and Logout views
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout



def register(request):
    """This is the register function"""

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
            return render(request, "login_error.html", {"message": message})

        if not password1 or not password2:
            message = "Passwords do not match"
            return render(request, "login_error.html", {"message": message})

        if not first_name:
            message = "Please provide your name"
            return render(request, "login_error.html", {"message": message})

        if not last_name:
            last_name = ""

        if not rollno:
            message = "Please provide your roll number"
            return render(request, "login_error.html", {"message": message})


        # Checks for invalid form fields
        invalid = []
        if "@" not in email or "." not in email:
            message = "Please provide a valid email."
            return render(request, "login_error.html", {"message": message})


        # Check for duplicate email
        try:
            already_user = User.objects.get(username=rollno)
        except:
            already_user = None

        if already_user != None:
            message = "The roll number entered already has an account"
            return render(request, "login_error.html", {"message":message})



        if password1==password2:

            # Creating a user on the platform
            user_created = User.objects.create_user(email=email, username=rollno,
                password=password1, first_name=first_name, last_name=last_name)

            userprofile = UserProfile()
            userprofile.user = user_created
            userprofile.name = user_created.first_name +" "+ user_created.last_name
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
                return render(request, 'login_error.html', {"message": message})

        else:
            message = "Passwords do not match"
            return render(request, "login_error.html", {"message": message})

    return render(request, "register.html")



def login(request):
    """This is the login function"""

    # After the user enters the credentials
    if request.method=='POST':

        rollno = request.POST.get('rollno')
        password = request.POST.get('password')
        user = authenticate(username=rollno, password=password)

        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect('/home/')
            else:
                message = """The user is not active.
                            Kindly contact the administrator"""
                return render(request, 'login_error.html', {"message": message})

        else:
            message = """The user could not be found.
                        Kindly ensure the email and
                        password entered are correct."""
            return render(request, 'login_error.html', {"message": message})

    return render(request, 'login.html')



def logout(request):
    """This is the logout function"""

    # The user logs out
    auth_logout(request)
    return redirect('/users/login/')



def profile(request):
    """This function will show the user their profile details"""
    user = User.objects.get(id=request.user.id)

    userprofile = UserProfile.objects.get(user=user)
    student = Student.objects.get(userprofile=userprofile)
    context = {"student": student}

    return render(request, "profile.html", context)



def edit(request):
    """This function will let the user edit their details"""

    user = User.objects.get(id=request.user.id)
    userprofile = UserProfile.objects.get(user=user)
    student = Student.objects.get(userprofile=userprofile)

    if request.method=="POST":
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
            student.sem = semester
        if libcard:
            student.libcard = libcard
        student.save()

        return redirect("/users/profile/")

    context = {"student": student}
    return render(request, "edit.html", context)



def user_detail(request):
    """This is the admin function which will show the details
        about all the users
    """
    pass
