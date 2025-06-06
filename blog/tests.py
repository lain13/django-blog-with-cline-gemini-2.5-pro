from django.test import TestCase
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
