from django.db import models

from app.models.status_task import StatusTask


class Tasks(models.Model):
    """
    Выполняемое задание.
    """
    code = models.CharField(null=True, max_length=20) # Код задачи или Null
    description = models.TextField() # Описание проблемы или самой задачи.
    status = models.ForeignKey(StatusTask, on_delete=models.SET_NULL, null=True) # Текущий статус задания.
    job_acceptance_date = models.DateTimeField() # Дата принятия задания в работу.
    # Предпологаемая дата выполнения, или Null, если дата выполнения не ограничина.
    approximate_date = models.DateTimeField(null=True)
    date_task = models.DateTimeField(null=True) # Дата завершения задания.
    is_periodic = models.BooleanField(default=False) # Определяет, переодически повторяющееся задание, или одноразовое.

    @staticmethod
    def is_not_empty():
        """
        Возвращает True, если в базе есть хоть одна заявка, иначе False
        """
        return Tasks.objects.all().exists()

    @staticmethod
    def get_for_date(from_date, to_date):
        """
        Возвращает список работ попадающих в заданный промежуток времени,
        если хоть она из дат равно None, возвращает пустой список.
        """
        if (from_date is None) or (to_date is None):
            return []
        # TODO: Вернуть список работ попадающих в заданный промежуток времени.
        return []
