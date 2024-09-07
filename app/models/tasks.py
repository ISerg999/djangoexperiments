from django.db import models
from datetime import datetime

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
