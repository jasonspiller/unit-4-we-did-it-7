from django.shortcuts import render
from .models import User

# Create your views here.

def sign_up(request):
	user = User.objects.all()
	return render(request, 'signup.html', {'user': user})


