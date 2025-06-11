from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from ..models import Post, Vote


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
        self.assertEqual(self.post.like_count, 2)
        self.assertEqual(self.post.dislike_count, 0)

        # Given
        Vote.objects.create(user=get_user_model().objects.create_user('user3'), post=self.post, value=Vote.DISLIKE)

        # When
        self.post.refresh_from_db()

        # Then
        self.assertEqual(self.post.like_count, 2)
        self.assertEqual(self.post.dislike_count, 1)
        self.assertEqual(self.post.get_vote_count(), 3) # 총 투표 수 확인

    def test_user_cannot_vote_twice_on_same_post(self):
        """한 사용자가 같은 게시물에 중복으로 투표할 수 없는지 테스트"""
        # Given
        Vote.objects.create(user=self.user1, post=self.post, value=Vote.LIKE)

        # When/Then
        with self.assertRaises(IntegrityError):
            Vote.objects.create(user=self.user1, post=self.post, value=Vote.DISLIKE)
