from django.core import validators
from django.forms import widgets, fields
from django import forms
from .models import LoginInfo

class StudentrRegistration(forms.ModelForm):
    class Meta:
        model=LoginInfo
        fields= ['username', 'password', 'email']
        widgets={
            'username': forms.TextInput( attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            'email': forms.EmailInput(   attrs={'class':'form-control'})
            
        }
