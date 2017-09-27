from django.db import models


class BookDescription(models.Model):
    """This class will hold the description of the books"""

    BRANCH = (
        ('cse', 'COMPUTER SCIENCE AND ENGINEERING'),
        ('et&t', 'ELECTRONICS AND TELECOMMUNICATIONS'),
        ('eee', 'ELECTRICAL AND ELCETRONICS ENGINEERING'),
        ('mech', 'MECHANICAL ENGINEERING'),
        ('civil', 'CIVIL ENGINEERING'),
    )
    SEM = (
        ('1', '1st SEMESTER'),
        ('2', '2nd SEMESTER'),
        ('3', '3rd SEMESTER'),
        ('4', '4th SEMESTER'),
        ('5', '5th SEMESTER'),
        ('6', '6th SEMESTER'),
        ('7', '7th SEMESTER'),
        ('8', '8th SEMESTER'),
    )

    name = models.CharField(max_length=200)
    branch = models.CharField(choices=BRANCH, max_length=20)
    sem = models.CharField(choices=SEM, max_length=1)
    subject = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    initial_stock = models.IntegerField()
    available_stock = models.IntegerField()



class Book(models.Model):
    """This class will hold the book details specific to one book"""
    description = models.ForeignKey(BookDescription, on_delete=models.CASCADE)
    book_number = models.IntegerField()
    publish_year = models.IntegerField()
