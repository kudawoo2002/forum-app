from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
import requests
# Create your views here.

def register_view(request):
    form = UserRegisterForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            print("Error in the form")
    return render(request, 'register.html', context=context)



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            return redirect("dashboard")
      
    context = {
       
    }
    
    return render(request, template_name='login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('login')
