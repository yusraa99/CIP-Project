from django.db import models
from category.models import Category
from compinformation.models import Informations
from  django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



def image_upload(instance,filename):
    imagename , extenstion = filename.split(".")
    return "company/%s.%s"%(instance.id,extenstion)

class Company(models.Model):
    info=models.OneToOneField(Informations, on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True, null=True)
    about_company=models.TextField(max_length=10000,blank=True, null=True)
    image=models.ImageField(upload_to=image_upload,blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
   
    def __str__(self):
        # return self.info.compcode
        return str(self.info.compcode)

    def name_url(self):    
        return self.name.replace(' ','-')


@receiver(post_save, sender=Informations)
def create_company_profile(sender,instance,created, **kwargs):
    if created:
        Company.objects.create(info=instance)

