from django.db import connection
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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
    
    if firstname!='' and lastname!='' and email!='' and password!='':
        register = User.objects.create_user(first_name=firstname, last_name=lastname,username=email, email=email, password=password)
        register.save()
        messages.success(request, 'User added successfully !!')
        return redirect(API+'/loginpage/')
    else:
        messages.error(request, 'Something went wrong !!')
        return redirect(API+'/register/')


def validation(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        # result = checkUser(username)
        user  = authenticate(username=username,password=password)
        print(user)
        
        if user is not None:
            # if result == 1:
            login(request,user)
            # return HttpResponse("true")
            return redirect(API+'/userhome/')
        else:
            # return HttpResponse("false")
            messages.error(request, 'Username or Password Incorrect')
            return redirect(API+'/loginpage/')
    else:
        # return HttpResponse("false")
        messages.error(request, 'Username or Password Incorrect')
        return redirect(API+'/loginpage/')

def checkUser(username):
    query = "SELECT is_staff FROM auth_user WHERE username='" + username + "';"
    with connection.cursor() as cursor:
        cursor.execute(query)
        res = cursor.fetchone()
        result = res[0]
    return result 

def userhome(request):
    return render(request, 'userhome.html')

def applypass(request):
    return render(request, 'applypass.html')

def updatepass(request):
    return render(request, 'updatepass.html')

def passhistory(request):
    return render(request, 'passhistory.html')
