from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1>Index</h1>")


def about(request):
    return HttpResponse("<h1>About</h1>")


def user(request):
    return HttpResponse("<h1>User</h1>")


def json(request):
    return JsonResponse({"name": "Владислав", "age": "33"})
