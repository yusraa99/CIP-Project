from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User
# from company.models import Company
# Create your models here.

class Informations(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    compcode=models.CharField(max_length=50,blank=True, null=True)
    email=models.EmailField(max_length=254,blank=True, null=True)
    phone=models.CharField(max_length=50,blank=True, null=True)
    location=models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.compcode
        

