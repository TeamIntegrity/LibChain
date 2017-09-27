from django.db import models
from users.models import Student, Staff
from books.models import Book

class Transaction(models.Model):
    """Will hold the transaction details"""

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    issued = models.BooleanField(default=False)
    issue_time = models.DateTimeField()

    returned = models.BooleanField(default=False)
    return_time = models.DateTimeField()

    hash = models.CharField(max_length=200)
