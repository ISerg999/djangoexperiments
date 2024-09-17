from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from app.models import ProgressJob, Tasks


def stop_task(request: HttpRequest, id_task: int):
    is_job = Tasks.get_count_part(id_task) > 0

    if request.method == 'POST':
        status_closing = int(request.POST.get('status_closing', 0))
        ProgressJob.test_and_continue(id_task, True)
        Tasks.close_task(id_task, status_closing)
        return HttpResponseRedirect(f'/view/task/{id_task}')

    return render(request, 'stop_task.html', {})
    # job = ProgressJob.get_in_job(id_task)
    # if job is not None:
    #     ProgressJob.set_frame_time(job)
    # return HttpResponseRedirect(f'/view/task/{id_task}')
