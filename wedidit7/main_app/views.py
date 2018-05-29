from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
from django.http import HttpResponseRedirect
from main_app.forms import SignUpForm

# Create your views here.

def index(request):
	return render(request, 'index.html')

@login_required
def home(request):
	return render(request, 'index.html')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			form.save()
			login(request, user)
			return HttpResponseRedirect('home')
	else: 
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})



