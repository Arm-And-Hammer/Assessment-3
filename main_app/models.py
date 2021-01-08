from django.db import models
from django.urls import reverse

# Create your models here.

class Widgit(models.Model):
    description = models.CharField(max_length=50)
    quantity = models.IntegerField

    def __str__(self):
        return self.description, self.quantity
    
    def get_absolute_urls(self):
        return reverse('index')
