"""Forms."""
from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    """Sign Up Form."""

    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=100, required=True)
    phone = forms.IntegerField(required=True)
    email = forms.CharField(max_length=100, required=True)
    motto = forms.CharField(max_length=1000, required=False)


class ShareForm(forms.Form):
    """Share Form."""

    #user = forms.ForeignKey(User)
    # story = forms.TextField(required=True)
    # post_date = forms.DateTimeField(required=True)
    # media = forms.TextField(required=True)
    # share_date = forms.DateTimeField(required=True)
