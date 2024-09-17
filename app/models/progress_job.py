from datetime import datetime, timezone, timedelta

from django.core.exceptions import ObjectDoesNotExist
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
        frame_time = timedelta(0)

        if (part_task_html['description'] is None) or (len(part_task_html['description']) == 0):
            description_err = 'Описание задания не должно быть пустым!'
            is_error = True
        if part_task_html['is_frame_time']:
            hours,minutes,seconds = map(float, part_task_html['frame_time'].split(':'))
            frame_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            if frame_time.total_seconds() <= 0:
                frame_time_err = 'Продолжительность выполнения части задания должно быть положительным значением!'
                is_error = True
        return is_error, description_err, frame_time_err, frame_time

    @staticmethod
    def get_in_job(id_task: int):
        """
        Возвращает подзадачу по заданому id_task задания которая в работе.
        Если не находит, возвращает None.
        """
        part_tasks = ProgressJob.objects.filter(task_id=id_task, frame_time__exact=None)
        return part_tasks[0] if len(part_tasks) > 0 else None

    @staticmethod
    def set_frame_time(job):
        """
        Приостанавливает текущее выполнение задания.
        """
        if job is not None:
            job.frame_time = datetime.now(timezone.utc) - job.frame_date
            job.save()

    @staticmethod
    def get_job(id_job: int):
        """
        Возвращает содержимое части выполняемой работы.
        """
        try:
            job = ProgressJob.objects.get(id=id_job)
            return job
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def test_and_continue(id_task: int, is_continue: bool) -> bool:
        """
        Проверяет есть ли не остановленная подзадача. Результат возвращает.
        Если is_continue == True, то закрывает не остановленную подзадачу.
        """
        job_obj = ProgressJob.get_in_job(id_task)
        if job_obj is None:
            return False
        if is_continue:
            ProgressJob.set_frame_time(job_obj)
        return True
