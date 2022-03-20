from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginpage,name='loginpage'),
    path('register',views.register,name='register'),
]
