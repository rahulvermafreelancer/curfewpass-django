import email
from sre_parse import State
from django.db import models

# Create your models here.

class applynewpass(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    contact = models.IntegerField(max_length=10)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=10)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)