from django.test import TestCase
from users.forms import SignupForm

class SignupFormTest(TestCase):
    def test_signup_form_invalid_without_captcha(self):
        """
        CAPTCHA 응답이 없는 경우 폼이 유효하지 않은지 테스트합니다.
        """
        form_data = {
            'username': 'testuser_captcha',
            'password': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('captcha', form.errors)
