from django.shortcuts import render
from django.shortcuts import redirect
from .forms import InformationForm
from company.forms import CompanyForm
from .models import Informations
from company.models import Company
from category.models import Category
from projects.models import Project
from projects.forms import ProjectForm
from django.urls import reverse
from blog.forms import PostForm
from blog.models import Blog
# Create your views here.
def add_comp_info(request):

    if request.method=="POST":
        form = InformationForm(request.POST)
        
        if form.is_valid():
            info=form.save(commit=False)
            info.user_id=request.user.id
            info.save()
            return redirect('/Company-Information/Information')
    else:
        form=InformationForm()
    return render(request,'compinformation/add_comp_info.html',{'form':form})



def compInfo(request):
    info=Informations.objects.get(user=request.user)
    comp=Company.objects.get(info=info)
    # category=Category.objects.get(id=comp.category_id)
    return render(request,'compinformation/comp_info.html',{'info':info,'comp':comp})

def edit_comp_info(request):
    info=Informations.objects.get(user=request.user)
    comp=Company.objects.get(info=info)
    # category=Category.objects.get(id=comp.category_id)
    
    if request.method=="POST":
        infoform=InformationForm(request.POST,instance=info)
        compcorm=CompanyForm(request.POST,request.FILES,instance=comp)
        if infoform.is_valid() and compcorm.is_valid():
            infoform.save()
            compcorm.save()
            return redirect(reverse('compinformation:compInfo'))

    else:
        infoform=InformationForm(instance=info)
        compcorm=CompanyForm(instance=comp)
        
    return render(request,'compinformation/edit_comp_info.html',{'infoform':infoform,'compcorm':compcorm})

def comp_project(request):
    return render(request,'compinformation/comp_project.html')


def add_comp_project(request):
    info=Informations.objects.get(user=request.user)
    comp=Company.objects.get(info=info)
    if request.method=="POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.company_id=comp.id
            proj.save()
            
            return redirect('/Company-Information/Projects')
    else:
        form=ProjectForm()
    return render(request,'compinformation/add_comp_project.html',{'form':form})

def get_comp_project(request):
    info=Informations.objects.get(user=request.user)
    comp=Company.objects.get(info=info)
    project=Project.objects.all()
    category=Category.objects.all()
    context={'project':project,'comp':comp,'category':category}
    return render(request,'compinformation/get_projects.html',context)
  
    

def edit_comp_project(request,prject_url):
    project_title=prject_url.replace('-',' ')
    info=Informations.objects.get(user=request.user)
    comp=Company.objects.get(info=info)
    project=Project.objects.get(title=project_title)
    if request.method=="POST":
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('/Company-Information/Project')
    else:
        projectform=ProjectForm(instance=project)
    return render(request,'compinformation/edit_comp_project.html',{'projectform':projectform})


def compBlog(request):
    return render(request,'compinformation/comp_blog.html')

def add_comp_post(request):
    info=Informations.objects.get(user=request.user)
    comp=Company.objects.get(info=info)
    if request.method=="POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.company_id=comp.id
            post.auther_name=comp.name
            post.save()

            return redirect('/Company-Information/Company-Blog')
    else:
        form=PostForm()
    return render(request,'compinformation/add_comp_post.html',{'form':form})

def get_comp_posts(request):
    info=Informations.objects.get(user=request.user)
    comp=Company.objects.get(info=info)
    category=Category.objects.all()
    posts=Blog.objects.all()
    context={'comp':comp,'category':category,'posts':posts}
    return render(request,'compinformation/get_posts.html',context)

def edit_comp_post(request,post_url):
   
    post_title=post_url.replace('-',' ')
    post=Blog.objects.get(title=post_title)
    if request.method=="POST":
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/Company-Information/Company-Blog/Posts')
    else:
        postform=PostForm(instance=post)
    return render(request,'compinformation/edit_comp_post.html',{'postform':postform})


