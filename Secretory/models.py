from django.db import models
from django.utils import timezone

# Create your models here.

class Secratory(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    password = models.CharField(max_length=30)
    sec_from = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name
    