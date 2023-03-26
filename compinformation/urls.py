from django.contrib import admin
from django.urls import path,include
from . import views




app_name='compinformation'
urlpatterns = [
    path('Add-Company/',views.add_comp_info,name='add_comp_info'),
    path('Information/',views.compInfo,name='compInfo'),
    path('Information/edit/',views.edit_comp_info,name='edit_comp_info'),
    path('Projects/',views.comp_project,name='comp_project'),
    path('Projects/Add/',views.add_comp_project,name='add_comp_project'),
    path('Project/',views.get_comp_project,name='get_comp_project'),
    path('Project/edit/<str:prject_url>',views.edit_comp_project,name='edit_comp_project'),
    path('Company-Blog/',views.compBlog,name='compBlog'),
    path('Company-Blog/Add/',views.add_comp_post,name='add_comp_post'),
    path('Company-Blog/Posts/',views.get_comp_posts,name='get_comp_posts'),
    path('Company-Blog/Posts/edit/<str:post_url>',views.edit_comp_post,name='edit_comp_post'),

    
    
    

]