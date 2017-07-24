from django.db import models
from accountapp.models import User


class Tech_entry(models.Model):
    client = models.ForeignKey(User, null=True, blank=True)
    entry_date = models.DateTimeField(null=True, blank=True)
    record_entry = models.CharField(max_length=255)
    tuning_notes = models.CharField(max_length=255)
    repairs = models.CharField(max_length=255)

    # def __str__(self):
    #     message = '{}\'s {} #{}'.format(self.client.username, self.make, self.client.customerID)
    #     return message




