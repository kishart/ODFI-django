from sys import path
from django.db import models
from django.conf import settings
from django.conf.urls.static import static

# Create your models here.

# class Photo(models.Model):
#     image = models.ImageField(upload_to='photos/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Photo {self.id} uploaded at {self.uploaded_at}"
    

class Photo(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)