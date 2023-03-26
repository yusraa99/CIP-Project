from django.contrib import admin
from django.urls import path,include
from . import views




app_name='accounts'
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.profile_edit,name='profile_edit'),
    
    path('wallet',views.view_wallet,name='view_wallet'),
    path('wallet/AddMoney',views.add_wallet,name='add_wallet'),
    path('wallet/Update',views.updatewallet,name='updatewallet'),
    


    path('verification/',views.verified_req,name='verified_req'),
    path('verification/Code',views.verified_code,name='verified_code'),
    path('verification/Projects',views.get_user_project,name='get_user_project'),
    path('verification/Projects/Add',views.add_user_project,name='add_user_project'),
    path('verification/Projects/Edit/<str:prject_url>',views.edit_user_project,name='edit_user_project'),

    

]