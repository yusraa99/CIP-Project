from django.db import models
from company.models import Company
from category.models import Category
# Create your models here.

def image_upload(instance,filename):
    imagename , extenstion = filename.split(".")
    return "blogs/%s.%s"%(instance.id,extenstion)

class Blog(models.Model):
    
    title = models.CharField(max_length=100)
    description=models.TextField(max_length=4000)
    created_at=models.DateTimeField(auto_now=True)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    auther_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to=image_upload)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.title)

    def title_url(self):
        return self.title.replace(' ','-')