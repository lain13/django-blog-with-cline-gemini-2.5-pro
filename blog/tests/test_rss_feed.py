from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Post

class RSSFeedTest(TestCase):
    """RSS 피드 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        User = get_user_model()
        cls.user = User.objects.create_user(username='rssuser', password='password')
        for i in range(5):
            Post.objects.create(
                title=f'RSS Post {i}',
                content=f'Content for RSS feed {i}',
                author=cls.user
            )

    def test_feed_url_exists(self):
        """피드 URL이 올바른 경로에 존재하는지 테스트"""
        response = self.client.get('/feed/')
        self.assertEqual(response.status_code, 200)

    def test_feed_url_accessible_by_name(self):
        """'post_feed' URL name으로 피드에 접근 가능한지 테스트"""
        response = self.client.get(reverse('blog:post_feed'))
        self.assertEqual(response.status_code, 200)

    def test_feed_contains_correct_items(self):
        """피드에 올바른 게시물 정보가 포함되어 있는지 테스트"""
        response = self.client.get(reverse('blog:post_feed'))
        self.assertEqual(response.status_code, 200)
        
        # 5개의 포스트가 모두 포함되었는지 확인
        self.assertContains(response, '<title>RSS Post 0</title>', count=1)
        self.assertContains(response, '<title>RSS Post 4</title>', count=1)
        
        # 포스트 내용이 포함되었는지 확인
        self.assertContains(response, 'Content for RSS feed 0')

    def test_feed_item_link_is_correct(self):
        """피드 아이템의 링크가 올바른지 테스트"""
        post = Post.objects.latest('created_at')
        response = self.client.get(reverse('blog:post_feed'))
        self.assertContains(response, post.get_absolute_url())
