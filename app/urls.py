from django.urls import path, re_path
from .views import about
from .views import index, create, edit, delete

urlpatterns = [
    path('create/', create.create),
    path('edit/<int:id>/', edit.edit),
    path('delete/<int:id>/', delete.delete),
    path('about/', about.about),
    path('', index.index, name="index"),
]