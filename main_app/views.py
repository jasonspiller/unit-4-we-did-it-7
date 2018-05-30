"""Views."""
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import User, Share
from django.views import generic



class SignUp(generic.CreateView):
    """Sign Up Form."""

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# def post_share(request):
#     """Share Form."""
#     form = ShareForm(request.POST)
#     if form.is_valid():
#         share = Share(
#             #user=user,
#             story=form.cleaned_data['story'],
#             post_date=form.cleaned_data['post_date'],
#             media=form.cleaned_data['media'],
#             share_date=form.cleaned_data['share_date'])
#         share.share = request.share
#         share.save()
#     return HttpResponseRedirect('/')
