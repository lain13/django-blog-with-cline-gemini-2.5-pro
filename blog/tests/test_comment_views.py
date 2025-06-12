from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from captcha.conf import settings as captcha_settings
from ..models import Post, Comment


class CommentViewTest(TestCase):
    """Comment 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        User = get_user_model()
        cls.user = User.objects.create_user(username='commentviewuser', password='password')
        cls.post = Post.objects.create(
            title="A good title for comment test",
            content="Nice body content for comment test",
            author=cls.user
        )

    def test_comment_creation(self):
        """로그인한 사용자가 새로운 댓글을 성공적으로 생성하는지 테스트"""
        # Given
        captcha_settings.CAPTCHA_TEST_MODE = True
        self.client.login(username='commentviewuser', password='password')
        initial_comment_count = self.post.comments.count()
        comment_data = {
            'text': 'A new comment',
            'captcha_0': 'passed',
            'captcha_1': 'passed',
        }
        url = reverse('blog:comment_new', kwargs={'pk': self.post.pk})

        # When
        response = self.client.post(url, data=comment_data)

        # Then
        captcha_settings.CAPTCHA_TEST_MODE = False
        self.assertEqual(self.post.comments.count(), initial_comment_count + 1)
        new_comment = self.post.comments.last()
        self.assertEqual(new_comment.author, self.user)
        self.assertEqual(new_comment.text, 'A new comment')
        self.assertRedirects(response, reverse('blog:post_detail', kwargs={'pk': self.post.pk}))

    def test_comment_creation_fails_without_captcha(self):
        """CAPTCHA 없이 댓글 생성 시도 시 실패하는지 테스트"""
        # Given
        self.client.login(username='commentviewuser', password='password')
        initial_comment_count = self.post.comments.count()
        comment_data = {
            'text': 'A comment without captcha'
        }
        url = reverse('blog:comment_new', kwargs={'pk': self.post.pk})

        # When
        response = self.client.post(url, data=comment_data)

        # Then
        self.assertEqual(self.post.comments.count(), initial_comment_count)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/comment_form.html')
        # Check for form error manually
        form = response.context.get('form')
        self.assertIsNotNone(form)
        self.assertTrue(form.is_bound)
        self.assertIn('captcha', form.errors)
        self.assertEqual(form.errors['captcha'], ['This field is required.'])


class CommentProtectionTest(TestCase):
    """댓글 생성, 수정, 삭제에 대한 접근 제어 테스트"""
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user1 = User.objects.create_user(username='commentuser1', password='password')
        cls.user2 = User.objects.create_user(username='commentuser2', password='password')
        cls.post = Post.objects.create(author=cls.user1, title='Post for Comments', content='Content')
        cls.comment = Comment.objects.create(post=cls.post, author=cls.user1, text='A comment to be tested')

    def test_authentication_required_for_comment_create(self):
        """로그인하지 않은 사용자가 댓글 생성 시도 시 로그인 페이지로 리다이렉트되는지 테스트"""
        # Given
        url = reverse('blog:comment_new', kwargs={'pk': self.post.pk})
        comment_data = {'text': 'This should not be created'}
        
        # When
        response = self.client.post(url, data=comment_data)
        
        # Then
        self.assertRedirects(response, f"{reverse('users:login')}?next={url}")

    def test_authentication_required_for_comment_update(self):
        """로그인하지 않은 사용자가 댓글 수정 시도 시 로그인 페이지로 리다이렉트되는지 테스트"""
        # Given
        url = reverse('blog:comment_edit', kwargs={'pk': self.comment.pk})
        
        # When
        response = self.client.get(url)
        
        # Then
        self.assertRedirects(response, f"{reverse('users:login')}?next={url}")

    def test_authentication_required_for_comment_delete(self):
        """로그인하지 않은 사용자가 댓글 삭제 시도 시 로그인 페이지로 리다이렉트되는지 테스트"""
        # Given
        url = reverse('blog:comment_delete', kwargs={'pk': self.comment.pk})
        
        # When
        response = self.client.get(url)
        
        # Then
        self.assertRedirects(response, f"{reverse('users:login')}?next={url}")

    def test_author_required_for_comment_update(self):
        """작성자가 아닌 사용자가 댓글 수정 시도 시 403 오류가 발생하는지 테스트"""
        # Given
        self.client.login(username='commentuser2', password='password')
        url = reverse('blog:comment_edit', kwargs={'pk': self.comment.pk})
        
        # When
        response = self.client.get(url)
        
        # Then
        self.assertEqual(response.status_code, 403)

    def test_author_required_for_comment_delete(self):
        """작성자가 아닌 사용자가 댓글 삭제 시도 시 403 오류가 발생하는지 테스트"""
        # Given
        self.client.login(username='commentuser2', password='password')
        url = reverse('blog:comment_delete', kwargs={'pk': self.comment.pk})
        
        # When
        response = self.client.get(url)
        
        # Then
        self.assertEqual(response.status_code, 403)
