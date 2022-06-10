from django.contrib import admin
from .models import Clients, Dogs, Employees, Reservation, Service
admin.site.register(Clients)
admin.site.register(Dogs)
admin.site.register(Employees)
admin.site.register(Reservation)
admin.site.register(Service)
