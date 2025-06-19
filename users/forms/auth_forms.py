from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField
from users.models import User

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    captcha = CaptchaField()

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()
