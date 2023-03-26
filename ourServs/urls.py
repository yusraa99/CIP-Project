from django.contrib import admin
from django.urls import path,include
from . import views

app_name='service'
urlpatterns = [
    path('',views.serv,name='serv_page'),
    path('details',views.servdetail,name='servdetail_page'),
]