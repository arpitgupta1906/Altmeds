from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    doctorName= models.CharField(max_length=200,null =True)
    doctorId = models.CharField(unique=True,max_length=200,null=True)
    hospitalName=models.CharField(max_length=200,null=True)
    # isApproved=models.BooleanField(default=False)
    isApproved=models.IntegerField(default=0)

    def __str__(self):
        return self.doctorName


class headache(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

class malaria(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name
