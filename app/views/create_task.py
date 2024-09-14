from datetime import datetime

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from app.models import Tasks


def create_task(request: HttpRequest):
    # if request.method == 'POST':
    #     code = request.POST.get('code', '')
    #     description = request.POST.get('description', '')
    #     approximate_date = request.POST.get('approximate_date', None)
    #     is_error, code_err, description_err, approximate_date_err, approximate_date =(
    #         Tasks.validate_task_for_html(code, description, approximate_date, 0))
    #     if not is_error:
    #         task = Tasks()
    #         task.code = code
    #         task.description = description
    #         task.accept_date = datetime.now()
    #         if approximate_date is not None:
    #             task.accept_date = approximate_date
    #         task.save()
    #         return HttpResponseRedirect('/')

    # if request.method == 'GET':
    #     code = ''
    #     code_err = ''
    #     description = ''
    #     description_err = ''
    #     approximate_date = None
    #     approximate_date_err = ''

    # ------------------------------------------------------------------------------------------------------------------
    code = ''
    code_err = ''
    description = ''
    description_err = ''
    approximate_date = None
    approximate_date_err = ''
    # ------------------------------------------------------------------------------------------------------------------
    html_title = 'Создание заявки'
    html_header = 'Создание новой заявки'
    return render(request, 'edit_task.html', {
        'html_title': html_title,
        'html_header': html_header,
        'id_task': 0,
        'code': code,
        'code_err': code_err,
        'description': description,
        'description_err': description_err,
        'approximate_date': approximate_date,
        'approximate_date_err': approximate_date_err,
    })
