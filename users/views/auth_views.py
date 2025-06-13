from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView as AuthLoginView
from .. import forms

class SignUpView(generic.CreateView):
    form_class = forms.SignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

class LoginView(AuthLoginView):
    form_class = forms.LoginForm
    template_name = 'users/login.html'
