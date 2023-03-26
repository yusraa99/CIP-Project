from django import forms
from .models import Blog


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','description','image','category']


# auther name is company name 
# company is the id of same company