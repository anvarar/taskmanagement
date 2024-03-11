from django import forms
from django.contrib.auth.models import User 
from .models import add_details
class loginform(forms.ModelForm):
    username=forms.CharField()
    class Meta:
        model=User
        fields=['username','email','password']


class addtask(forms.ModelForm):
    class Meta:
        model=add_details 
        fields='__all__'