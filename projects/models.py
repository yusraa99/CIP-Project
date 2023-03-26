from django.db import models
from category.models import Category
from company.models import Company
from django.contrib.auth.models import User
# Create your models here.



def image_upload(instance,filename):
    imagename , extenstion = filename.split(".")
    return "project/%s.%s"%(instance.id,extenstion)

OPEN_TYPE=(
    ('Open','Open'),
    ('Close','Close'),
    ('Coming Soon','Coming Soon'),
)

class Project(models.Model):

    title=models.CharField(max_length=50)
    description=models.TextField(max_length=10000)
    image=models.ImageField(upload_to=image_upload)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    company=models.ForeignKey(Company, on_delete=models.CASCADE,blank=True, null=True)
    user_verf=models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    open_at=models.CharField(max_length=50)
    goal=models.CharField(max_length=50)
    minimum_investment=models.CharField(max_length=50)
    open_type=models.CharField(max_length=15,choices=OPEN_TYPE)

   
    def __str__(self):
        return self.title

    def title_url(self):
        return self.title.replace(' ','-')