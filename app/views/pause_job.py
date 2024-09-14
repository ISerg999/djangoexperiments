from django.http import HttpRequest, HttpResponseRedirect

from app.models import ProgressJob


def pause_job(request: HttpRequest, id_task: int):
    job = ProgressJob.get_in_job(id_task)
    ProgressJob.set_frame_time(job)
    return HttpResponseRedirect(f'/view/task/{id_task}')
