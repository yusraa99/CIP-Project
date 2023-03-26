from django.contrib import admin
from django.urls import path,include
from . import views

app_name='howinvest'
urlpatterns = [
    path('',views.howinvest,name='howinvest_page'),
]