from django.shortcuts import render
from django.http import HttpResponse

def home(requests):
    """This is the home page functions"""
    return HttpResponse("This is the home page!")
