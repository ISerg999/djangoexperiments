import datetime
from datetime import timedelta

from django.shortcuts import render

from app.models import Tasks


#from app.models.product import Product


def index(request):
    str_from_date = request.POST.get('from_date')
    str_to_date = request.POST.get('to_date')
    if str_from_date:
        from_date = datetime.datetime.strptime(str_from_date, '%y-%m-%dT%H:%M')
    else:
        from_date = datetime.datetime.today() + timedelta(days=-datetime.datetime.today().weekday())
        from_date = datetime.datetime(from_date.year, from_date.month, from_date.day, 0, 0, 0)
    if str_to_date:
        to_date = datetime.datetime.strptime(str_to_date, '%y-%m-%dT%H:%M')
    else:
        to_date = datetime.datetime.today() + timedelta(days=1)
        to_date = datetime.datetime(to_date.year, to_date.month, to_date.day, 0, 0, 0)

    return render(request, 'index.html', {
        'is_all_tasks': Tasks.is_not_empty(),
        'from_date': from_date,
        'to_date': to_date,
        'tasks': Tasks.get_for_date(from_date, to_date),
    })
