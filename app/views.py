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


def postuser(request):
    name = request.POST.get("name", "Безимянный")
    age = request.POST.get("age", 16)
    langs = request.POST.getlist("languages", ["python",]) # Также с select формы
    return HttpResponse(f"""
        <p>Имя: {name}  Возраст: {age}</p>
        <p>Языки: {langs}</p>
    """)


def json(request, name: str = "Undefined", age: int = 16):
    return JsonResponse({"name": name, "age": age})
