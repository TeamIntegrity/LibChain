from django.contrib import admin

from .models import Department, Subject, Semester

admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Semester)
