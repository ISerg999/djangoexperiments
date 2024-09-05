import datetime
from datetime import timedelta

from django.http import HttpRequest, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render

from app.models import Tasks


def index(request: HttpRequest):
    if request.method == "POST":
        str_from_date = request.POST.get('from_date')
        str_to_date = request.POST.get('to_date')
        if (str_from_date is None) or (str_to_date is None):
            return HttpResponseBadRequest(HttpResponse("Ошибка в переданных датах!"))
        from_date = datetime.datetime.strptime(str_from_date, '%Y-%m-%dT%H:%M')
        to_date = datetime.datetime.strptime(str_to_date, '%Y-%m-%dT%H:%M')

    if request.method == "GET":
        from_date = datetime.datetime.today() + timedelta(days=-datetime.datetime.today().weekday())
        from_date = datetime.datetime(from_date.year, from_date.month, from_date.day, 0, 0, 0, 0)
        to_date = datetime.datetime.today() + timedelta(days=1)
        to_date = datetime.datetime(to_date.year, to_date.month, to_date.day, 0, 0, 0, 0)

    return render(request, 'index.html', {
        'is_all_tasks': Tasks.is_not_empty(),
        'from_date': from_date,
        'to_date': to_date,
        'tasks': Tasks.get_for_date(from_date, to_date),
    })
