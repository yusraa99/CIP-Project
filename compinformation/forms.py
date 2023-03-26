from django import forms
from .models import Informations


class InformationForm(forms.ModelForm):
    class Meta:
        model = Informations
        fields = ['compcode','email','phone','location']
