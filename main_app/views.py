"""Views."""
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Share
from django.views import generic
from .forms import ShareForm
from django.contrib.auth.decorators import login_required


class SignUp(generic.CreateView):
    """Sign Up Form."""

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def storyline(request):
    """Storyline."""
    share = Share.objects.all()
    return render(request, 'storyline.html', {'share': share})


@login_required
def profile(request):
    """Profile."""
    return render(request, 'profile.html', {})


@login_required
def share(request):
    """Shareself."""
    share = Share.objects.all()
    form = ShareForm()
    return render(request, 'share.html', {'form': form, 'share': share})


def signin(request):
    """Sign In."""
    return render(request, 'signin.html', {})


def post_share(request):
    """Share Form."""
    form = ShareForm(request.POST)
    if form.is_valid():
        share = form.save(commit=False)
        share.user = request.user
        share.save()
    return HttpResponseRedirect('/storyline')


def team(request):
    """Team Page."""
    users = User.objects.all()
    return render(request, 'team.html', {'users': users})
