from tkinter import Variable
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


# Create your views here.
API = 'http://127.0.0.1:8000/tokenGenerator'

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
        register.save()
    else:
        return redirect(API+'/register/')

def userhome(request):
    return render(request, 'userhome.html')

def applypass(request):
    return render(request, 'applypass.html')

def updatepass(request):
    return render(request, 'updatepass.html')

def passhistory(request):
    return render(request, 'passhistory.html')

def adminHome(request):
    return render(request, 'adminHome.html')

def newrequestadmin(request):
    return render(request, 'newrequestadmin.html')

def assignauthority(request):
    return render(request, 'assignauthority.html')

def createauthority(request):
    return render(request, 'createauthority.html')

def requestfind(request):
    return render(request, 'requestfind.html')

def authorityhome(request):
    return render(request, 'authorityhome.html')    

def newrequestauthority(request):
    return render(request, 'newrequestauthority.html')

def checkhistoryauthority(request):
    return render(request, 'checkhistoryauthority.html')

