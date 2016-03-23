from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Transaction,Bike,Station,Customer
from django.utils import timezone
from django.core.urlresolvers import reverse
 

def index(request):
	latest_transaction_list = Transaction.objects.order_by('-start_time')[:5]
	context = {'latest_transaction_list':latest_transaction_list}
	return render(request,'core/index.html',context)

def book(request):
	available_bikes = Bike.objects.all()
#	stations = Station.objects.all()
	customers = Customer.objects.all()
	context = { 'available_bikes' : available_bikes ,'customers':customers}
	return render(request, 'core/book.html',context)

def booki(request):
	bk = Bike.objects.get(id=request.POST['choice_bike'])
	cs = Customer.objects.get(pan_id=request.POST['choice_customer'])
	#st = Station.objects.get(id=request.POST['choice_station'])
	new_transaction = Transaction(bike=bk,cust=cs,start_time=timezone.now())
	new_transaction.save()
	return HttpResponseRedirect(reverse('core:index'))

def managetrans(request):
	trans = Transaction.objects.filter(end_time=None)
	context = { 'active_transactions' : trans }
	return render(request,'core/managetrans.html',context)
