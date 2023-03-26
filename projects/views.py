from django.shortcuts import render
from .models import Project
from company.models import Company
from blog.models import Blog
from compinformation.models import Informations
from django.core.paginator import Paginator
from InvestmentEth import app
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def projects(request):
    project=Project.objects.all()
    company=Company.objects.all()

    paginator=Paginator(project,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    context={'project':page_obj,'company':company}
    return render(request,'projects/projects.html',context)

def project_details(request,prject_url):
    project_title=prject_url.replace('-',' ')
    project=Project.objects.get(title=project_title)
    
        # company=Company.objects.get(id=project.company_id)
    blogs=Blog.objects.all()
    context={'project':project,'blogs':blogs}
    return render(request,'projects/project_details.html',context)
      
    # blogs=Blog.objects.all()
    # context={'project':project,'blogs':blogs}

    # return render(request,'projects/project_details.html',context)

@login_required
def addinvest(request,prject_url):
    project_title=prject_url.replace('-',' ')
    project=Project.objects.get(title=project_title)
    
    currencyType="$"
    user_name=request.user.username
    if request.method=="POST":
        user_id=request.user.id
        investtype="Risk"
        value=int(request.POST.get('money'))
        wallet=app.contract.functions.ShowUserWallet(user_id).call()
        newmoney=wallet[2]-value
        print(newmoney)
        project_id=project.id
        if value <= wallet[2]:
            if project.company:
                company_id=project.company_id
                print(company_id)
                addinvest=app.contract.functions.AddInvest(company_id,user_id,investtype,value,project_id).transact()
                tx_receipt = app.web3.eth.waitForTransactionReceipt(addinvest)
                updatewallet=app.contract.functions.UpdateUserWallet(user_id,user_name,newmoney,currencyType).transact()
                tx_receipt = app.web3.eth.waitForTransactionReceipt(updatewallet)
            elif project.user_verf:
                investorid=project.user_verf.id
                print(investorid)
                addinvest=app.contract.functions.AddInvest(investorid,user_id,investtype,value,project_id).transact()
                tx_receipt = app.web3.eth.waitForTransactionReceipt(addinvest)
                updatewallet=app.contract.functions.UpdateUserWallet(user_id,user_name,newmoney,currencyType).transact()
                tx_receipt = app.web3.eth.waitForTransactionReceipt(updatewallet)

            return redirect('/Our-Projects/')
        elif value > wallet[2]:
            msg="Sorry you don't have enough money!! Please Check your account balance."
            context={'project':project,'msg':msg}
            return render(request,'projects/project_invest.html',context)

    context={'project':project}
    return render(request,'projects/project_invest.html',context)

def invest(request,prject_url):

    project_title=prject_url.replace('-',' ')
    project=Project.objects.get(title=project_title)
    user_id=request.user.id
    investtype="Risk"
    value=1
    wallet=app.contract.functions.ShowUserWallet(user_id).call()
    newmoney=wallet[2]-value
    print(newmoney)
    # companyid=Company.objects.get(id=project.company.id)
    project_id=project.id
    if project.company:
        company_id=project.company_id
        print(company_id)
        addinvest=app.contract.functions.AddInvest(company_id,user_id,investtype,value,project_id).transact()
        tx_receipt = app.web3.eth.waitForTransactionReceipt(addinvest)
        updatewallet=app.contract.functions.UpdateUserWallet(user_id,newmoney).transact()
        tx_receipt = app.web3.eth.waitForTransactionReceipt(updatewallet)
    elif project.user_verf:
        investorid=project.user_verf.id
        print(investorid)
        addinvest=app.contract.functions.AddInvest(investorid,user_id,investtype,value,project_id).transact()
        tx_receipt = app.web3.eth.waitForTransactionReceipt(addinvest)
        updatewallet=app.contract.functions.UpdateUserWallet(user_id,newmoney).transact()
        tx_receipt = app.web3.eth.waitForTransactionReceipt(updatewallet)

    return redirect('/Our-Projects/')

    