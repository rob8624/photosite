from django.urls import path, include
from django.urls import re_path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
]