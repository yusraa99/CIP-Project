from django.contrib import admin
from django.urls import path,include
from . import views

app_name='markettrend'
urlpatterns = [
    path('',views.markettrend,name='markettrend_page'),
]