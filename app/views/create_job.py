from datetime import datetime, timezone
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from app.models import ProgressJob, Tasks


def create_job(request: HttpRequest, id_task: int):
    part_task_html = {
        'id': 0,
        'description': '',
        'description_err': '',
        'is_frame_time': False,
        'frame_time': None,
        'frame_time_err': '',
    }

    if request.method == 'POST':
        part_task_html['description'] = request.POST.get('description', '')
        is_error, description_err, _, _ = ProgressJob.validate_job_for_html(part_task_html)
        part_task_html['description_err'] = description_err
        if not is_error:
            ProgressJob.test_and_continue(id_task, True)
            progress = ProgressJob()
            progress.frame_date = datetime.now(timezone.utc)
            progress.description = part_task_html['description']
            progress.task = Tasks.get_task(id_task)
            if progress.task.job_status < 0:
                progress.task.job_status = 0
                progress.task.save()
            progress.save()
            return HttpResponseRedirect(f'/view/task/{id_task}')

    html_title = 'Создание работы'
    html_header = 'Создание новой работы'
    return render(request, 'edit_job.html', {
        'html_title': html_title,
        'html_header': html_header,
        'part_task_html': part_task_html,
    })