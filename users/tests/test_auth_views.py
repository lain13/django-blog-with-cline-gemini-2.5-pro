import unittest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import translation
from captcha.conf import settings as captcha_settings
from blog.tests.helpers import create_user

User = get_user_model()

class AuthViewTest(TestCase):
    def setUp(self):
        self.user = create_user(username='testuser', password='password123')

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

    def test_login_fails_without_captcha(self):
        """
        CAPTCHA 없이 로그인 시도 시 실패하는지 테스트
        """
        with translation.override('en'):
            response = self.client.post(reverse('users:login'), {
                'username': 'testuser',
                'password': 'password123',
            })
        self.assertEqual(response.status_code, 200)
        # Manually check for form errors to bypass potential assertFormError issues
        form = response.context.get('form')
        self.assertIsNotNone(form)
        self.assertTrue(form.is_bound)
        self.assertIn('captcha', form.errors)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_login_succeeds_with_captcha(self):
        """
        올바른 CAPTCHA로 로그인 시도 시 성공하는지 테스트
        """
        captcha_settings.CAPTCHA_TEST_MODE = True
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'password123',
            'captcha_0': 'passed',
            'captcha_1': 'passed',
        })
        self.assertRedirects(response, reverse('blog:post_list'))
        # Check if the user is logged in by checking a subsequent request
        response = self.client.get(reverse('blog:post_list'))
        self.assertTrue(response.context['user'].is_authenticated)
        captcha_settings.CAPTCHA_TEST_MODE = False


class SignUpViewTest(TestCase):
    def test_signup_view_uses_correct_template(self):
        """
        회원가입 페이지가 'users/signup.html' 템플릿을 사용하는지 테스트
        """
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signup_creates_new_user(self):
        """
        회원가입 시 새로운 사용자가 생성되는지 테스트 (CAPTCHA 테스트 모드 활성화)
        """
        captcha_settings.CAPTCHA_TEST_MODE = True
        initial_user_count = User.objects.count()
        response = self.client.post(
            reverse('users:signup'),
            {
                'username': 'newuser',
                'password1': 'ComplexPassword123!',
                'password2': 'ComplexPassword123!',
                'captcha_0': 'passed',
                'captcha_1': 'passed',
            }
        )
        captcha_settings.CAPTCHA_TEST_MODE = False

        # Check if the user count has increased by 1
        self.assertEqual(User.objects.count(), initial_user_count + 1)
        # Check for redirect to login page
        self.assertRedirects(response, reverse('users:login'))
        # Check if the new user was actually created
        self.assertTrue(User.objects.filter(username='newuser').exists())
