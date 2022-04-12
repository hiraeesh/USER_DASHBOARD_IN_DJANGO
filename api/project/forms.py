from django.contrib.auth.models import User
from django import forms
from .models import OurPatient
# from django.contrib.auth.forms import UserCreationForm

# class Doctor(UserCreationForm):
#  password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
#  class Meta:
#   model = User
#   fields = ['username', 'first_name', 'last_name', 'email']
#   labels = {'email': 'Email'}


  


class Patient(forms.ModelForm):
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
 class Meta:
  model =OurPatient
  fields = ['username', 'first_name','last_name','email','image','city','state','pincode','password']
  labels = {'username': 'username', 'first_name': 'Enter Name', 'last_name':'Last Name','email': 'Enter Email','image':'Profile Picture','city':'City','state':'state','pncode':'Pincode' }
  widgets = {'password':forms.PasswordInput} 



class Login(forms.Form):
    Username=forms.CharField()
    Password=forms.CharField()
    widgets = {'password':forms.PasswordInput} 

