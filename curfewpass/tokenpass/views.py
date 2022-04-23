from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginpage(request):
    return render(request, 'login.html')
    
def register(request):
    return render(request, 'register.html')

def registerUser(request):
    if request.method=='POST':
        return HttpResponse("working")

def userhome(request):
    return render(request, 'userhome.html')