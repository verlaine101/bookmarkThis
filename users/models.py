from django.db import models
from django import forms

# Create your models here.
class RegistrationForm(forms.Form):
	username=forms.CharField(20,label=(u'User name'))
	emailaddress=forms.EmailField(100,label=(u'Email Address'))
	password1=forms.CharField(20,label=(u'Password'),widget=forms.PasswordInput) 
	password2=forms.CharField(20,label=(u'Repeat Password'),widget=forms.PasswordInput) 
