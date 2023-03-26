"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('admin/', admin.site.urls),
    path('', include('home.urls',namespace='home')),
    path('Blog/', include('blog.urls',namespace='blog')),
    path('About-cip/', include('about.urls',namespace='about')),
    path('Contact-us/', include('contact.urls',namespace='contact')),
    path('Team/', include('team.urls',namespace='team')),
    path('Faq/', include('freqQuestions.urls',namespace='faq')),
    path('Services/', include('ourServs.urls',namespace='service')),
    path('Market-Trend/', include('marketTrend.urls',namespace='markettrend')),
    path('How-to-Invest/', include('howInvest.urls',namespace='howinvest')),
    path('Development-Process/', include('learn.urls',namespace='learn')),
    path('Advices/', include('advices.urls',namespace='advices')),
    path('Privacy-Policy/', include('privacyPolicy.urls',namespace='privacypolicy')),
    path('Terms-Condition/',include('termsCondition.urls',namespace='termscondition')),
    path('Companies/',include('company.urls',namespace='company')),
    path('Our-Projects/',include('projects.urls',namespace='projects')),
    path('Company-Information/',include('compinformation.urls',namespace='compinformation')),

    

   
]
urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)