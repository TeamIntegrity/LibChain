from django.contrib import admin
from .models import Book, BookDescription

admin.site.register(Book)
admin.site.register(BookDescription)
