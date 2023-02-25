from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Image
# Create your views here.
def index(request):
    images_all = Image.objects.all()
    images = images_all.filter(front_page=True)
    return render(request,  "index.html", {"images": images})