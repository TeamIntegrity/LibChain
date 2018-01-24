from django.shortcuts import render

from users.models import UserProfile, Student, Staff



def get_base(request):
    """ This method will render correct base template according to the user type """

    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except:
        return "base.html"

    if userprofile.entity == "student":
        base = "base_student.html"
    elif userprofile.entity == "staff":
        base = "base_staff.html"
    else:
        base = "base.html"

    return base
