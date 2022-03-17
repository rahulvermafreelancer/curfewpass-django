from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def header(request):
    return render(request, 'header.html')    

def userheader(request):
    return render(request, 'userheader.html')

def adminheader(request):
    return render(request, 'adminheader.html')