from django.contrib import admin
from django.urls import path,include
from . import views

app_name='advices'
urlpatterns = [
    path('',views.advices,name='advices_page'),
    path('trading-bot/',views.Trading_page,name='Trading_page'),
    path('trading-bot/broken-trend',views.secon_ques,name='secon_ques'),
    path('trading-bot/model',views.therdques,name='therdques'),
    path('trading-bot/model/type',views.forthques,name='forthques'),
    path('trading-bot/model/breaking-resistence',views.fifthques,name='fifthques'),
    path('trading-bot/model/breaking-resistence/breaking-suport',views.sixques,name='sixques'),
    path('trading-bot/model/breaking-resistence/breaking-suport/volume',views.sevnques,name='sevnques'),
    path('trading-bot/model/breaking-resistence/breaking-suport/volume/price',views.eightques,name='eightques'),
    path('trading-bot/model/breaking-resistence/breaking-suport/volume/price/rsi',views.nineques,name='nineques'),


    

]