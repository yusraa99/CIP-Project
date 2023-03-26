from django.contrib import admin
from django.urls import path,include
from . import views

app_name='faq'
urlpatterns = [
    path('',views.freQuestion,name='faq_page'),
]