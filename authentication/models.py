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

