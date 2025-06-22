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
    
class Files(models.Model):
    file = models.FileField(upload_to='files/')  # Accepts both image and video files

class Media(models.Model):
    CATEGORY_CHOICES = [
        ('Images', 'Images'),
        ('Videos', 'Videos'),
    ]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to='media/')  # Accepts both image and video files
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media {self.id} ({self.category}) uploaded at {self.uploaded_at}"

    def is_video(self):
        return self.file.name.lower().endswith(('.mp4', '.mov', '.avi', '.webm', '.mkv'))



class Photo(models.Model):
    TYPE_CHOICES = [
        ('News', 'News'),
        ('Event', 'Event'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default='2025-01-01')

    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.type}: {self.title}"

