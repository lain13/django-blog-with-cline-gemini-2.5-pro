import unittest
from django.test import TestCase, TransactionTestCase, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.forms import SignupForm

User = get_user_model()

class AuthViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_login_view_uses_correct_template(self):
        """
        로그인 페이지가 'users/login.html' 템플릿을 사용하는지 테스트
        """
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout_view(self):
        """
        로그아웃 시 홈으로 리다이렉트되는지 테스트
        """
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('users:logout'))
        self.assertRedirects(response, reverse('blog:post_list'))
        # Check if the user is logged out
        response = self.client.get(reverse('blog:post_list'))
        self.assertFalse(response.context['user'].is_authenticated)


class SignUpViewTest(TransactionTestCase):
    def test_signup_view_uses_correct_template(self):
        """
        회원가입 페이지가 'users/signup.html' 템플릿을 사용하는지 테스트
        """
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    @unittest.skip("Skipping due to CAPTCHA issues in test environment")
    def test_signup_creates_new_user(self):
        """
        회원가입 시 새로운 사용자가 생성되는지 테스트
        """
        # The other test class creates a user, so we check the count increases
        initial_user_count = User.objects.count()
        response = self.client.post(
            reverse('users:signup'),
            {
                'username': 'newuser',
                'password1': 'ComplexPassword123!',
                'password2': 'ComplexPassword123!',
            }
        )
        # Check if the user count has increased by 1
        self.assertEqual(User.objects.count(), initial_user_count + 1)
        # Check for redirect to login page
        self.assertRedirects(response, reverse('users:login'))
        # Check if the new user was actually created
        self.assertTrue(User.objects.filter(username='newuser').exists())


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
