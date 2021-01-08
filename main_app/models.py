from django.db import models
from django.urls import reverse

# Create your models here.

class Widgit(models.Model):
    item = models.CharField(max_length=50)

    def __str__(self):
        return self.item

    def get_absolute_urls(self):
        return reverse('index')
