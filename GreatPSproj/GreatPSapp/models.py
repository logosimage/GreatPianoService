from django.db import models
from accountapp.models import User


class Piano(models.Model):
    MODEL_CHOICES = (

        ('grand', 'Grand'),
        ('old upright', 'Old Upright'),
        ('console', 'Console'),
        ('studio', 'Studio'),
        ('spinet', 'Spinet')
    )

    REQUEST_CHOICES = (
        ('tune', 'Tune'),
        ('repair', 'Repair'),
        ('key services', 'Key Services'),
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

    def __str__(self):
        message = '{}\'s {} #{}'.format(self.client.username, self.make, self.client.customerID)
        return message


class Service_Record(models.Model):
    piano = models.ForeignKey(Piano)
    # last_serviced = models.DateField()
    date = models.DateField(null=True, blank=True)
    service_performed = models.CharField(max_length=255)
    service_hours = models.CharField(max_length=10)
    service_count = models.CharField(max_length=10)
    service_cost = models.CharField(max_length=10)
    service_notify = models.CharField(max_length=10)


class Service_Request(models.Model):
    tune = models.CharField(max_length=20, null=True, blank=True)
    regulation = models.CharField(max_length=20, null=True, blank=True)
    repair = models.CharField(max_length=20, null=True, blank=True)
    key_services = models.CharField(max_length=20, null=True, blank=True)
    cleaning = models.CharField(max_length=20, null=True, blank=True)
    appraisal = models.CharField(max_length=20, null=True, blank=True)
    humidity_control = models.CharField(max_length=20, null=True, blank=True)
    purchase_consulting = models.CharField(max_length=20, null=True, blank=True)





    annual_contract = models.CharField(max_length=20)




class Schedule_Appointment(models.Model):
    day = models.CharField(max_length=10)
    date = models.DateTimeField(null=True, blank=True)
