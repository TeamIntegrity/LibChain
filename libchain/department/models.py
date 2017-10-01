from django.db import models

class Department(models.Model):
    """This will store the details about the departments"""
    name = models.CharField(max_length=200)

    def __str__(self):
        """To represent the objects name in the admin panel"""
        return '{}'.format(self.name)



class Subject(models.Model):
    """This will store the subject names"""
    name = models.CharField(max_length=200)

    def __str__(self):
        """To represent the objects name in the admin panel"""
        return '{}'.format(self.name)
