from django.urls import path
from . import views

urlpatterns=[path('',views.index),path('register/',views.register1),path('signin/command/1',views.home),
path('signin/command/2',views.command),path('signin/command/3',views.about),path('signin/command/5',views.register1),
path('signin/command/',views.signin1),path('fdelectro/aboutus',views.about),path('fdelectro/command',views.command),path('fdelectro/command/10',views.btn10),path('fdelectro/command/11',views.btn11),path('fdelectro/command/12',views.btn12),path('fdelectro/command/13',views.btn13),path('fdelectro/command/14',views.btn14),path('fdelectro/command/15',views.btn15),path('fdelectro/command/16',views.btn16),]
                                  
