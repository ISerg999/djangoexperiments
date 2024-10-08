from datetime import datetime

from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render

from app.models import Tasks


def view_task(request: HttpRequest, id_task: int):
    task, parts_task, is_job = Tasks.get_task_full(id_task)
    if task is None:
        return HttpResponseNotFound()
    job_staus = Tasks.get_name_job_status(task.job_status)
    closing_status = Tasks.get_name_closing_status(task.closing_status)
    return render(request, 'view_task.html', {
        'task': task,
        'parts_task': parts_task,
        'is_job': is_job,
        'job_staus': job_staus,
        'closing_status': closing_status,
    })
