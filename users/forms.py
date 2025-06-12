from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

class SignupForm(UserCreationForm):
    captcha = CaptchaField()
