from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponsePermanentRedirect


# Create your views here.

def index(request):
    return render(request, "index.html")


def home(request):
    return HttpResponsePermanentRedirect("/")


def about(request):
    return render(request, "about.html")


def user(request, name: str = "Undefined", age: int = 16):
    data = {"name": name, "age": age}
    return render(request, "user.html", context=data)


def json(request, name: str = "Undefined", age: int = 16):
    return JsonResponse({"name": name, "age": age})
