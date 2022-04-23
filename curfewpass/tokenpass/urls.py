from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('register/',views.register,name='register'),
    path('registerUser/',views.registerUser,name='registerUser'),
    path('userhome/',views.userhome,name='userhome'),
    path('applypass/',views.applypass,name='applypass'),
    path('updatepass/',views.updatepass,name='updatepass'),
    path('passhistory/',views.passhistory,name='passhistory'),
]
