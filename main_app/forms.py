"""Forms."""
from django import forms
from django.contrib.auth.models import User
from .models import Share


class ShareForm(forms.Form):
    """Share Form."""
    story = forms.CharField(max_length=1000, required=True)
    share_date = forms.DateTimeField(required=True)