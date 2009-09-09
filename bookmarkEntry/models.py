from django.db import models
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django import forms
from django.forms import ModelForm
from django.forms.formsets import formset_factory

class bookmarkEntry(models.Model):
	title=models.CharField(max_length=100)
	user=models.ForeignKey(User)
	summary=models.TextField(max_length=350)
	link=models.CharField(max_length=255)
	judgementDay=models.DateField()
	active=models.BooleanField()
	def __str__(self):
		display=self.user.username+' '+str(self.judgementDay.day)+' '+str(self.judgementDay.month)
		return display
#bookmark entry form
class bookmarkEntryForm(ModelForm):
	
	class Meta:
		model = bookmarkEntry
		fields = ('title','summary','link','judgementDay')


