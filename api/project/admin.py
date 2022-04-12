from django.contrib import admin
from .models import OurPatient

# Register your models here.
@admin.register(OurPatient)
class Student(admin.ModelAdmin):
      list_display=[
    'username',
    'first_name',
    'last_name',
    'email',
  
    'city',
    'state',
    'pincode',
       
      ]