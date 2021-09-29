from django.forms import ModelForm
from .models import Account 

class AccountForm(ModelForm):
    class Meta:
        models = Account
        fields = ['title', 'username', 'email', 'password', 'link']

