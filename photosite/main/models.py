from django.db import models

# Create your models here.

class Image(models.Model):
    timestamp = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = 'images')
    image_number = models.IntegerField
    front_page = models.BooleanField()