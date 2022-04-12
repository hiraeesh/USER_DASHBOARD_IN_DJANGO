
from email.policy import default
from django.db import models

# Create your models here.

class OurPatient(models.Model):
 username = models.CharField(max_length=100)
 first_name = models.CharField(max_length=100)
 last_name = models.CharField(max_length=100)
 email = models.EmailField(max_length=100)
 image = models.ImageField(default=None, upload_to='images')  


 
 city= models.CharField(default=None,max_length=40)
 state=models.CharField(default=None,max_length=40)
 pincode=models.IntegerField(default=None)
 password = models.CharField(max_length=100)

