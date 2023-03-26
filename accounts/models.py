from django.db import models
from django.contrib.auth.models import User
from  django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

def image_upload(instance,filename):
    imagename , extenstion = filename.split(".")
    return "profile/%s.%s"%(instance.id,extenstion)

GENDER_TYPE=(
    ('Male','Male'),
    ('Fmale','Fmale'),
    
)


class Profile(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city=models.CharField(max_length=50,blank=True, null=True)
    phone_number=models.CharField( max_length=15,blank=True, null=True)
    gender=models.CharField(max_length=15,choices=GENDER_TYPE,blank=True, null=True)
    image=models.ImageField(upload_to=image_upload,blank=True, null=True)
    is_user=models.BooleanField(default=True)
    is_company=models.BooleanField(default=False)
    verf_user=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    
@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

