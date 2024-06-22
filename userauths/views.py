from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
import requests
from decouple import config
# Create your views here.

def dashboard(request):
    list_weather = {
        "Rain":"#127783",
        "Clouds": "#127783",
        "Clear":"#127780",
        "Sun":"#127781"
    }
    city_name = request.user.city
    api_key = config("weather_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    weather = list_weather[data["weather"][0]["main"]]
    temp = data["main"]['temp'] / 10

    context = {
        'weather': weather,
        'temp':temp
    }
    return render(request, 'dashboard.html', context)

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
