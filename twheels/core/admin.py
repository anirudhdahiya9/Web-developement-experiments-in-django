from django.contrib import admin
from .models import Bike, Customer, Transaction, Station

class TAdmin(admin.ModelAdmin):
	list_display = ('id','start_time','end_time','bike','rate')

admin.site.register(Bike)
admin.site.register(Customer)
admin.site.register(Transaction, TAdmin)
admin.site.register(Station)
