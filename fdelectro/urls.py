from django.urls import path
from . import views

urlpatterns=[path('',views.index),path('register/',views.register1),path('signin/command/1',views.home),
path('signin/command/2',views.command),path('signin/command/3',views.about),
path('signin/command/',views.command),path('signin/command/1',views.signin1),path('fdelectro/aboutus',views.about),path('fdelectro/command',views.command),]
