"""Views."""
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
#from .models import User, Share
from django.views import generic
from django.contrib.auth.models import User


class SignUp(generic.CreateView):
    """Sign Up Form."""

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# def index(request):
# 	user = User.objects.all()
# 	form = SignUpForm()
# 	return render(request, 'index.html')

def storyline(request):
    """Storyline."""
    return render(request, 'storyline.html', {})


def profile(request):
    """Profile."""
    return render(request, 'profile.html', {})


def share(request):
    """Shareself."""
    return render(request, 'share.html', {})


def signin(request):
    """Sign In."""
    return render(request, 'signin.html', {})

def team(request):
    users = User.objects.all()
    return render(request, 'team.html' , {'users':users})
