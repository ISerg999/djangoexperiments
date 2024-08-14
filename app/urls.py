from django.urls import path, re_path
from . import views

urlpatterns = [
    path('user', views.user, name="user"),
    path('user/<name>', views.user, name="user"),
    path('user/<name>/<int:age>', views.user, name="user"),
    path('about', views.about, name="about"),
    path('json', views.json, name="json"),
    path('json/<name>', views.json, name="json"),
    path('json/<name>/<int:age>', views.json, name="json"),
    path('home', views.home),
    path('', views.index, name="index"),
]