from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Post, Category

class RSSFeedTest(TestCase):
    """RSS 피드 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        User = get_user_model()
        cls.user = User.objects.create_user(username='rssuser', password='password')
        cls.category_django = Category.objects.create(name='Django', slug='django')
        cls.category_python = Category.objects.create(name='Python', slug='python')

        for i in range(5):
            category = cls.category_django if i % 2 == 0 else cls.category_python
            Post.objects.create(
                title=f'RSS Post {i}',
                content=f'Content for RSS feed {i}',
                author=cls.user,
                category=category
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

    def test_feed_item_has_metadata(self):
        """피드 아이템에 게시일, 작성자 등 메타데이터가 포함되는지 테스트"""
        response = self.client.get(reverse('blog:post_feed'))
        post = Post.objects.latest('created_at')
        
        # Django의 syndication 프레임워크는 네임스페이스와 함께 <dc:creator> 태그를 생성합니다.
        self.assertContains(response, f'<dc:creator xmlns:dc="http://purl.org/dc/elements/1.1/">{post.author.username}</dc:creator>')
        # pubDate 형식: 'Sat, 14 Jun 2025 14:30:00 +0000'
        # 테스트에서는 년, 월, 일 정도만 확인하여 시간차로 인한 실패를 방지합니다.
        self.assertContains(response, post.created_at.strftime('%a, %d %b %Y'))

    def test_category_feed_returns_correct_posts(self):
        """카테고리별 피드가 올바른 게시물만 반환하는지 테스트"""
        # 'django' 카테고리 피드 URL을 reverse를 사용해 가져오려고 시도합니다.
        # 아직 URL이 없으므로 NoReverseMatch 예외가 발생하며 테스트는 실패(Error)합니다.
        url = reverse('blog:category_feed', kwargs={'category_slug': self.category_django.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        
        # Django 카테고리의 게시물(짝수)은 포함되어야 함
        self.assertContains(response, '<title>RSS Post 0</title>')
        self.assertContains(response, '<title>RSS Post 2</title>')
        self.assertContains(response, '<title>RSS Post 4</title>')

        # Python 카테고리의 게시물(홀수)은 포함되지 않아야 함
        self.assertNotContains(response, '<title>RSS Post 1</title>')
        self.assertNotContains(response, '<title>RSS Post 3</title>')
