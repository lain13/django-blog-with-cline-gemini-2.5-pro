from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Post, Category


class CategoryPostListViewTest(TestCase):
    """카테고리 필터링 목록 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        # Given
        User = get_user_model()
        cls.user = User.objects.create_user(username='categoryuser', password='password')
        cls.category_tech = Category.objects.create(name="Tech", slug="tech")
        cls.category_life = Category.objects.create(name="Life", slug="life")

        cls.post1 = Post.objects.create(title="Post 1 Tech", content="Content 1", author=cls.user, category=cls.category_tech)
        cls.post2 = Post.objects.create(title="Post 2 Life", content="Content 2", author=cls.user, category=cls.category_life)
        cls.post3 = Post.objects.create(title="Post 3 Tech", content="Content 3", author=cls.user, category=cls.category_tech)

    def test_view_url_accessible_by_name(self):
        """'post_list_by_category' URL name으로 뷰에 접근 가능한지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_category', args=[self.category_tech.slug]))
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """뷰가 올바른 템플릿(post_list.html)을 사용하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_category', args=[self.category_tech.slug]))
        # Then
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_filters_posts_by_category(self):
        """뷰가 카테고리에 따라 포스트를 올바르게 필터링하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_category', args=[self.category_tech.slug]))
        # Then
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)
        self.assertContains(response, self.post3.title)
        self.assertEqual(len(response.context['posts']), 2)

    def test_non_existent_category_returns_not_found(self):
        """존재하지 않는 카테고리로 접근 시 404를 반환하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_category', args=['non-existent-category']))
        # Then
        self.assertEqual(response.status_code, 404)
