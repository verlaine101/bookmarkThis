from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from bookmarkThis.users.models import RegistrationForm
def register(request):
	if request.method == 'POST':
		regform=RegistrationForm(request.POST)
		if regform.is_valid():
			if request.POST['password1']==request.POST['password1']:
				newUser=User.objects.create_user(request.POST['username'],request.POST['emailaddress'],request.POST['password1'])
				newUser.save()
				user = authenticate(username=newUser.username, password=newUser.password)
				login(request,user)
				return HttpResponseRedirect('/thanks/')
	else:
		regform=RegistrationForm()
	return render_to_response('registration/register.html',{'regform':regform})
