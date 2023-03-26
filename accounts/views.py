from django.shortcuts import render
from InvestmentEth import app
from category.models import Category
from .forms import SignupForm,UserForm,ProfileForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.urls import reverse
from .models import Profile
from company.models import Company
from compinformation.models import Informations
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from random import randrange
from projects.models import Project
from django.core.mail import send_mail
from django.conf import settings
from projects.models import Project
from projects.forms import ProjectForm

# Create your views here.
def signup(request):
   
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form =SignupForm()
    return render(request,'registration/signup.html',{'form':form})

@login_required
def profile(request):
    profile=Profile.objects.get(user=request.user)
    if profile.is_user==True or profile.verf_user==True:
        return render(request,'accounts/profile.html',{'profile':profile})
    elif profile.is_company==True:
        compinfo=Informations.objects.get(user_id=profile.user_id)
        context={'compinfo':compinfo,'profile':profile}
        return render(request,'accounts/companyprofile.html',context)

    return render(request,'accounts/profile.html')

@login_required
def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    # if profile.is_user==True:
    if request.method=="POST":
        userform=UserForm(request.POST,instance=request.user)
        profileform=ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile=profileform.save(commit=False)
            myprofile.user=request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:
        userform=UserForm(instance=request.user)
        profileform=ProfileForm(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})

@login_required
def add_wallet(request):
    # Dollar
    currencyType="$"
    global id
    id =0
    id +=1
    if request.method=="POST":
        user_id=request.user.id
        user_name=request.user.username
        money=int(request.POST.get('money'))
        global mywallet
        mywallet=app.contract.functions.AddWallet(id,user_name,money,currencyType,user_id).transact()
        tx_receipt = app.web3.eth.waitForTransactionReceipt(mywallet)
        return redirect(reverse('accounts:view_wallet'))
    
    return render(request,'accounts/wallet.html')

@login_required
def view_wallet(request):
    project=Project.objects.all()
    user_id=request.user.id
    try:
        wallet=app.contract.functions.ShowUserWallet(user_id).call()
        allInvest=app.contract.functions.ShowAllUserInvestments(user_id).call()
        print(wallet)
        print(allInvest)
        context={'wallet':wallet,'allInvest':allInvest,'project':project}
        
    except:
        
        return render(request,'accounts/viewWallet.html')
    return render(request,'accounts/viewWallet.html',context)
    
@login_required
def updatewallet(request):
    currencyType="$"
    global id
    id =0
    id +=1
    if request.method=="POST":
        user_id=request.user.id
        user_name=request.user.username
        money=int(request.POST.get('money'))
        global mywallet
        updatewallet=app.contract.functions.UpdateUserWallet(user_id,user_name,money,currencyType).transact()
        tx_receipt = app.web3.eth.waitForTransactionReceipt(updatewallet)
        print(updatewallet)
        return redirect(reverse('accounts:view_wallet'))
    
    return render(request,'accounts/updatewallet.html')

@login_required
def verified_req(request):

    user=randrange(10000)
    company=randrange(100000)
    if request.method=="POST":
        is_user=request.POST.get('verif')
        
        if is_user == "user":
            subject="Verification Code"
            global message
            message=str(user)
            email=request.POST['email']
            send_mail(subject , message ,  settings.EMAIL_HOST_USER , [email])
            # send=True
            return redirect('/accounts/verification/Code')
        elif is_user == "company":
            subject="Verification Code"
            message=str(company)
            email=request.POST['email']
            send_mail(subject , message ,  settings.EMAIL_HOST_USER , [email])
            return redirect('/accounts/verification/Code')

    # elif 'codesubmit' in request.POST:
    #     profile=Profile.objects.get(user=request.user)
    #     if request.method == "POST":
    #         code=request.POST.get('code')
    #         if len(code) >= 5:
    #             profile.is_company=True
    #             profile.is_user=False
    #             profile.verf_user=False
    #             profile.save()
    #             company=Informations.objects.create(user=request.user)
    #             return redirect(reverse('accounts:profile'))
    #         elif len(code) <= 4:
    #             profile.verf_user=True
    #             profile.is_user=False
    #             profile.save()
    #             return redirect(reverse('accounts:profile'))
        
    return render(request,'verefications/verefied_page.html')

@login_required
def verified_code(request):
    print(message)
    if request.method=="POST":
        profile=Profile.objects.get(user=request.user)
        if request.method == "POST":
            code=request.POST.get('code')
            if len(code) >= 5 and code == message:
                profile.is_company=True
                profile.is_user=False
                profile.verf_user=False
                profile.save()
                company=Informations.objects.create(user=request.user)
                return redirect(reverse('accounts:profile'))
            elif len(code) <= 4 and code == message:
                profile.verf_user=True
                profile.is_user=False
                profile.save()
                return redirect(reverse('accounts:profile'))
    return render(request,'verefications/code_page.html')
        


@login_required
def add_user_project(request):
    user_id=request.user
    if request.method=="POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.user_verf=user_id
            proj.save()
            
            return redirect('/accounts/verification/Projects')
    else:
        form=ProjectForm()
    return render(request,'verefications/add_user_project.html',{'form':form})

@login_required
def get_user_project(request):
    user=request.user
    project=Project.objects.all()
    category=Category.objects.all()
    context={'project':project,'user':user,'category':category}
    return render(request,'verefications/get_user_project.html',context)


@login_required
def edit_user_project(request,prject_url):
    project_title=prject_url.replace('-',' ')
    project=Project.objects.get(title=project_title)
    if request.method=="POST":
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('/accounts/verification/Projects')
    else:
        projectform=ProjectForm(instance=project)
    return render(request,'verefications/edit_user_project.html',{'projectform':projectform,'project':project})
