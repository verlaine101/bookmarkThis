from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from bookmarkThis.bookmarkEntry.models import bookmarkEntry,bookmarkEntryForm

@login_required
def createBookmark(request):
	if request.POST:
		entryForm=bookmarkEntryForm(request.POST)
		if entryForm.is_valid():
			entry=bookmarkEntry()
			entry.user=request.user
			entry.title=request.POST['title']
			entry.summary=request.POST['summary']
			entry.title=request.POST['link']
			entry.judgementDay=request.POST['judgementDay']
			entry.active=1
			entry.save()
			return HttpResponseRedirect('/thanks/')
	else:
		entryForm=bookmarkEntryForm()
	return render_to_response('bookmarkEntry.html',{'entryForm':entryForm})
			
			
	
	
