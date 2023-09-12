from django.db import models

# Create your models here.
choice = [
    ('Owner','Owner'),
    ('Rent','Rent')
]

class Member(models.Model):

    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    mobile = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    flat_no = models.IntegerField()
    wing = models.CharField(max_length=1)
    res_from = models.DateField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    res_type = models.CharField(max_length=20,default='Owner',choices=choice)
    verify = models.BooleanField(default=False)
    pic = models.FileField(upload_to='member_pic',default='avtar.png')
    password = models.CharField(max_length=30,null=True,blank=True)


    def __str__(self) -> str:
        return self.fname + '  ' + self.lname + ' >> ' + str(self.flat_no)


class Main(models.Model):

    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    pay_on = models.DateTimeField(auto_now_add=True)
    verify = models.BooleanField(default=False)
    amount = models.IntegerField()
    trans_id = models.CharField(max_length=30)
    pay_for = models.DateField()

    def __str__(self):
        return self.member.fname + ' >> ' + self.amount
