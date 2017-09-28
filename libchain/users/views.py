from django.shortcuts import render, redirect

# Importing Django's default User model class for users
from django.contrib.auth.models import User

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
            already_user = User.objects.get(email=email)
        except:
            already_user = None

        if already_user != None:
            message = "The email entered already has an account"
            return render(request, "login_error.html", {"message":message})



        if password1==password2:

            # Creating a user on the platform
            user_created = User.objects.create_user(email=email, username=rollno,
                password=password1, first_name=first_name, last_name=last_name)

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
    pass

def edit(request):
    """This function will let the user edit their details"""
    pass

def user_detail(request):
    """This is the admin function which will show the details
        about all the users
    """
    pass
