from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponsePermanentRedirect
from .forms import UserForm

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привет: {name}, твой возраст: {age}</h2>")
    else:
        user_form = UserForm()
        return render(request, "index.html", {"form": user_form})


def home(request):
    return HttpResponsePermanentRedirect("/")


def about(request):
    return render(request, "about.html")


def user(request, name: str = "Undefined", age: int = 16):
    data = {"name": name, "age": age}
    return render(request, "user.html", context=data)


def json(request, name: str = "Undefined", age: int = 16):
    return JsonResponse({"name": name, "age": age})
