from django.shortcuts import render
<<<<<<< HEAD:wedidit7/main_app/views.py
from .models import User
=======
from django.http import HttpResponse
import os
>>>>>>> master:main_app/views.py

# Create your views here.

def sign_up(request):
	user = User.objects.all()
	return render(request, 'signup.html', {'user': user})


<<<<<<< HEAD:wedidit7/main_app/views.py
=======
users = [
	User('Test', 'Mom', 1234567890, 'test@mom.com', 'sillymom', 'mom123', 'luke I am your mother'),
	User('Test2', 'Mom2', 9876543211, 'test2@mom.com', 'sillymom2', 'mom123', 'luke I am also your mother'),
	User('Test3', 'Mom3', 1234567878, 'test3@mom.com', 'sillymom3', 'mom123', 'luke I am also also your mother')
]
>>>>>>> master:main_app/views.py
