from django.db import models
from accountapp.models import User



class Piano(models.Model):
    MODEL_CHOICES = (

         ('grand','Grand'),
         ('upright', 'Upright'),
         ('studio','Studio'),
         ('spinet','Spinet')
    )

    REQUEST_CHOICES = (


        ('tune', 'Tune'),
        ('repair', 'Repair'),
        ('regulation', 'Regulation'),
        ('voicing', 'Voicing'),
        ('cleaning', 'Cleaning'),
        ('restoration', 'Restoration'),
        ('appraisal', 'Appraisal'),
        ('purchase evaluation', 'Purchasing Evaluation'),
        ('humidity control', 'Humidity Control'),
        ('annual contract', 'Annual Contract')


    )
    make = models.CharField(max_length=30)
    mod = models.CharField(max_length=30, choices=MODEL_CHOICES)
    serial_num = models.CharField(max_length=30, null=True, blank=True)
    size = models.CharField(max_length=30, null=True, blank=True)
    client = models.ForeignKey(User)
    last_serviced = models.DateField(null=True, blank=True)
    service_request = models.CharField(max_length=30, choices=REQUEST_CHOICES, null=True, blank=True)









