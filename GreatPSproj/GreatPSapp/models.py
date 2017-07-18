from django.db import models
from accountapp.models import User



class Piano(models.Model):
    make = models.CharField(max_length=30)
    mod = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    serial_num = models.IntegerField()