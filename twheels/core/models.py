from django.db import models

class Bike(models.Model):
	def __str__(self):
		return self.bike_model+str((self.depl_date))
	bike_model = models.CharField(max_length=200)
	depl_date = models.DateTimeField('Date Deployed')
	position_x = models.FloatField()
	position_y = models.FloatField()

class Customer(models.Model):
	def __str__(self):
		return self.name+' '+str(self.pan_id)
	pan_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length = 100)
	mem_join = models.DateTimeField('Date Joined')

class Transaction(models.Model):
	def __str__(self):
		return str(self.id)
	bike = models.ForeignKey(Bike)
	cust = models.ForeignKey(Customer)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField(null=True,blank=True)
	rate = models.IntegerField(default=10)
	
class Station(models.Model):
	name = models.CharField(default='Name',max_length=100)
	coordinates_x = models.FloatField()
	coordinates_y = models.FloatField()
	Incharge = models.CharField(max_length=100)
