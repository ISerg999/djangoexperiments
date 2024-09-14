from datetime import datetime

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from app.models import Tasks


def create_task(request: HttpRequest):
    task_html = {
        'id': 0,
        'code': '',
        'code_err': '',
        'description': '',
        'description_err': '',
        'approximate_date': None,
        'approximate_date_err': '',
    }

    if request.method == 'POST':
        task_html['code'] = request.POST.get('code', '')
        task_html['description'] = request.POST.get('description', '')
        task_html['approximate_date'] = request.POST.get('approximate_date', '')
        is_error, code_err, description_err, approximate_date_err, approximate_date =(
            Tasks.validate_task_for_html(task_html))
        task_html['code_err'] = code_err
        task_html['description_err'] = description_err
        task_html['approximate_date_err'] = approximate_date_err
        if not is_error:
            task = Tasks()
            task.code = task_html['code']
            task.description = task_html['description']
            task.accept_date = datetime.now()
            if task_html['approximate_date'] is not None:
                task.approximate_date = approximate_date
            task.save()
            return HttpResponseRedirect('/')

    html_title = 'Создание заявки'
    html_header = 'Создание новой заявки'
    return render(request, 'edit_task.html', {
        'html_title': html_title,
        'html_header': html_header,
        'task_html': task_html,
    })
