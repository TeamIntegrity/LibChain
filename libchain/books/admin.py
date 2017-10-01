from django.contrib import admin
from .models import Book, BookDescription, BookDepartmentSubject

admin.site.register(Book)
admin.site.register(BookDescription)
admin.site.register(BookDepartmentSubject)
