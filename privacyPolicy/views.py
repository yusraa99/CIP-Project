from django.shortcuts import render

# Create your views here.
def privacypolicy(request):
    return render(request,'privacyPolicy/privacypolicy.html')
