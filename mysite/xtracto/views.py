from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'xtracto/home.html')

def about(request):
    return render(request, 'xtracto/About-us.html')

def contact(request):
    return render(request, 'xtracto/contact.html')


def register(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            post = Registered()
            post.email= request.POST.get('email')
            post.password= request.POST.get('password')
            post.save()
            # mydictionary= {}
            # mydictionary['SuccessMsg'] = 'Form Submitted: You can now login'
            messages.success(request, 'You nhave been succefully registered')
            return render(request, 'xtracto/login.html', )
        else:
            return render(request,'xtracto/register.html')  

    else:        
        return render(request,'xtracto/register.html')


def login(request):
    if request.method == 'POST':
        if request.POST.get('email') and request.POST.get('password'):
            email =request.POST['email']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                email= user.email
                return render(request, 'xtracto/dashboard.html', {'email': email})  
            else:
                messages.error(request, 'Invalid details')
                return redirect('xtracto/home')
    return render(request, 'xtracto/loginfrontend.html')






def dashboard(request):
    return render(request, 'xtracto/dashboard.html')

def collections(request):
    return render(request, 'xtracto/collections.html')

def features(request):
    return render(request, 'xtracto/features.html')










def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("xtracto:homepage")
