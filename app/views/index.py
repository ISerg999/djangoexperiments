from django.shortcuts import render
from ..models.person import Person

def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})
