from django.contrib import admin
from .models import Service, Appointment, CompanyInfo, BusinessHours, EmergencyContact, CounterStat

admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(CompanyInfo)
admin.site.register(BusinessHours)  
admin.site.register(EmergencyContact)
admin.site.register(CounterStat)