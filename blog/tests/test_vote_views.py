import json
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Post, Vote


class VoteViewTest(TestCase):
    """좋아요/싫어요 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(username='voteuser', password='password')
        cls.post = Post.objects.create(author=cls.user, title='Vote Post', content='Content')
        cls.url = reverse('blog:post_vote', kwargs={'pk': cls.post.pk})

    def test_vote_requires_login(self):
        """로그인하지 않은 사용자가 투표 시도 시 에러를 반환하는지 테스트"""
        # When
        response = self.client.post(self.url, json.dumps({'value': 'like'}), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        # Then
        self.assertEqual(response.status_code, 401) # Unauthorized

    def test_like_a_post(self):
        """로그인한 사용자가 '좋아요'를 성공적으로 하는지 테스트"""
        # Given
        self.client.login(username='voteuser', password='password')
        # When
        response = self.client.post(
            self.url,
            json.dumps({'value': 'like'}),
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        # Then
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['liked'])
        self.assertFalse(data['disliked'])
        self.assertEqual(data['vote_count'], 1)
        self.assertTrue(Vote.objects.filter(user=self.user, post=self.post, value=Vote.LIKE).exists())

    def test_dislike_a_post(self):
        """로그인한 사용자가 '싫어요'를 성공적으로 하는지 테스트"""
        # Given
        self.client.login(username='voteuser', password='password')
        # When
        response = self.client.post(
            self.url,
            json.dumps({'value': 'dislike'}),
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        # Then
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['liked'])
        self.assertTrue(data['disliked'])
        self.assertEqual(data['vote_count'], -1)
        self.assertTrue(Vote.objects.filter(user=self.user, post=self.post, value=Vote.DISLIKE).exists())

    def test_toggle_like(self):
        """'좋아요'를 다시 눌렀을 때 투표가 취소되는지 테스트"""
        # Given
        self.client.login(username='voteuser', password='password')
        Vote.objects.create(user=self.user, post=self.post, value=Vote.LIKE)
        # When
        response = self.client.post(
            self.url,
            json.dumps({'value': 'like'}),
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        # Then
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['liked'])
        self.assertEqual(data['vote_count'], 0)
        self.assertFalse(Vote.objects.filter(user=self.user, post=self.post).exists())

    def test_change_vote_from_like_to_dislike(self):
        """'좋아요'에서 '싫어요'로 투표를 변경하는지 테스트"""
        # Given
        self.client.login(username='voteuser', password='password')
        Vote.objects.create(user=self.user, post=self.post, value=Vote.LIKE)
        # When
        response = self.client.post(
            self.url,
            json.dumps({'value': 'dislike'}),
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        # Then
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertFalse(data['liked'])
        self.assertTrue(data['disliked'])
        self.assertEqual(data['vote_count'], -1)
        self.assertTrue(Vote.objects.filter(user=self.user, post=self.post, value=Vote.DISLIKE).exists())
