from django.db import models
from django.utils import timezone


class Articles(models.Model):
    draft = "d"
    publish = "p"
    STATUS_CHOICES = [
        (draft,"draft"),
        (publish,"publish")
    ]
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to="images",)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=draft)

    def __str__(self):
        return self.title

