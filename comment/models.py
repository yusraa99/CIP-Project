from django.db import models
from blog.models import Blog
from django.contrib.auth.models import User


# Create your models here.

class Comment(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    body=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title
