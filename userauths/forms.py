from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegisterForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username','email','first_name','last_name','password1', 'password2', 'city','country','address']
