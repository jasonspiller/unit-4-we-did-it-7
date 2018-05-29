"""Views."""
from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.decorators import login_required
from .models import User, Share
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, ShareForm


def index(request):
    """Sign Up Form."""
    user = User.objects.all()
    form = SignUpForm()
    return render(request, 'signup.html', {'user': user, 'form': form})

# @login_required
# def home(request):
# 	return render(request, 'index.html')


def show(request, user_id):
    """Show User."""
    user = User.objects.get(id=user_id)
    return render(request, 'profile.html', {'user': user})


def signup(request):
    """Sign Up Form."""
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = User(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            phone=form.cleaned_data['phone'],
            motto=form.cleaned_data['motto'])
        user.user = request.user
        user.save()
    return HttpResponseRedirect('/')


def share(request):
    """Share Form."""
    form = ShareForm(request.POST)
    if form.is_valid():
        share = Share(
            user_id=form.cleaned_data['share_date'],
            story=form.cleaned_data['story'],
            post_date=form.cleaned_data['post_date'],
            media=form.cleaned_data['media'],
            share_date=form.cleaned_data['share_date'])
        share.share = request.share
        share.save()
    return HttpResponseRedirect('/')
