from django.db import models

# Importing models from department app
from department.models import Department, Subject


class BookDescription(models.Model):
    """This class will hold the description of the books"""
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    initial_stock = models.IntegerField()
    available_stock = models.IntegerField()



class BookDepartmentSubject(models.Model):
    """This will define the relationship among books, departments and subjects"""
    book = models.ManyToManyField(BookDescription)
    department = models.ManyToManyField(Department)
    subject = models.ManyToManyField(Subject)
    semester = models.IntegerField()



class Book(models.Model):
    """This class will hold the book details specific to one book"""
    details = models.ForeignKey(BookDescription, on_delete=models.CASCADE)
    book_number = models.IntegerField()
