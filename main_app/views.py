from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.decorators import login_required
from .models import User
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm

# Create your views here.

# def index(request):
# 	return render(request, 'index.html')

# def sign_up(request):
# 	user = User.objects.all()
# 	form = SignUpForm()
# 	return render(request, 'signup.html', {'user': user, 'form': form})

def index(request):
	user = User.objects.all()
	form = SignUpForm()
	return render(request, 'signup.html', {'user': user, 'form': form})

# @login_required
# def home(request):
# 	return render(request, 'index.html')

def show(request, user_id):
	user = User.objects.get(id=user_id)
	return render(request, 'profile.html', {'user': user})

def signup(request):
	form = SignUpForm(request.POST)
	if form.is_valid():
		user = User (
			first_name = form.cleaned_data['first_name'],
			last_name = form.cleaned_data['last_name'],
			username = form.cleaned_data['username'],
			email = form.cleaned_data['email'],
			password = form.cleaned_data['password'],
			phone = form.cleaned_data['phone'],
			motto = form.cleaned_data['motto'])
		user.user = request.user
		user.save()
	return HttpResponseRedirect('/')