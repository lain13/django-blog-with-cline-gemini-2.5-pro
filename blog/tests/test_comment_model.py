import time
from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Post, Comment


class CommentModelTest(TestCase):
    """Comment 모델 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 클래스 레벨 데이터 설정"""
        User = get_user_model()
        cls.user = User.objects.create_user(username='commenter', password='password')
        cls.post = Post.objects.create(
            title="Test Post for Comment",
            content="Some content",
            author=cls.user
        )

    def test_comment_model_creation_with_user_author(self):
        """Comment 모델이 User를 author로 하여 올바르게 생성되는지 테스트"""
        # Given
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            text="A comment from a logged-in user."
        )
        # When
        saved_comment = Comment.objects.get(pk=comment.pk)
        # Then
        self.assertEqual(saved_comment.author, self.user)
        self.assertEqual(saved_comment.text, "A comment from a logged-in user.")
        self.assertIsNotNone(saved_comment.created_at)
        self.assertIsNotNone(saved_comment.updated_at)

    def test_comment_updated_at_is_updated_on_save(self):
        """댓글이 저장될 때마다 updated_at 필드가 업데이트되는지 테스트"""
        # Given
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            text="Initial comment text."
        )
        first_updated_at = comment.updated_at
        # When
        time.sleep(0.001)
        comment.text = "Updated comment text."
        comment.save()
        comment.refresh_from_db()
        second_updated_at = comment.updated_at
        # Then
        self.assertGreater(second_updated_at, first_updated_at)

    def test_nested_comment_relationship(self):
        """계층형 댓글 관계가 올바르게 설정되는지 테스트"""
        # Given
        parent_comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            text="This is a parent comment."
        )
        child_comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            text="This is a reply.",
            parent=parent_comment
        )
        # When
        saved_child = Comment.objects.get(pk=child_comment.pk)
        # Then
        self.assertIsNotNone(saved_child.parent)
        self.assertEqual(saved_child.parent, parent_comment)
        self.assertIn(child_comment, parent_comment.replies.all())
