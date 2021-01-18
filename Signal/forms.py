
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

colour_choices = [('',''),('red','red'),('yellow','yellow'),('blue','blue'),('multi','multi'),]
flash_choices = [('',''),('fixed','fixed'),('flashing','flashing'),('occulting','occulting'),]

class mainForm(ModelForm):
    class Meta:
        model = Signal
        fields = '__all__'

        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=colour_choices, attrs={'class':'form-control'}),
            'colour': forms.Select(choices=colour_choices, attrs={'class':'form-control'}),
            'flash_type': forms.Select(choices=flash_choices, attrs={'class':'form-control'}),
        }

