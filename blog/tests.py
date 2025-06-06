from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    """Post 모델 관련 테스트"""

    def test_post_model_can_be_created(self):
        """Post 모델 인스턴스가 올바르게 생성되는지 테스트"""
        # Given
        post = Post.objects.create(
            title="Test Title",
            content="Test Content"
        )

        # When
        saved_post = Post.objects.get(pk=post.pk)

        # Then
        self.assertEqual(saved_post.title, "Test Title")
        self.assertEqual(saved_post.content, "Test Content")
        self.assertIsNotNone(saved_post.created_at)
        self.assertIsNotNone(saved_post.updated_at)


class PostListViewTest(TestCase):
    """Post 목록 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        # Given
        for i in range(5):
            Post.objects.create(
                title=f"Test Post {i}",
                content=f"Test Content {i}"
            )

    def test_view_url_exists_at_desired_location(self):
        """루트 URL(/)에 뷰가 존재하는지 테스트"""
        # When
        response = self.client.get('/')
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """'post_list' URL name으로 뷰에 접근 가능한지 테스트"""
        # When
        response = self.client.get(reverse('post_list'))
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """뷰가 올바른 템플릿을 사용하는지 테스트"""
        # When
        response = self.client.get(reverse('post_list'))
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_pagination_is_correct(self):
        """포스트 목록이 컨텍스트에 포함되어 있고, 모든 포스트가 표시되는지 테스트"""
        # When
        response = self.client.get(reverse('post_list'))
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertTrue('posts' in response.context)
        self.assertEqual(len(response.context['posts']), 5)
