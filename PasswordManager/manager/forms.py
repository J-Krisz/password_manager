from django.contrib.auth.models import User
from django.forms import ModelForm, EmailField
from django.contrib.auth.forms import UserCreationForm
from .models import Account 


class UserRegistrationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['title', 'username', 'email', 'password', 'url', 'notes']

