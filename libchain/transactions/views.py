from django.shortcuts import render, redirect

from users.models import UserProfile, Student

from transactions.models import Transaction


def transaction(request, type):
    """This will return the transaction detail table for
        specific users and can be filtered by the type
    """
    if type == "all":
        userprofile = UserProfile.objects.get(user=request.user)
        try:
            student = Student.objects.get(userprofile=userprofile)
        except:
            student = None

        if student != None:
            tx_details = Transaction.objects.filter(student=student)
        else:
            return redirect("/")

        context = {"tx_details": tx_details}
        return render(request, "tx_detail.html", context)



def tx_detail(request, hash):
    """This function will return the transaction detail based on the tx_hash"""
    pass
