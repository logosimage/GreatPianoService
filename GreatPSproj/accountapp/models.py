from django.db import models
from django.contrib.auth.models import AbstractUser





class User(AbstractUser):
    

    REQUIRED_FIELDS = ['email',]
 
    email = models.EmailField()

    cell_phone= models.CharField(max_length=20, null=True, blank=True)

    work_phone = models.CharField(max_length=20, null=True, blank=True)

    home_phone = models.CharField(max_length=20, null=True, blank=True)

    address = models.CharField(max_length=20, null=True, blank=True)

    city = models.CharField(max_length=20, null=True, blank=True)

    state = models.CharField(max_length=20, null=True, blank=True)

    zip = models.CharField(max_length=20, null=True, blank=True)

    customerID = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self,):
        return self.email










