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
def applyForNewPass(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        contact = request.POST['contact']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        dateofbirth = request.POST['date_of_birth']
        startdate = request.POST['start_date']
        startlocation = request.POST['start_location']
        endlocation = request.POST['end_location']
        reason = request.POST['reason']
        identitytype = request.POST['identity_type']
        employeeid = request.POST['employee_id']
        department = request.POST['department']
        photo = request.POST['photo']
    
    # if firstname!='' and lastname!='' and contact!='' and email!='' and address!='' and city!='' and state!='' and dateofbirth!='' and startdate!='' and startlocation!='' and endlocation!='' and reason!='' and identitytype!='' and employeeid!='' and department!='' and photo!='' :

def updatePass(request):
    if request.method=='POST':
        updatestartlocation = request.POST['update_start_location']
        updateendloction = request.POST['update_end_location']
        update_reason = request.POST['update_reason']

def userhome(request):
    return render(request, 'userhome.html')

def applypassuser(request):
    return render(request, 'applypassuser.html')

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

