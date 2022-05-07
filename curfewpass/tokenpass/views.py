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

def applypass(request):
    return render(request, 'applypass.html')

def updatepass(request):
    return render(request, 'updatepass.html')

def passhistory(request):
    return render(request, 'passhistory.html')
