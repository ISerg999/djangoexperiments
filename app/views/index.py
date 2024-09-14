from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

from app.models import Tasks


def index(request: HttpRequest):
    """
    Вывод списка заданий находящихся в работе.
    """
    tasks = Tasks.get_in_job()
    if tasks:
        paginator = Paginator(tasks, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else:
        page_obj = None
    return render(request, 'index.html', {'page_obj': page_obj})
