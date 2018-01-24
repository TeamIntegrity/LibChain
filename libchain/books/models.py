from django.db import models

# Importing models from department app
from department.models import Department, Subject, Semester


class BookDescription(models.Model):
    """This class will hold the description of the books"""
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    initial_stock = models.IntegerField()
    available_stock = models.IntegerField()

    department = models.ManyToManyField(Department)
    subject = models.ManyToManyField(Subject)
    semester = models.ManyToManyField(Semester)

    def __str__(self):
        """To represent the objects name in the admin panel"""
        return '{}'.format(self.name)



class Book(models.Model):
    """This class will hold the book details specific to one book"""
    details = models.ForeignKey(BookDescription, on_delete=models.CASCADE)
    book_number = models.IntegerField()

    def __str__(self):
        """To represent the objects name in the admin panel"""
        return '{} {}'.format(self.book_number, self.details.name)
