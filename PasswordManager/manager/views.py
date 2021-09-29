import requests
import json
import string
import hashlib
import base64

from django.db import IntegrityError

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, EditView, FormView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.urls import reverse_lazy

# Create your views here.
