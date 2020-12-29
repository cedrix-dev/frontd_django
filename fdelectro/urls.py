from django.urls import path
from . import views

urlpatterns=[path('',views.index),path('register/',views.register),path('register/',views.register),path('fdelectro/aboutus',views.about),path('fdelectro/command',views.command),]
