from django.shortcuts import render

# Create your views here.
def freQuestion(request):
    return render(request,'freqQuestions/faq.html')
