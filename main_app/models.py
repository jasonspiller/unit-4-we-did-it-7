from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=13)
	email = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	motto = models.CharField(max_length=1000)

def __str__(self):
	return self.name 