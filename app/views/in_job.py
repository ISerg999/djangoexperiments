from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

from app.models import Tasks


def in_job(request: HttpRequest):
    # tasks = Tasks.get_in_job()
    # paginator = Paginator(tasks, 10)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    # ------------------------------------------------------------------------------------------------------------------
    page_obj = {}
    # ------------------------------------------------------------------------------------------------------------------
    return render(request, 'in_job.html', {'tasks': page_obj})
