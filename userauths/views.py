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
    weather = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            weather = ""    
            api_key = "a71b7607817b263c56b4d69a7f4b5cd9"
            
            login(request, user)
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user.city}&appid=a71b7607817b263c56b4d69a7f4b5cd9")
            data = response.json()
            print(data)
            weather = data["weather"][0]['main']
            
            print(user.city)
            return redirect("home")
        else:
            print("invalide")
    print(weather)
    context = {
        'weather': weather,
    }
    
    return render(request, template_name='login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('login')