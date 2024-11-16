from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser 

class CustomUser CreationForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ('username', 'email', 'password1', 'password2', 'bio', 'profile_picture')