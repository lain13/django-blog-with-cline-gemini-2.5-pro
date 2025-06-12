from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField

class SignupForm(UserCreationForm):
    captcha = CaptchaField()

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()
