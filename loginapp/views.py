from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Adv
#  your views here.,


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username,password=pass1)
        if user is not None:
           login(request,user)
           return redirect('home')
        else:
            messages.error(request,"ENTER VALID DATA")
    return render(request,'index.html')

@login_required(login_url='/signin')
def home(request):
    adv = Adv.objects.all()
    context ={
        'adv' : adv,
    }
    return render(request,'home.html', context )
    

def signout(request):
    logout(request)
    messages.success(request,"logged out succesfully")
    return redirect('signin')