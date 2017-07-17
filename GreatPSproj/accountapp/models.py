from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    My custom user model.
    first_name,
    """

    REQUIRED_FIELDS = ['email',]

    email = models.EmailField()

    def __str__(self):
        return self.email
class Piano(models.Model):
    make = models.CharField(max_length=30)
    mod = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    serial_num = models.IntegerField()







