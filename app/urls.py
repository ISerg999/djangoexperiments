from django.urls import path, re_path
from . import views

urlpatterns = [
    path('user', views.user, name="user"),
    path('about', views.about, name="about"),
    path('json', views.json, name="json"),
    path('', views.index, name="index"),
]