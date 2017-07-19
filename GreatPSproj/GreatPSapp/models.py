from django.db import models
from accountapp.models import User



class Piano(models.Model):
    MODEL_CHOICES = (

         ('grand','Grand'),
         ('upright', 'Upright'),
         ('studio','Studio'),
         ('spinet','Spinet')
    )

    make = models.CharField(max_length=30)
    mod = models.CharField(max_length=30, choices=MODEL_CHOICES)
    serial_num = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    client = models.ForeignKey(User)
    last_serviced = models.DateField(null=True, blank=True)
