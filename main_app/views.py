from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'index.html', {'users': users})

class User:
	def __init__(self, first_name, last_name, phone, email, username, password, motto):
		self.first_name = first_name
		self.last_name = last_name
		self.phone = phone
		self.email = email
		self.username = username
		self.password = password
		self.motto = motto

users = [
	User('Test', 'Mom', 1234567890, 'test@mom.com', 'sillymom', 'mom123', 'luke I am your mother'),
	User('Test2', 'Mom2', 9876543211, 'test2@mom.com', 'sillymom2', 'mom123', 'luke I am also your mother'),
	User('Test3', 'Mom3', 1234567878, 'test3@mom.com', 'sillymom3', 'mom123', 'luke I am also also your mother')
]