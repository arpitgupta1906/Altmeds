from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    doctorName= models.CharField(max_length=200)
    doctorId = models.CharField(unique=True)
    hospitalName=models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    isApproved=False

    def __str__(self):
        return self.user.username
