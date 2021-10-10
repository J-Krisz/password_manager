from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, EmailField
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Submit, Field, Fieldset, Layout
from crispy_forms.bootstrap import AppendedText

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
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'},),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'type': 'password', }), 
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }


    # TODO: start working on modals
    # TODO: password generator app