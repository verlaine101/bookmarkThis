from django.db import models
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django import forms
from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.extras.widgets import SelectDateWidget    

class bookmarkEntry(models.Model):
	title=models.CharField(max_length=100)
	user=models.ForeignKey(User)
	summary=models.TextField(max_length=350)
	link=models.CharField(max_length=255)
	judgementDay=models.DateField()
	active=models.BooleanField()
	def __str__(self):
		return self.title
	def getBookmarksByDate(self,date,month,year):
		d=date(year,month,date)
		entries=bookmarkEntry.objects.filter(judgementDay=d)
		return entries	
	def getTodaysBookmarks(self):
		today=date.today()
		entries=bookmarkEntry.objects.filter(judgementDay=today)
		return entries
	def getRandomBookmarks(self,limit):
		today=date.today()
		entries=bookmarkEntry.objects.filter(judgementDay=today).order_by('?')[:limit]
		return entries
	def getRecentBookmarks(self,limit):
		entries=bookmarkEntry.objects.filter(active=True).order_by('id').reverse()[:limit]
		return entries		
				

#bookmark entry form
class bookmarkEntryForm(ModelForm):
	judgementDay=forms.DateField(widget=SelectDateWidget())
	class Meta:
		model = bookmarkEntry
		fields = ('title','summary','link','judgementDay')

class verdict(models.Model):
	verdict=models.CharField(max_length=60)
	def __str__(self):
		return self.verdict

class vote(models.Model):
	bookmarkEntry=models.ForeignKey(bookmarkEntry)
	user=models.ForeignKey(User)
	verdict=models.ForeignKey(verdict)
	def __str__(self):
		return self.verdict.verdict
	def registerVote(self,bookmark,user,verdict):
		existingVote=vote.objects.filter(bookmarkEntry=bookmark).filter(user=user)
		if existingVote:
			existingVote[0].verdict=verdict
			existingVote[0].save()
		else:
			newVote=vote(bookmarkEntry=bookmark,user=user,verdict=verdict)
			newVote.save()
			

