from django.db import models

# Create your models here.

class Widgit(models.Model):
    item = models.CharField(max_length=50)

    