from django.contrib import admin
from .models import Piano, Service_Record, Service_Request, Scheduling
# Register your models here.
admin.site.register(Piano)
admin.site.register(Service_Record)
admin.site.register(Service_Request)
admin.site.register(Scheduling)
