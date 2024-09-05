from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect

from app.models import Tasks
from app.views.forms.form_create_task import TasksCreateForm


def create_tasks(request):
    if request.method == 'POST':
        task = Tasks()
        task.code = request.POST.get('code')
        task.description = request.POST.get('description')
        task.status = 1 # TODO: Статус Подзадача создана.
        task.job_acceptance_date = datetime.now()
        approximate_date = request.POST.get('approximate_date')
        task.is_periodic = request.POST.get('is_periodic')
        if (approximate_date is not None) and (len(approximate_date) > 0) and request.POST.get('selected_periodic') and not task.is_periodic:
            task.approximate_date = datetime.strptime(approximate_date, '%Y-%m-%dT%H:%M')
        # task.save()
        return HttpResponseRedirect('/')
    task_form = TasksCreateForm()
    return render(request, 'create_tasks.html', {'task_form': task_form})
