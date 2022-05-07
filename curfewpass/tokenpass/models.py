import email
from sre_parse import State
from statistics import mode
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
    start_date = models.DateField()
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    reason = models.CharField(max_length=500)
    identity_type = models.CharField(max_length=15)
    employee_id = models.CharField(max_length=50)
    department = models.CharField(max_length=30)
    photo = models.CharField(max_length=30)


class updatepass(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    contact = models.IntegerField(max_length=10)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=10)
    start_date = models.DateField()
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    reason = models.CharField(max_length=500)
    identity_type = models.CharField(max_length=15)
    employee_id = models.CharField(max_length=50)
    department = models.CharField(max_length=30)
    photo = models.CharField(max_length=30)
    update_start_location =models.CharField(max_length=100)
    update_end_location = models.CharField(max_length=100)
    update_reason = models.CharField(max_length=500)


class userprofile(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    contact = models.IntegerField(max_length=10)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    photo = models.CharField(max_length=30)


class addauthority(models.Model):
    authority_name = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    contact = models.IntegerField(max_length=10)
