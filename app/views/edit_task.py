from django.http import HttpRequest, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from app.models import Tasks


def edit_task(request: HttpRequest, id_task: int):
    task = Tasks.get_task(id_task)
    if task is None:
        return HttpResponseNotFound("Заявки с заданным номером не существует!")

    task_html = {
        'id': task.id,
        'code': task.code,
        'code_err': '',
        'description': task.description,
        'description_err': '',
        'approximate_date': task.approximate_date,
        'approximate_date_err': '',
    }

    if request.method == 'POST':
        task_html['code'] = request.POST.get('code', '')
        task_html['description'] = request.POST.get('description', '')
        task_html['approximate_date'] = request.POST.get('approximate_date', None)
        is_error, code_err, description_err, approximate_date_err, approximate_date =(
            Tasks.validate_task_for_html(task_html))
        if not is_error:
            task.code = task_html['code']
            task.description = task_html['description']
            if task_html['approximate_date'] is not None:
                task.approximate_date = approximate_date
            task.save()
            return HttpResponseRedirect(f'/view/task/{id_task}')

    html_title = 'Редактирование заявки'
    html_header = 'Редактирование заявки заявки'
    return render(request, 'edit_task.html', {
        'html_title': html_title,
        'html_header': html_header,
        'task_html': task_html,
    })
