from django.shortcuts import render

from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm

class CustomSignup(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = 'tasks'
