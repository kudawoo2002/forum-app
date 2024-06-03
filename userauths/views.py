from django.shortcuts import render
from .forms import UserRegisterForm
# Create your views here.

def register_view(request):
    form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context=context)