from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

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
