from django.urls import path, re_path
from . import views

urlpatterns = [
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('', views.index, name="index"),
]