from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponsePermanentRedirect


# Create your views here.

def index(request):
    return HttpResponse("<h1>Index</h1>")


def about(request):
    return HttpResponse("<h1>About</h1>")


def user(request):
    return HttpResponse("<h1>User</h1>")


def json(request, name: str = "Undefined", age: int = 16):
    return JsonResponse({"name": name, "age": age})


def home(request):
    return HttpResponsePermanentRedirect("/")
