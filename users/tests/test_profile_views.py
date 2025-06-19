from django.test import TestCase
from django.urls import reverse
from django.utils import translation

from blog.tests.helpers import create_user

class ProfileDetailViewTest(TestCase):
    def setUp(self):
        self.user = create_user(username='testuser', password='password123')

    def test_profile_detail_view_returns_200_for_valid_user(self):
        """
        프로필 상세 뷰가 유효한 사용자에 대해 200 OK를 반환하는지 테스트
        """
        with translation.override('en'):
            url = reverse('users:profile_detail', kwargs={'username': self.user.username})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_view_uses_correct_template(self):
        """
        프로필 상세 뷰가 올바른 템플릿을 사용하는지 테스트
        """
        with translation.override('en'):
            url = reverse('users:profile_detail', kwargs={'username': self.user.username})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'users/profile_detail.html')

    def test_profile_detail_view_contains_profile_data(self):
        """
        프로필 상세 뷰의 컨텍스트에 올바른 프로필 데이터가 포함되어 있는지 테스트
        """
        with translation.override('en'):
            url = reverse('users:profile_detail', kwargs={'username': self.user.username})
        response = self.client.get(url)
        self.assertEqual(response.context['profile'], self.user.profile)
        self.assertEqual(response.context['profile'].user, self.user)
