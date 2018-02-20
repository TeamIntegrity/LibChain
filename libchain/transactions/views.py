from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from api.views import get_base, get_vars

from users.models import UserProfile, Student

from transactions.models import Transaction


# Global variables to be used in each methods
semesters, departments, subjects = get_vars()


@login_required
def transaction(request, type):
    """This will return the transaction detail table for
        specific users and can be filtered by the type
    """
    base = get_base(request)
    if type == "all":
        userprofile = UserProfile.objects.get(user=request.user)
        try:
            student = Student.objects.get(userprofile=userprofile)
        except:
            student = None

        if student != None:
            tx_details = Transaction.objects.filter(student=student).order_by('-id')
        else:
            return redirect("/")

        context = {"tx_details": tx_details, "base": base, 'semesters': semesters,
        'departments': departments, 'subjects': subjects}
        return render(request, "tx_detail.html", context)



def tx_detail(request, hash):
    """This function will return the transaction detail based on the tx_hash"""
    pass
