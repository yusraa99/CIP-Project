from django.shortcuts import render

# Create your views here.
def serv(request):
    return render(request,'ourServs/servs.html')



def servdetail(request):
    return render(request,'ourServs/servsdetail.html')
