from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class event(models.Model):
	Manager_Name=models.CharField(max_length=50)
	Event_title=models.CharField(max_length=20)
	Event_venue=models.CharField(max_length=10)
	Event_Details=models.TextField(max_length=500)
	Event_date=models.DateTimeField( default='dd/mm/yyyy 00:00:00',blank=False)
	Email=models.EmailField(blank=False, default="")
	Contact=models.IntegerField(default="")
	

	
	



# Create your models here.
