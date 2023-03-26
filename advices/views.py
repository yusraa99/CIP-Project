from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def advices(request):
    return render(request,'advices/advices.html')


def Trading_page(request):
    if request.method=="POST":
        global company
        company=request.POST.get('trade')
        return redirect(reverse('advices:secon_ques'))
    
    return render(request,'advices/tradingbot.html')

def secon_ques(request):
    if request.method=="POST":
        answer=request.POST.get('trends')
        if answer == "yes":
            return render(request,'advices/sellpage.html')
        elif answer == "no":
            return render(request,'advices/buypage.html')
        elif answer == "none":
            return redirect(reverse('advices:therdques'))
    return render(request,'advices/brokentrend.html')

def therdques(request):
    if request.method=="POST":
        answer=request.POST.get('model')
        if answer == "yes":
            return redirect(reverse('advices:forthques'))
        elif answer == "no":
            return redirect(reverse('advices:fifthques'))
        

    return render(request,'advices/modelpage.html')


def forthques(request):
    if request.method=="POST":
        answer=request.POST.get('modeltype')
        if answer == "m":
            return render(request,'advices/sellpage.html')
        elif answer == "w":
            return render(request,'advices/buypage.html')
        

    return render(request,'advices/whatmodelpage.html')


def fifthques(request):
    if request.method=="POST":
        answer=request.POST.get('break')
        if answer == "yes":
            return render(request,'advices/buypage.html')
        elif answer == "no":
            return redirect(reverse('advices:sixques'))
        

    return render(request,'advices/breakresis.html')


def sixques(request):
    if request.method=="POST":
        answer=request.POST.get('support')
        if answer == "yes":
            return render(request,'advices/buypage.html')
        elif answer == "no":
            return redirect(reverse('advices:sevnques'))
        

    return render(request,'advices/breaksupport.html')

def sevnques(request):
    if request.method=="POST":
        answer=request.POST.get('volume')
        
        if int(answer) > 75 :
            return render(request,'advices/sellpage.html')
        elif int(answer) < 75:
            return redirect(reverse('advices:eightques'))
        

    return render(request,'advices/volume.html')


def eightques(request):
    if request.method=="POST":
        answer=request.POST.get('price')
        if answer == "up":
            return render(request,'advices/sellpage.html')
        elif answer == "down":
            return render(request,'advices/buypage.html')
        elif answer == "none":
            return redirect(reverse('advices:nineques'))
        

    return render(request,'advices/price.html')

def nineques(request):
    if request.method=="POST":
        answer=request.POST.get('rsi')
        if int(answer) < 35:
            return render(request,'advices/buypage.html')
        elif int(answer) > 75:
            return render(request,'advices/sellpage.html')
        else:
            return render(request,'advices/waitpage.html')
        

    return render(request,'advices/rsi.html')