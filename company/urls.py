from django.contrib import admin
from django.urls import path,include
from . import views

app_name='company'
urlpatterns = [
    path('',views.company,name='company_page'),
    path('<str:name>',views.company_details,name='company_details'),
    path('Projects/<str:comp_url>',views.company_project,name='company_project'),
    
]