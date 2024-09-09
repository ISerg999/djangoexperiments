from django.urls import path, re_path
from .views import about
from .views import index
from .views import create_task
from .views import in_job

urlpatterns = [
    # path('create/', create.create),
    # path('edit/<int:id>/', edit.edit),
    # path('delete/<int:id>/', delete.delete),
    path('create/task', create_task.create_task),
    path('injob', in_job.in_job, name='injob'),
    path('about/', about.about, name='about'),
    path('', index.index, name='index'),
]