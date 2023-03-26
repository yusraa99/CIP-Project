from django.contrib import admin
from django.urls import path,include
from . import views

app_name='blog'
urlpatterns = [
    path('',views.blog_list,name='blog_page'),
    path('<str:blog_url>',views.blog_details,name='blogdetail_page'),
]