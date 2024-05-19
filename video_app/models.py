from django.db import models
from tinymce.models import HTMLField

class Video(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    url         = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class WebPage(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField(null=True, blank=True)

    def __str__(self):
        return self.title
    