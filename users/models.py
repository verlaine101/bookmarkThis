from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    twitterId = models.CharField(null=True, blank=True,max_length=20)
    facebookId = models.CharField(null=True, blank=True,max_length=20)
    emailReminder = models.BooleanField()
    user = models.ForeignKey(User, unique=True)

class RegistrationForm(forms.Form):
	username=forms.CharField(20,label=(u'User name'))
	emailaddress=forms.EmailField(100,label=(u'Email Address'))
	password1=forms.CharField(20,label=(u'Password'),widget=forms.PasswordInput) 
	password2=forms.CharField(20,label=(u'Repeat Password'),widget=forms.PasswordInput) 

class UserProfileForm(ModelForm):

	class Meta:
		model = UserProfile
		fields = ('twitterId','facebookId','emailReminder')
