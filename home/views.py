from django.shortcuts import render
from blog.models import Blog
from projects.models import Project
from company.models import Company
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    project=Project.objects.all()[:4]
    all_project=Project.objects.all()
    all_company=Company.objects.all()
    all_users=User.objects.all()
    blog_list=Blog.objects.all()[:3]
    context={'blogs':blog_list,'project':project,'all_project':all_project,'all_company':all_company,'all_users':all_users}
    return render(request,'home/home.html',context)
