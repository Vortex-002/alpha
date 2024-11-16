from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import CustomUser 
from django.contrib.auth.admin import UserAdmin

class CustomUser Admin(UserAdmin):
    model = CustomUser 
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    ordering = ['username']

admin.site.register(CustomUser , CustomUser Admin)