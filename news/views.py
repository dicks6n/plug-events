from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
   
    return render(request, 'news/home.html')


def about(request):
    return render(request, 'news/about.html')


def blog(request):
    return render(request, 'news/blog.html') 

@login_required(login_url='login/')
def login (request):
    return render(request ,'login.html')   

@login_required(login_url='register/')
def register (request):
    return render(request ,'register.html')   
