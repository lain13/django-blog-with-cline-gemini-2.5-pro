from django.test import TestCase
from django.urls import reverse
from django.utils import translation

from blog.tests.helpers import create_user


class UserTemplateTest(TestCase):
    def setUp(self):
        self.user = create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

    def test_my_profile_link_in_base_template(self):
        """
        로그인 시 base.html 템플릿에 '내 프로필' 링크가 표시되는지 테스트
        """
        with translation.override("en"):
            # post_list 뷰는 base.html을 상속하므로, 이 페이지를 통해 테스트
            url = reverse("blog:post_list")
            response = self.client.get(url)
            profile_url = reverse(
                "users:profile_detail", kwargs={"username": self.user.username}
            )
            self.assertContains(response, f'href="{profile_url}"')
            self.assertContains(response, "My Profile")
