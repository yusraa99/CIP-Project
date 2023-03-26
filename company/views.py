from django.shortcuts import render
from .models import Company
from compinformation.models import Informations
from company.models import Company
from projects.models import Project
# Create your views here.


def company(request):
    
    company=Company.objects.all().order_by('name')
    context={'companies':company}
    
    return render(request,'company/company.html',context)

def company_details(request,name):
    company=Informations.objects.get(compcode=name)
    company_details=Company.objects.get(info=company)
    context={'company':company,'company_details':company_details}
    return render(request,'company/company_detail.html',context)
    
def company_project(request,comp_url):

    company_name=comp_url.replace('-',' ')
    company=Company.objects.get(name=company_name)
    project=Project.objects.all()
    
    context={'project':project,'company':company}
    return render(request,'company/company_projects.html',context)