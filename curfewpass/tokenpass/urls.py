from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('register/',views.register,name='register'),
    path('registerUser/',views.registerUser,name='registerUser'),
    path('userhome/',views.userhome,name='userhome'),
    path('applypassuser/',views.applypassuser,name='applypassuser'),
    path('updatepass/',views.updatepass,name='updatepass'),
    path('passhistory/',views.passhistory,name='passhistory'),
    path('validation',views.validation,name='validation'),
    path('adminHome/',views.adminHome,name='adminHome'),
    path('newrequestadmin/',views.newrequestadmin,name='newrequestadmin'),
    path('assignauthority/',views.assignauthority,name='assignauthority'),
    path('createauthority/',views.createauthority,name='createauthority'),
    path('requestfind/',views.requestfind,name='requestfind'),
    path('authorityhome/',views.authorityhome,name='authorityhome'),
    path('newrequestauthority/',views.newrequestauthority,name='newrequestauthority'),
    path('checkhistoryauthority/',views.checkhistoryauthority,name='checkhistoryauthority'),
    path('applyForNewPass/',views.applyForNewPass,name='applyForNewPass'),
]
