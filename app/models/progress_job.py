from django.db import models

from app.models.tasks import Tasks


class ProgressJob(models.Model):
    """
    Модель выполняемых заданий.
    """
    # Дата начала выполнения фрагмента задания.
    frame_date = models.DateTimeField()
    # Длительность фрагмента задания.
    frame_time = models.DurationField(null=True)
    # Описание действий в данном фрагменте задания.
    description = models.TextField()
    # Ссылка на задание к которой принадлежит текущий выполняемый фрагмент.
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    @staticmethod
    def validate_job_for_html(part_task_html: dict) -> tuple:
        """
        Валидация полей description и frame_time
        """
        is_error = False
        description_err = ''
        frame_time_err = ''

        if (part_task_html['description'] is None) or (len(part_task_html['description']) == 0):
            description_err = 'Описание задания не должно быть пустым!'
            is_error = True
        if part_task_html['frame_time'] is not None:
            if part_task_html['frame_time'] <= 0:
                frame_time_err = 'Продолжительность выполнения части задания должно быть положительным значением!'
                is_error = True
        return is_error, description_err, frame_time_err
