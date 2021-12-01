from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    a=5
    b=2
    c=a+b
    return HttpResponse(c)
# Create your views here.
