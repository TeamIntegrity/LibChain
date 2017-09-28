from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    """This model class will hold additional details about the user
        that is common among all the user and can not be stored in
        the base User table.
    """

    ENTITY = (
        ('student', 'STUDENT'),
        ('librarian', 'LIBRARIAN'),
        ('faculty', 'FACULTY'),
        ('staff', 'STAFF'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField(blank=True, null=True)
    entity = models.CharField(choices=ENTITY, max_length=100, default='student')



class Student(models.Model):
    """This model class will hold the data specific to students only"""

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

    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    rollno = models.BigIntegerField()
    branch = models.CharField(max_length=10, choices=BRANCH, blank=True, null=True)
    sem = models.CharField(max_length=1, choices=SEM, blank=True, null=True)
    libcard = models.IntegerField(blank=True, null=True)



class Staff(models.Model):
    """This model class will store details specific to staff only"""
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
