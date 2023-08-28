from django.db import models
from django.utils import timezone

# Create your models here.

class Secratory(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    password = models.CharField(max_length=30)
    sec_from = models.DateField(auto_now_add=True)
    profile_pic = models.FileField(upload_to='profile',default='avtar.png')

    def __str__(self):
        return self.name
    

class Event(models.Model):

    created_by = models.ForeignKey(Secratory,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    des = models.TextField()
    date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    pic = models.FileField(upload_to='event',null=True,blank=True)

    def __str__(self) -> str:
        return self.subject