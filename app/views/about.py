from django.http import HttpRequest
from django.shortcuts import render

def about(request: HttpRequest):
    return render(request, 'about.html')