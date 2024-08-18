from django.http import HttpResponseRedirect
from ..models.person import Person


def create(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/")

