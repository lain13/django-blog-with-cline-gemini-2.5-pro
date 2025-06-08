import time
from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Post, Comment, Tag, Category


class CategoryModelTest(TestCase):
    """Category 모델 관련 테스트"""

    def test_category_model_can_be_created(self):
        """Category 모델 인스턴스가 올바르게 생성되는지 테스트"""
        # Given
        category = Category.objects.create(name="Programming", slug="programming")

        # When
        saved_category = Category.objects.get(pk=category.pk)

        # Then
        self.assertEqual(saved_category.name, "Programming")
        self.assertEqual(saved_category.slug, "programming")

    def test_category_str_representation(self):
        """Category 모델의 __str__ 메서드가 올바르게 동작하는지 테스트"""
        # Given
        category = Category.objects.create(name="Life", slug="life")

        # When/Then
        self.assertEqual(str(category), "Life")

    def test_hierarchical_category(self):
        """계층형 카테고리 관계가 올바르게 설정되는지 테스트"""
        # Given
        parent_category = Category.objects.create(name="Tech", slug="tech")
        child_category = Category.objects.create(
            name="Python",
            slug="python",
            parent=parent_category
        )

        # When
        saved_child = Category.objects.get(pk=child_category.pk)

        # Then
        self.assertIsNotNone(saved_child.parent)
        self.assertEqual(saved_child.parent, parent_category)
        self.assertIn(child_category, parent_category.children.all())


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


class CommentModelTest(TestCase):
    """Comment 모델 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 클래스 레벨 데이터 설정"""
        User = get_user_model()
        user = User.objects.create_user(username='commenter', password='password')
        cls.post = Post.objects.create(
            title="Test Post for Comment",
            content="Some content",
            author=user
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
