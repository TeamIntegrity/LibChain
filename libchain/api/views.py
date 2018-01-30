from django.shortcuts import render

from users.models import UserProfile, Student, Staff

from department.models import Semester, Subject, Department



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


def get_vars():
    """ This will return variables to be used in nav bar """

    semesters = Semester.objects.all()
    departments = Department.objects.all().order_by('name')
    subjects = Subject.objects.all().order_by('name')[:5]

    return (semesters, departments, subjects)
