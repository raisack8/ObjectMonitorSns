from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm

# Create your views here.

class SignupView(CreateView):
  form_class = SignupForm
  template_name = "account/signup.html"
  model = User
  success_url = reverse_lazy('index')