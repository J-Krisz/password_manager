import requests
import json
import string
import hashlib
import base64

from django.db import IntegrityError
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import  CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import AccountForm, UserRegistrationForm
from .models import Account


class LandingPageView(TemplateView):
    template_name = 'manager/index.html'
    model = Account

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'manager/sign_up_form.html'
    form_class = UserCreationForm
    success_message = 'Your account was created successfully'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'manager/login_form.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('accounts')
    
class AddNewAccountView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'manager/add_accounts.html'


class AccountListView(LoginRequiredMixin, ListView):
    template_name = 'manager/accounts.html'
    model = Account
    context_object_name = 'accounts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = context['accounts'].filter(user=self.request.user)
        return context


# class AccountDetailView(LoginRequiredMixin, DetailView):
#     pass


class EditAccountView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'manager/edit_account.html'
    success_url = reverse_lazy('accounts')



class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    context_object_name = 'account'
    success_url = reverse_lazy('accounts')

