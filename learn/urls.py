from django.contrib import admin
from django.urls import path,include
from . import views

app_name='learn'
urlpatterns = [
    path('',views.learn,name='learn_page'),
]