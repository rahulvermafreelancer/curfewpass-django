from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('main/',views.main,name='main'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('register/',views.register,name='register'),
    path('registerUser/',views.registerUser,name='registerUser'),
    path('userhome/',views.userhome,name='userhome'),
    path('applypassuser/',views.applypassuser,name='applypassuser'),
    path('passUpdate/',views.passUpdate,name='passUpdate'),
    path('updateUserPass/',views.updateUserPass,name='updateUserPass'),
    path('passhistory/',views.passhistory,name='passhistory'),
    path('validation',views.validation,name='validation'),
    path('logoutusers',views.logout_users,name='logout_users'),
    path('adminHome/',views.adminHome,name='adminHome'),
    path('newrequestadmin/',views.newrequestadmin,name='newrequestadmin'),
    path('assignauthority/',views.assignauthority,name='assignauthority'),
    path('createauthority/',views.createauthority,name='createauthority'),
    path('authoritycreated/',views.authoritycreated,name='authoritycreated'),
    path('requestfind/',views.requestfind,name='requestfind'),
    path('authorityhome/',views.authorityhome,name='authorityhome'),
    path('newrequestauthority/',views.newrequestauthority,name='newrequestauthority'),
    path('checkhistoryauthority/',views.checkhistoryauthority,name='checkhistoryauthority'),
    path('applyForNewPass/',views.applyForNewPass,name='applyForNewPass'),
    path('manageprofile/',views.manageprofile,name='manageprofile'),
    path('acceptrequestadmin/',views.acceptrequestadmin,name='acceptrequestadmin'),
]
