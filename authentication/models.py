from sys import path
from django.db import models
from django.conf import settings
from django.conf.urls.static import static



class MediaGroup(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MediaFile(models.Model):
    group = models.ForeignKey(MediaGroup, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='uploads/')


class Files(models.Model):
    file = models.FileField(upload_to='files/')
    title = models.CharField(max_length=255)
    description = models.TextField()


    
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

class Highlight(models.Model):
    HIGHLIGHT_TYPES = [
        ('news', 'News'),
        ('event', 'Event'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=HIGHLIGHT_TYPES)
    image = models.ImageField(upload_to='highlights/')
    date = models.DateField()

    def __str__(self):
        return self.title