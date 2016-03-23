from django.db import models
from django.utils import timezone

class bikemodels(models.Model):
	bikemodel = models.CharField(max_length = 40,primary_key=True)
	def __unicode__(self):
		return self.bikemodel

class bike(models.Model):
	def __unicode__(self):
		return self.bikemodel+' '+str(self.id)
	bikemodel = models.ForeignKey(bikemodels)
	size = models.CharField(max_length = 1,choices = (('S','Small'),('M','Medium'),('L','Large')))
	date_deployed = models.DateField()
	date_inspected = models.DateField(blank = True,null = True)
	available = models.BooleanField(default = True)
	x_coordinate = models.FloatField(blank = True,null = True)
	y_coordinate = models.FloatField(blank= True, null = True)

class addr(models.Model):
	def __unicode__(self):
		return self.address_1
	address_1 = models.CharField(max_length = 128)
	address_2 = models.CharField(max_length = 128, blank = True)
	city = models.CharField(max_length = 64)
	state = models.CharField(max_length = 64)
	pin_code = models.CharField(max_length = 6)

class customer(models.Model):
	def __unicode__(self):
		return self.first_name + self.id_number
	ID_TYPES = (('PAN','PAN Card'),('ADH','Adhar Card'))
	id_type = models.CharField(max_length = 3,choices = ID_TYPES)
	id_number = models.CharField(max_length = 20)
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	email = models.EmailField()
	contact_num = models.CharField(max_length = 10)
	address = models.ForeignKey(addr)


class station(models.Model):
	x_coordinate = models.FloatField(blank = True,null = True)
	y_coordinate = models.FloatField(blank= True, null = True)
	address = models.ForeignKey(addr)

class transaction(models.Model):
	def __unicode__(self):
		return str(self.id)
	customer = models.ForeignKey(customer)
	bike = models.ForeignKey(bike)
	start = models.DateTimeField(default = timezone.now)
	end = models.DateTimeField(blank = True,null = True)
	start_stn = models.ForeignKey(station,related_name = 'Start_Station')
	end_stn = models.ForeignKey(station,blank = True,null = True)
