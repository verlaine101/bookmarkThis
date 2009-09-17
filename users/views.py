from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from bookmarkThis.users.models import RegistrationForm, UserProfileForm, UserProfile
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		regform=RegistrationForm(request.POST)
		if regform.is_valid():
			if request.POST['password1']==request.POST['password2']:
				newUser=User.objects.create_user(request.POST['username'],request.POST['emailaddress'],request.POST['password1'])
				newUser.save()
				userProfile=UserProfile()
				userProfile.user=newUser
				userProfile.save()
				user = authenticate(username=request.POST['username'], password=request.POST['password1'])
				login(request,user)
				return HttpResponseRedirect('/accounts/user-profile/')
	else:
		regform=RegistrationForm()
	return render_to_response('accounts/register.html',{'regform':regform})

@login_required
def userProfile(request):
	up=UserProfile.objects.get(user=request.user)		
	if request.method == 'POST':
		profileForm=UserProfileForm(request.POST,instance=up)
		if profileForm.is_valid():
			profileForm.save()
			return HttpResponseRedirect('/accounts/profile-updated/')
	else:
		profileForm=UserProfileForm(instance=up)
	return render_to_response('accounts/user-profile.html',{'profileForm':profileForm})			
