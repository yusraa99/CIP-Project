from django.contrib import admin
from django.urls import path,include
from . import views

app_name='projects'
urlpatterns = [
    path('',views.projects,name='projects_page'),
    path('<str:prject_url>',views.project_details,name='project_details'),
    path('Invest/Add/<str:prject_url>',views.addinvest,name='addinvest'),
    path('Invest/Confirm/<str:prject_url>',views.invest,name='invest'),


    
]