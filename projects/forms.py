from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','image','category','open_at','goal','minimum_investment','open_type']


