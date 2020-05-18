from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.widgets import DateInput, TextInput
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username')
