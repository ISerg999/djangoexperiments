from django.urls import path, re_path
from .views import about, index, create_task, view_task, edit_task, create_job, pause_job, edit_job

urlpatterns = [
    path('stop/task/<int:id_task>', pause_job.pause_job),
    path('edit/task/<int:id_task>/job/<int:id_job>', edit_job.edit_job),
    path('pause/job/<int:id_task>', pause_job.pause_job),
    path('create/job/<int:id_task>', create_job.create_job),
    path('edit/task/<int:id_task>', edit_task.edit_task),
    path('view/task/<int:id_task>', view_task.view_task),
    path('create/task', create_task.create_task),
    path('about/', about.about, name='about'),
    path('', index.index, name='index'),
]
