from datetime import datetime

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from app.models import TasksJob


def create_job(request: HttpRequest, id_task: int):
    # if request.method == 'POST':
    #     description = request.POST.get('description', '')
    #     is_error, description_err, duration_err = TasksJob.validate_job_for_html(description, None)
    #     if not is_error:
    #         job = TasksJob()
    #         job.description = description
    #         job.start_date = datetime.now()
    #         job.task = id_task
    #         job.save()
    #         return HttpResponseRedirect(f'/view/task/{id_task}')

    if request.method == 'GET':
        description = ''
        description_err = ''

    # ------------------------------------------------------------------------------------------------------------------
    description = ''
    description_err = ''
    # ------------------------------------------------------------------------------------------------------------------
    html_title = 'Создание работы'
    html_header = 'Создание новой работы'
    return render(request, 'edit_job.html', {
        'html_title': html_title,
        'html_header': html_header,
        'job_id': 0,
        'description': description,
        'description_err': description_err,
        'is_duration': False,
        'duration': None,
        'duration_err': '',
    })