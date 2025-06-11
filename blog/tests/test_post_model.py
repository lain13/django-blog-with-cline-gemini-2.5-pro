import time
from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Post, Tag, Category


class PostModelTest(TestCase):
    """Post 모델 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 클래스 레벨 데이터 설정"""
        User = get_user_model()
        cls.user = User.objects.create_user(username='testuser', password='password')
        cls.post = Post.objects.create(
            title="Test Title",
            content="Test Content",
            author=cls.user
        )

    def test_post_has_author(self):
        """Post 모델에 author 필드가 올바르게 설정되었는지 테스트"""
        # Given: setUpTestData에서 post 객체 생성
        # When
        saved_post = Post.objects.get(pk=self.post.pk)
        # Then
        self.assertEqual(saved_post.author, self.user)

    def test_post_model_can_be_created(self):
        """Post 모델 인스턴스가 올바르게 생성되는지 테스트"""
        # Given: setUpTestData에서 post 객체 생성
        # When
        saved_post = Post.objects.get(pk=self.post.pk)

        # Then
        self.assertEqual(saved_post.title, "Test Title")
        self.assertEqual(saved_post.content, "Test Content")
        self.assertIsNotNone(saved_post.created_at)
        self.assertIsNotNone(saved_post.updated_at)

    def test_updated_at_is_updated_on_save(self):
        """게시글이 저장될 때마다 updated_at 필드가 업데이트되는지 테스트"""
        # Given
        post = self.post
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
        post = self.post
        tag1 = Tag.objects.create(name="tag1")
        tag2 = Tag.objects.create(name="tag2")

        # When
        post.tags.add(tag1, tag2)

        # Then
        self.assertEqual(post.tags.count(), 2)
        self.assertIn(tag1, post.tags.all())
        self.assertIn(tag2, post.tags.all())

    def test_post_can_have_category(self):
        """Post 모델이 Category를 가질 수 있는지 테스트"""
        # Given
        post = self.post
        category = Category.objects.create(name="Test Category", slug="test-category")

        # When
        post.category = category
        post.save()

        # Then
        saved_post = Post.objects.get(pk=post.pk)
        self.assertEqual(saved_post.category, category)

    def test_post_has_initial_view_count(self):
        """Post 모델 생성 시 view_count가 0으로 초기화되는지 테스트"""
        # Given: setUpTestData에서 post 객체 생성
        # When
        saved_post = Post.objects.get(pk=self.post.pk)
        # Then
        self.assertEqual(saved_post.view_count, 0)

    def test_increase_view_count(self):
        """increase_view_count 메서드가 조회수를 1 증가시키는지 테스트"""
        # Given
        post = self.post
        self.assertEqual(post.view_count, 0)
        # When
        post.increase_view_count()
        post.refresh_from_db()
        # Then
        self.assertEqual(post.view_count, 1)
