from django.db import models

# Create your models here.
class register(models.Model):
    firstname= models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    contact_number = models.IntegerField()
    status = models.IntegerField(max_length=5,default='1')
    role = models.CharField(max_length=255,default="user")
    created_date = models.DateTimeField(auto_now_add=True)