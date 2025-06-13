from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView as AuthLoginView
from ..forms import SignupForm, LoginForm

class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

class LoginView(AuthLoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
