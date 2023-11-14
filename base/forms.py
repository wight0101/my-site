from django import forms
from .models import Room
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__' 
        exclude = ['participants']

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("name", "username", "email", "password1", "password2")