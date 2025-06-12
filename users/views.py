from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm

class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'
