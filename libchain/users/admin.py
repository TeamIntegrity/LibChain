from django.contrib import admin
from .models import UserProfile, Student, Staff

admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Staff)
