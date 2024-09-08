from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import models
from datetime import datetime, timedelta


class Tasks(models.Model):
    """
    Модель выполняемых заданий.
    """
    # Код задания или пустое значение.
    code = models.CharField(default='', max_length=20)
    # Описание задания.
    description = models.TextField()
    # Дата принятия задания.
    accept_date = models.DateTimeField()
    # Предполагаемая дата выполнения задания или null.
    approximate_date = models.DateTimeField(null=True)
    # Статус выполнения задания: -1 - принято, но не начато, 0 - в работе, 1 - закончено
    job_status = models.SmallIntegerField(default=-1)
    # Статус закрытия задания: -1 - не смог выполнить, 0 - отменено, 1 - выполнил
    closing_status = models.SmallIntegerField(default=0)


    @staticmethod
    def validate_task_for_html(code: str, description: str, approximate_date: str, id_task: int) -> tuple:
        """
        Валидация для создания новой заявки и редактирования заявки.
        code - код заявки
        description - описание заявки
        approximate_date - предпологаемая дата завершения заявки
        id_task - для создания заявки имеет значение 0, для редактирования должно иметь знаяения id заявки
        """
        is_error = False
        get_id = Tasks.get_id_code(code)
        if (get_id > 0) and (get_id != id_task):
            code_err = 'Заявка с таким кодом уже существует!'
            is_error = True
        else:
            code_err = ''
        if (description is not None) and (len(description) > 0):
            description_err = ''
        else:
            description_err = 'Описание задания не должно быть пустым!'
            is_error = True
        if (approximate_date is not None) and (len(approximate_date) > 0):
            approximate_date = datetime.strptime(approximate_date, '%Y-%m-%dT%H:%M')
            if approximate_date > datetime.now() + timedelta(minutes=1):
                approximate_date_err = ''
            else:
                approximate_date_err = 'Дата окончания задания должна быть больше текущей даты!'
                is_error = True
        else:
            approximate_date = None
            approximate_date_err = ''
        return is_error, code_err, description_err, approximate_date_err, approximate_date

    @staticmethod
    def get_id_code(code: str) -> int:
        """
        Проверяет существование заявки с заданным кодом. При возвращении -1 указывает, что кода нет.
        """
        if (code is not None) and (len(code) > 0):
            try:
                task = Tasks.objects.get(code=code)
                return task.id
            except ObjectDoesNotExist:
                return -1
            except MultipleObjectsReturned:
                print(f"Ошибка в базе. Количество заданий с кодом = {code} более 1.")
                return -2
        else:
            return -1

    @staticmethod
    def is_not_empty() -> bool:
        """
        Возвращает True, если в базе есть хоть одно задание, иначе False
        """
        return Tasks.objects.all().exists()

    @staticmethod
    def get_for_date(from_date: datetime, to_date: datetime):
        """
        Возвращает список заданий у которых дата создания, либо дата выполнения работ
        попадает в заданный промежуток времени.
        Если таких заданий нет, возвращает пустой список.
        """
        if (from_date is None) or (to_date is None):
            return []
        # TODO: Вернуть список заданий попадающих в заданный промежуток времени.
        return []
