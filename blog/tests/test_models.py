import time
import time
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from ..models import Post, Comment, Tag, Category, Vote


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


class VoteModelTest(TestCase):
    """Vote 모델 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 클래스 레벨 데이터 설정"""
        User = get_user_model()
        cls.user1 = User.objects.create_user(username='user1', password='password')
        cls.user2 = User.objects.create_user(username='user2', password='password')
        cls.post = Post.objects.create(
            title="Post for Voting",
            content="Content",
            author=cls.user1
        )

    def test_vote_model_can_be_created(self):
        """Vote 모델 인스턴스가 올바르게 생성되는지 테스트"""
        # Given: Like
        like_vote = Vote.objects.create(user=self.user1, post=self.post, value=Vote.LIKE)
        # Given: Dislike
        dislike_vote = Vote.objects.create(user=self.user2, post=self.post, value=Vote.DISLIKE)

        # When
        saved_like = Vote.objects.get(pk=like_vote.pk)
        saved_dislike = Vote.objects.get(pk=dislike_vote.pk)

        # Then
        self.assertEqual(saved_like.user, self.user1)
        self.assertEqual(saved_like.post, self.post)
        self.assertEqual(saved_like.value, 1)
        self.assertEqual(saved_dislike.user, self.user2)
        self.assertEqual(saved_dislike.post, self.post)
        self.assertEqual(saved_dislike.value, -1)

    def test_post_vote_aggregation(self):
        """Post 모델에서 투표 수를 올바르게 집계하는지 테스트"""
        # Given
        Vote.objects.create(user=self.user1, post=self.post, value=Vote.LIKE)
        Vote.objects.create(user=self.user2, post=self.post, value=Vote.LIKE)

        # When
        self.post.refresh_from_db()

        # Then
        self.assertEqual(self.post.get_vote_count(), 2)

        # Given
        Vote.objects.create(user=get_user_model().objects.create_user('user3'), post=self.post, value=Vote.DISLIKE)

        # When
        self.post.refresh_from_db()

        # Then
        self.assertEqual(self.post.get_vote_count(), 1)

    def test_user_cannot_vote_twice_on_same_post(self):
        """한 사용자가 같은 게시물에 중복으로 투표할 수 없는지 테스트"""
        # Given
        Vote.objects.create(user=self.user1, post=self.post, value=Vote.LIKE)

        # When/Then
        with self.assertRaises(IntegrityError):
            Vote.objects.create(user=self.user1, post=self.post, value=Vote.DISLIKE)
