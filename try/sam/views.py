from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import regform,profileform
from .models import userprofile
from django.http import HttpResponse
def register(request):
	if request.method=='POST':
		print request.POST
		form = regform(request.POST,prefix='user')
		pform = profileform(request.POST,prefix='profile')
		if form.is_valid() and pform.is_valid():
			user=form.save()
			userprofile = pform.save(commit=False)
			userprofile.user = user
			userprofile.save()
			return HttpResponse("User Registered")
	else:
		form = regform(prefix='user')
		pform = profileform(prefix='profile')
	return render(request,'register.html',{'form':form,'profileform':pform})

