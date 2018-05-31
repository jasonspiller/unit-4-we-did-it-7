"""Forms."""
from django import forms
from django.contrib.auth.models import User
from .models import Share


class ShareForm(forms.ModelForm):
	"""Share Form."""
	class Meta:
		model = Share
		fields = ['story', 'share_date']

