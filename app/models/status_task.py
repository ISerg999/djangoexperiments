from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class StatusTask(models.Model):
    """
    Таблица справочник статуса задачи.
    """
    status = models.CharField(max_length=120) # Статус задачи.

    @staticmethod
    def get_list_status():
        """
        Возвращает весь список статусов задачи.
        """
        status_all = StatusTask.objects.values_list()
        return status_all

    @staticmethod
    def get_list_end_status():
        """
        Возвращает список статусов закрытия задачи.
        """
        # TODO: Получить список статусов закрытия задачи.
        return []

    @staticmethod
    def get_status_for_id(id: int):
        """
        Возвращает название статуса по его id.
        Если статус не найден, возвращает None.
        """
        try:
            status = StatusTask.objects.get(id=id)
        except ObjectDoesNotExist:
            return None
        return status.status

    @staticmethod
    def insert_all_status(is_clear: bool = False):
        """
        Заполнение справочника статуса данными.
        Если is_clear == True, то таблица очищается, после заполняется,
        иначе заполняется, если таблица пустая
        """
        if is_clear:
            # TODO: Очистить справочник.
            pass
        else:
            # TODO: Проверить пустой справочник или нет. Если не пустой, то выйти.
            pass
        # TODO: Загрузить список с данными справочника.
        # TODO: Заполнить таблицу данными из загруженного списка.
        # StatusTask.objects.create(id=1, status='...')
        pass

