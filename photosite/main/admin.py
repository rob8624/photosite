from django.contrib import admin
from .models import Image



# Register your models here.



class ImageAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'image', 'image_number', 'front_page',)

    
    
admin.site.register(Image)





