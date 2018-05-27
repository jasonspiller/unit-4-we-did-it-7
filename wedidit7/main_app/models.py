from django.db import models

# Create your models here.
first_name, last_name, phone, email, username, password, motto

class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=13)
	email = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	motto = models.CharField(max_length=1000)
