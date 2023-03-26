from django.contrib import admin
from .models import Profile

# Register your models here.

admin.site.register(Profile)
admin.site.site_header='Dashboard'
admin.site.site_title='Dashboard'