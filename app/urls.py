from django.urls import path, re_path
from .views import about
from .views import index
from .views import create_task
from .views import in_job
from .views import view_task
from .views import edit_task

urlpatterns = [
    path('create/job/<int:id_task>', edit_task.edit_task),
    path('edit/task/<int:id_task>', edit_task.edit_task),
    path('view/task/<int:id_task>', view_task.view_task),
    path('create/task', create_task.create_task),
    path('injob', in_job.in_job),
    path('about/', about.about, name='about'),
    path('', index.index, name='index'),
]