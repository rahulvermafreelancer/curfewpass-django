from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('header/',views.header,name='header'),
    path('userheader/',views.userheader,name='userheader'),
    path('adminheader/',views.adminheader,name='adminheader'),
]
