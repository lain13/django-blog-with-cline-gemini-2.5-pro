from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog.models import Post, Category

User = get_user_model()


class PaginationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        테스트를 위해 15개의 포스트 데이터를 생성합니다.
        """
        cls.user = User.objects.create_user(username="testuser", password="password")
        cls.category = Category.objects.create(name="Test Category", slug="test-category")
        for i in range(15):
            Post.objects.create(
                title=f"Test Post {i}",
                content=f"Test Content {i}",
                author=cls.user,
                category=cls.category,
            )

    def test_post_list_pagination(self):
        """
        PostListView에 페이지네이션이 올바르게 적용되었는지 테스트합니다.
        - 10개씩 페이징
        - 첫 페이지에는 10개의 포스트가 노출
        - 두 번째 페이지에는 5개의 포스트가 노출
        """
        # 첫 페이지 테스트
        response_page1 = self.client.get(reverse("blog:post_list"))
        self.assertEqual(response_page1.status_code, 200)
        self.assertTrue("page_obj" in response_page1.context)
        self.assertEqual(len(response_page1.context["page_obj"]), 10)

        # 두 번째 페이지 테스트
        response_page2 = self.client.get(reverse("blog:post_list"), {"page": 2})
        self.assertEqual(response_page2.status_code, 200)
        self.assertTrue("page_obj" in response_page2.context)
        self.assertEqual(len(response_page2.context["page_obj"]), 5)

    def test_invalid_page_number_raises_404(self):
        """
        잘못된 페이지 번호로 접근 시 404 에러가 발생하는지 테스트합니다.
        """
        # 숫자가 아닌 페이지 번호
        response_invalid = self.client.get(reverse("blog:post_list"), {"page": "abc"})
        self.assertEqual(response_invalid.status_code, 404)

        # 범위를 벗어난 페이지 번호
        response_out_of_range = self.client.get(reverse("blog:post_list"), {"page": 999})
        self.assertEqual(response_out_of_range.status_code, 404)
