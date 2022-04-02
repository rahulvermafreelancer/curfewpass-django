from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('register/',views.register,name='register'),
    path('registerUser/',views.registerUser,name='registerUser'),
]
