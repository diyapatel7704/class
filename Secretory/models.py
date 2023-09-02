from django.db import models
from django.utils import timezone
from Members.models import *

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
    

class Complain(models.Model):
    
    complain_by = models.ForeignKey(Member,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    des = models.TextField()
    pic = models.FileField(upload_to='complains/',null=True,blank=True)
    solve_by = models.ForeignKey(Secratory,on_delete=models.CASCADE,blank=True,null=True)
    complain_on = models.DateTimeField(auto_now_add=True)
    solve_on = models.DateTimeField(null=True,blank=True)
    solve = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    

