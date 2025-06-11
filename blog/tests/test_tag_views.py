from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Post, Tag


class TagFilteredListViewTest(TestCase):
    """태그 필터링 목록 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        # Given
        User = get_user_model()
        cls.user = User.objects.create_user(username='taguser', password='password')
        cls.tag_python = Tag.objects.create(name="python")
        cls.tag_django = Tag.objects.create(name="django")

        cls.post1 = Post.objects.create(title="Post 1", content="Content 1", author=cls.user)
        cls.post1.tags.add(cls.tag_python)

        cls.post2 = Post.objects.create(title="Post 2", content="Content 2", author=cls.user)
        cls.post2.tags.add(cls.tag_django)

        cls.post3 = Post.objects.create(title="Post 3", content="Content 3", author=cls.user)
        cls.post3.tags.add(cls.tag_python, cls.tag_django)

    def test_view_url_exists_at_desired_location(self):
        """태그 필터링 뷰 URL에 접근 시 200 응답을 반환하는지 테스트"""
        # When
        response = self.client.get(f'/tag/{self.tag_python.name}/')
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """'post_list_by_tag' URL name으로 뷰에 접근 가능한지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_tag', args=[self.tag_python.name]))
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """뷰가 올바른 템플릿(post_list.html)을 사용하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_tag', args=[self.tag_python.name]))
        # Then
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_filters_posts_by_tag(self):
        """뷰가 태그에 따라 포스트를 올바르게 필터링하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_tag', args=[self.tag_python.name]))
        # Then
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)
        self.assertContains(response, self.post3.title)
        self.assertEqual(len(response.context['posts']), 2)

    def test_non_existent_tag_returns_not_found(self):
        """존재하지 않는 태그로 접근 시 404를 반환하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_tag', args=['non-existent-tag']))
        # Then
        self.assertEqual(response.status_code, 404)
