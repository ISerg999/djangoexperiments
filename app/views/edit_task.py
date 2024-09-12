from django.http import HttpRequest, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render

from app.models import Tasks


def edit_task(request: HttpRequest, id_task: int):
    task = Tasks.get_task(id_task)
    if task is None:
        return HttpResponseNotFound("Заявки с заданным номером не существует!")

    if request.method == 'POST':
        code = request.POST.get('code', '')
        description = request.POST.get('description', '')
        approximate_date = request.POST.get('approximate_date', None)
        is_error, code_err, description_err, approximate_date_err, approximate_date =(
            Tasks.validate_task_for_html(code, description, approximate_date, id_task))
        if not is_error:
            task.code = code
            task.description = description
            if approximate_date is not None:
                task.accept_date = approximate_date
            task.save()
            return HttpResponseRedirect(f'/view/task/{id_task}')

    if request.method == 'GET':
        code = task.code
        code_err = ''
        description = task.description
        description_err = ''
        approximate_date = task.approximate_date
        approximate_date_err = ''

    html_title = 'Редактирование заявки'
    html_header = 'Редактирование заявки заявки'
    return render(request, 'edit_task.html', {
        'html_title': html_title,
        'html_header': html_header,
        'code': code,
        'code_err': code_err,
        'description': description,
        'description_err': description_err,
        'approximate_date': approximate_date,
        'approximate_date_err': approximate_date_err,
    })
