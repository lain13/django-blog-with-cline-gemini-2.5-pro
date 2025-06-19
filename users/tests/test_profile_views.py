from django.test import TestCase
from django.urls import reverse
from django.utils import translation

from blog.tests.helpers import create_user


class ProfileUpdateViewTest(TestCase):
    def setUp(self):
        self.user = create_user(username='testuser', password='password123')
        self.other_user = create_user(username='otheruser', password='password123')
        with translation.override('en'):
            self.url = reverse('users:profile_update', kwargs={'username': self.user.username})

    def test_redirects_if_not_logged_in(self):
        """
        로그인하지 않은 경우 로그인 페이지로 리다이렉트되는지 테스트
        """
        response = self.client.get(self.url)
        self.assertRedirects(response, f'/en/users/login/?next={self.url}')

    def test_forbidden_if_editing_another_user_profile(self):
        """
        다른 사용자의 프로필을 수정하려고 할 때 403 Forbidden을 반환하는지 테스트
        """
        self.client.login(username='otheruser', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_profile_update_view_returns_200_for_owner(self):
        """
        프로필 소유자가 접근 시 200 OK를 반환하는지 테스트
        """
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_profile_update_view_uses_correct_template(self):
        """
        프로필 수정 뷰가 올바른 템플릿을 사용하는지 테스트
        """
        self.client.login(username='testuser', password='password123')
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'users/profile_form.html')

    def test_profile_update_successfully(self):
        """
        프로필이 성공적으로 업데이트되는지 테스트
        """
        self.client.login(username='testuser', password='password123')
        new_bio = "This is an updated bio."
        response = self.client.post(self.url, {'bio': new_bio})

        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.bio, new_bio)
        with translation.override('en'):
            expected_redirect_url = reverse('users:profile_detail', kwargs={'username': self.user.username})
        self.assertRedirects(response, expected_redirect_url)


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
