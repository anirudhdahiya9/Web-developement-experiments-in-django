from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import RegBike
from django.contrib.auth import authenticate, login

def login(request):
	print request.POST
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request,user)
		else:
			#return an error message
	else:
		#Return an invalid login error message

def logout(request):
	logout(request)
	#redirect

def index(request):
	return render(request,'core/index.html')

def makebooking(request):
	available_bikes = bike.objects.filter(available = True)
	start_station = station.objects.all()
	customers = customer.objects.exclude(transaction__isnull=True)
	#customers = customer.objects.all()
	context = {'available_bikes':available_bikes,'start_station':start_station,'customer':customer}
	return render(request,'core/makebooking.html',context)

def regbike(request):
	bikes = bike.objects.all()
	if request.method == 'POST':
		form = RegBike(request.POST)
		if form.is_valid():
			print form.cleaned_data
			b1 = bike(bikemodel=form.cleaned_data['bikemodel'],size=form.cleaned_data['size'],date_deployed=form.cleaned_data['date_deployed'])
			b1.save()
	else:
		form = RegBike()
		
	return render(request,'core/regbike.html',{'form':form,'bikes':bikes})
