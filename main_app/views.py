"""Views."""
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
#from .models import User, Share
from django.views import generic
#from .forms import SignUpForm, ShareForm


class SignUp(generic.CreateView):
    """Sign Up Form."""

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def index(request):
    """Sign Up Form."""
    user = User.objects.all()
    form = SignUpForm()
    return render(request, 'signup.html', {'user': user, 'form': form})


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


def post_share(request):
    """Share Form."""
    form = ShareForm(request.POST)
    if form.is_valid():
        share = Share(
            #user=user,
            story=form.cleaned_data['story'],
            post_date=form.cleaned_data['post_date'],
            media=form.cleaned_data['media'],
            share_date=form.cleaned_data['share_date'])
        share.share = request.share
        share.save()
    return HttpResponseRedirect('/')
