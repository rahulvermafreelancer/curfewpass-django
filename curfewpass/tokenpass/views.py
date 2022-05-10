import os
import time
from django.db import connection
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import *

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
        result = checkUser(username)
        user  = authenticate(username=username,password=password)
        print(user,result)
        
        if user is not None:
            if result == 0:
                login(request,user)
            # return HttpResponse("true")
                return redirect(API+'/userhome/')
            elif result==1:
                login(request,user)
            # return HttpResponse("true")
                return redirect(API+'/adminHome/')
            elif result==2:
                login(request,user)
            # return HttpResponse("true")
                return redirect(API+'/authorityhome/')
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
        
        
        profile_pic = request.FILES['uploadFile']
        splitName = os.path.splitext(profile_pic.name)
        fileName = str(int(time.time()))+splitName[1]
        handle_uploaded_file(profile_pic, fileName)         
    
    if firstname!='' and lastname!='' and contact!='' and email!='' and address!='' and city!='' and state!='' and dateofbirth!='' and startdate!='' and startlocation!='' and endlocation!='' and reason!='' and identitytype!='' and employeeid!='' and department!='':
        apply_pass = applynewpass(firstname=firstname,lastname=lastname,contact=contact,email=email,address=address,city=city,state=state,date_of_birth=dateofbirth,start_date=startdate,start_location=startlocation,end_location=endlocation,reason=reason,identity_type=identitytype,employee_id=employeeid,department=department,photo=fileName)
        apply_pass.save()
        messages.success(request, 'Pass request generated successfully !!')
        return redirect(API+'/userhome/')
    else:
        messages.error(request, 'Something went wrong !!')
        return redirect(API+'/applypassuser/')

def handle_uploaded_file(f, fileName):
    with open('tokenpass/static/upload/'+fileName, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def passUpdate(request):
    return render(request, 'updatepass.html')

def updateUserPass(request):
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
        
        # profile_pic = request.FILES['uploadFile']
        # splitName = os.path.splitext(profile_pic.name)
        # fileName = str(int(time.time()))+splitName[1]
        # handle_uploaded_file(profile_pic, fileName)

        updatestartlocation = request.POST['update_start_location']
        updateendloction = request.POST['update_end_location']
        update_reason = request.POST['update_reason']

        if firstname!='' and lastname!='' and contact!='' and email!='' and address!='' and city!='' and state!='' and dateofbirth!='' and startdate!='' and startlocation!='' and endlocation!='' and reason!='' and identitytype!='' and employeeid!='' and department!='' and updatestartlocation!='' and updateendloction!='' and update_reason!='':
            update_pass = updatepass(firstname=firstname,lastname=lastname,contact=contact,email=email,address=address,city=city,state=state,date_of_birth=dateofbirth,start_date=startdate,start_location=startlocation,end_location=endlocation,reason=reason,identity_type=identitytype,employee_id=employeeid,department=department,update_start_location=updatestartlocation,update_end_location=updateendloction,update_reason=update_reason)
            update_pass.save()
            messages.success(request, 'Pass Update Request generated successfully !!')
            return redirect(API+'/userhome/')
        else:
            messages.error(request, 'Something went wrong !!')
            return redirect(API+'/updatepass/')

def userhome(request):
    return render(request, 'userhome.html')

def applypassuser(request):
    return render(request, 'applypassuser.html')

def passhistory(request):
    return render(request, 'passhistory.html')

def adminHome(request):
    return render(request, 'adminHome.html')

def newrequestadmin(request):
    passes=applynewpass.objects.all()
    return render(request, 'newrequestadmin.html',{'passes':passes})

def assignauthority(request):
    return render(request, 'assignauthority.html')

def createauthority(request):
    return render(request, 'createauthority.html')

def authoritycreated(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']

    if firstname!='' and lastname!='' and username!='' and password!='' and email!='':
        add_auth = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password,is_staff='1')
        add_auth.save()
        messages.success(request, 'Authority Created successfully !!')
        return redirect(API+'/adminHome/')
    else:
        messages.error(request, 'Something went wrong !!')
        return redirect(API+'/createauthority/')

def requestfind(request):
    return render(request, 'requestfind.html')

def authorityhome(request):
    return render(request, 'authorityhome.html')    

def newrequestauthority(request):
    return render(request, 'newrequestauthority.html')

def checkhistoryauthority(request):
    return render(request, 'checkhistoryauthority.html')

def manageprofile(request):
    passes=applynewpass.objects.all()
    return render(request, 'manageprofile.html',{'passes':passes})    

