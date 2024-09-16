import datetime

from django.http import HttpRequest, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

from app.models import ProgressJob


def edit_job(request: HttpRequest, id_task: int, id_job: int):
    job = ProgressJob.get_job(id_job)
    if job is None:
        return HttpResponseNotFound("Такой работы не существует!")

    part_task_html = {
        'id': job.id,
        'description': job.description,
        'description_err': '',
        'is_frame_time': (job.frame_time is not None) and (job.frame_time > datetime.timedelta(0)),
        'frame_time': job.frame_time,
        'frame_time_err': '',
    }

    if request.method == 'POST':
        part_task_html['description'] = request.POST.get('description', '')
        if part_task_html['is_frame_time']:
            part_task_html['frame_time'] = request.POST.get('frame_time', '')
        is_error, description_err, frame_time_err, frame_time = ProgressJob.validate_job_for_html(part_task_html)
        part_task_html['description_err'] = description_err
        part_task_html['frame_time_err'] = frame_time_err
        if not is_error:
            job.description = part_task_html['description']
            job.frame_time = frame_time
            job.save()
            return HttpResponseRedirect(f'/view/task/{id_task}')

    html_title = 'Редактирование работы'
    html_header = 'Редактирование работы'
    return render(request, 'edit_job.html', {
        'html_title': html_title,
        'html_header': html_header,
        'part_task_html': part_task_html,
    })
