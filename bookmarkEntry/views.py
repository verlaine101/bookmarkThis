from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from datetime import date
from bookmarkThis.bookmarkEntry.models import bookmarkEntry,bookmarkEntryForm,verdict,vote
import string
@login_required
def createBookmark(request):
	if request.POST:
		entryForm=bookmarkEntryForm(request.POST)
		if entryForm.is_valid():
			entry=bookmarkEntry()
			entry.user=request.user
			entry.title=request.POST['title']
			entry.summary=request.POST['summary']
			entry.link=request.POST['link']
			inputDate=request.POST['judgementDay'].split('/')
			entry.judgementDay=inputDate[2]+'-'+inputDate[1]+'-'+inputDate[0]
			entry.active=1
			entry.save()
			return HttpResponseRedirect('/thanks/')
	else:
		entryForm=bookmarkEntryForm()
	return render_to_response('bookmarkEntry.html',{'entryForm':entryForm})
			
def default(request):
	bookmarkObj=bookmarkEntry()
	todaysBookmarks	= bookmarkObj.getTodaysBookmarks()
	recentBookmarks = bookmarkObj.getRecentBookmarks(5)
	return render_to_response('index.html',{'todaysBookmarks':todaysBookmarks,'recentBookmarks':recentBookmarks})
	
def bookmarkDetail(request,bookmark_id,verdictInput=None):
	entry=bookmarkEntry.objects.get(id=bookmark_id)
	if verdictInput:
		userVerdict=verdict.objects.get(id=verdictInput)
		voteObj=vote()
		voteObj.registerVote(entry,request.user,userVerdict)
	return render_to_response('entry.html',{'entry':entry, 'user':request.user, 'verdict': verdictInput})


