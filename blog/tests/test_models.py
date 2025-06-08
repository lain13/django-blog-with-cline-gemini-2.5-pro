import time
from django.test import TestCase
from ..models import Post, Comment, Tag


class TagModelTest(TestCase):
    """Tag 모델 관련 테스트"""

    def test_tag_model_can_be_created(self):
        """Tag 모델 인스턴스가 올바르게 생성되는지 테스트"""
        # Given
        tag = Tag.objects.create(name="django")

        # When
        saved_tag = Tag.objects.get(pk=tag.pk)

        # Then
        self.assertEqual(saved_tag.name, "django")


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

    def test_updated_at_is_updated_on_save(self):
        """게시글이 저장될 때마다 updated_at 필드가 업데이트되는지 테스트"""
        # Given
        post = Post.objects.create(
            title="Initial Title",
            content="Initial Content"
        )
        first_updated_at = post.updated_at

        # When
        # 게시글을 수정하고 저장
        time.sleep(0.001) # 시간차를 만들기 위해 약간의 딜레이를 줍니다.
        post.title = "Updated Title"
        post.save()
        post.refresh_from_db()
        second_updated_at = post.updated_at

        # Then
        self.assertGreater(second_updated_at, first_updated_at)

    def test_post_can_have_tags(self):
        """Post 모델이 여러 Tag를 가질 수 있는지 테스트"""
        # Given
        post = Post.objects.create(title="Post with tags", content="Content")
        tag1 = Tag.objects.create(name="tag1")
        tag2 = Tag.objects.create(name="tag2")

        # When
        post.tags.add(tag1, tag2)

        # Then
        self.assertEqual(post.tags.count(), 2)
        self.assertIn(tag1, post.tags.all())
        self.assertIn(tag2, post.tags.all())


class CommentModelTest(TestCase):
    """Comment 모델 관련 테스트"""

    def setUp(self):
        """테스트를 위한 데이터 사전 생성"""
        self.post = Post.objects.create(
            title="Test Post for Comment",
            content="Some content"
        )

    def test_comment_model_can_be_created(self):
        """Comment 모델 인스턴스가 올바르게 생성되는지 테스트"""
        # Given
        comment = Comment.objects.create(
            post=self.post,
            author="Cline",
            text="This is a test comment."
        )

        # When
        saved_comment = Comment.objects.get(pk=comment.pk)

        # Then
        self.assertEqual(saved_comment.post, self.post)
        self.assertEqual(saved_comment.author, "Cline")
        self.assertEqual(saved_comment.text, "This is a test comment.")
        self.assertIsNotNone(saved_comment.created_at)
