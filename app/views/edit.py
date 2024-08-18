from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from ..models.person import Person


def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == 'POST':
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
