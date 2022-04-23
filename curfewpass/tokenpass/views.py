from tkinter import Variable
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginpage(request):
    return render(request, 'login.html')
    
def register(request):
    return render(request, 'register.html')

def registerUser(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname= request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
    
    if firstname!='' and lastname!='' and email!='':
        register = User(first_name=firstname, last_name=lastname, email=email)

def userhome(request):
    return render(request, 'userhome.html')