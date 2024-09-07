from django.db import models

from app.models.tasks import Tasks


class ProgressJob(models.Model):
    """
    Модель выполняемых заданий.
    """
    # Дата начала выполнения фрагмента задания.
    frame_date = models.DateTimeField()
    # Длительность фрагмента задания.
    frame_time = models.DurationField(default=0)
    # Описание действий в данном фрагменте задания.
    description = models.TextField(null=True)
    # Ссылка на задание к которой принадлежит текущий выполняемый фрагмент.
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

