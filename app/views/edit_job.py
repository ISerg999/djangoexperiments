from django.http import HttpRequest
from django.shortcuts import render


def edit_job(request: HttpRequest, id_task: int, id_job: int):
    return render(request, 'edit_job.html', {})
