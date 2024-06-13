from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from django.forms.widgets import DateInput # need to import

class UserRegisterForm(UserCreationForm):
      
        class Meta: 
            model = User
            fields = ['username','email','first_name','last_name','password1', 'password2', 'city','country','address', 'dob']

            widgets = {
                'dob': DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'input-field'})
            }
