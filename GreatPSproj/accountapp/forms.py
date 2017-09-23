from django import forms
from django.contrib.auth.forms import UserCreationForm
from accountapp.models import User
from django.contrib.auth.models import auth


class CustomUserCreationForm(UserCreationForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields + ( 'email', 'password')
