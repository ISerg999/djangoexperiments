from django.db import models

from app.models.tasks import Tasks


class PartTasks(models.Model):
    """
    Части выполняемого задания.
    """
    frame_date = models.DateTimeField() # Дата начала выполнения части задачи.
    frame_time = models.DurationField(default=0) # Длительность части задачи.
    description = models.TextField(null=True) # Описание выполнения части задачи.
    # Ссылка на задачку к которой принадлежит часть выполняемого задания.
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
