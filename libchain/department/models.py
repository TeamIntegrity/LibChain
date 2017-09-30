from django.db import models

class Department(models.Model):
    """This will store the details about the departments"""
    name = models.CharField(max_length=200)



class Subject(models.Model):
    """This will store the subject names"""
    name = models.CharField(max_length=200)
