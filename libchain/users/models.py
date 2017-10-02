from django.db import models
from django.contrib.auth.models import User

from department.models import Department, Semester



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
    #name = models.CharField(max_length=100)
    phone = models.BigIntegerField(blank=True, null=True)
    entity = models.CharField(choices=ENTITY, max_length=100, default='student')

    def __str__(self):
        """To represent the objects name in the admin panel"""
        return '{} {}'.format(self.user.first_name, self.user.last_name)



class Student(models.Model):
    """This model class will hold the data specific to students only"""

    BRANCH = (
        ('COMPUTER SCIENCE AND ENGINEERING', 'COMPUTER SCIENCE AND ENGINEERING'),
        ('ELECTRONICS AND TELECOMMUNICATIONS', 'ELECTRONICS AND TELECOMMUNICATIONS'),
        ('ELECTRICAL AND ELCETRONICS ENGINEERING', 'ELECTRICAL AND ELCETRONICS ENGINEERING'),
        ('MECHANICAL ENGINEERING', 'MECHANICAL ENGINEERING'),
        ('CIVIL ENGINEERING', 'CIVIL ENGINEERING'),
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
    #branch = models.CharField(max_length=200, choices=BRANCH, blank=True, null=True)
    department_name = models.ForeignKey(Department, blank=True, null=True)
    #sem = models.CharField(max_length=1, choices=SEM, blank=True, null=True)
    semester = models.ForeignKey(Semester, blank=True, null=True, default=None)
    libcard = models.IntegerField(blank=True, null=True)

    def __str__(self):
        """To represent the objects name in the admin panel"""
        return '{} {}'.format(self.userprofile.user.first_name,
                                self.userprofile.user.last_name)



class Staff(models.Model):
    """This model class will store details specific to staff only"""
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
