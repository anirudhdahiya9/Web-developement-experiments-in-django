from django.contrib import admin

from .models import bike,transaction,station,customer,addr
admin.site.register(bike)
admin.site.register(transaction)
admin.site.register(station)
admin.site.register(customer)
admin.site.register(addr)

