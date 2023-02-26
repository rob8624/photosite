from django.db import models
from PIL import Image as Image_pil, ExifTags

# Create your models here.

class Image(models.Model):
    timestamp = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = 'images')
    image_number = models.IntegerField
    front_page = models.BooleanField()
    caption = models.TextField(max_length=2000, null=True, blank=True, editable=True)

    
    if caption != caption:
        
        def save(self, *args, **kwargs):
            super(Image, self).save(*args, **kwargs)

            """Get EXIF"""
            
            im = Image_pil.open(self.image)
            try:
                info = im.getexif()[0x010e]
                self.caption = info
                print(self.caption)

            
                
                super(Image, self).save(*args, **kwargs)
            
            except KeyError:
                pass
            super(Image, self).save(*args, **kwargs)
            
   