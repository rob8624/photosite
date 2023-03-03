from django.urls import path, include
from django.urls import re_path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("sign-in", views.sign_in, name="sign-in"),
    path("sign-up", views.sign_up, name="sign-up"),
]