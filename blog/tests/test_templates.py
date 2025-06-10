from django.test import TestCase
from django.urls import reverse

from blog.models.post import Post
from django.contrib.auth.models import User


class TemplateInheritanceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(author=self.user, title='Test Post', content='Test Content')

    def test_post_list_uses_base_template(self):
        """
        post_list 뷰가 렌더링하는 페이지에 base.html의 title 태그가 포함되어 있는지 확인
        """
        response = self.client.get(reverse('blog:post_list'))
        self.assertContains(response, '<title>Django TDD Blog</title>')

    def test_post_detail_uses_base_template(self):
        """
        post_detail 뷰가 렌더링하는 페이지에 base.html의 title 태그가 포함되어 있는지 확인
        """
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        self.assertContains(response, '<title>Django TDD Blog</title>')

    def test_post_form_uses_base_template(self):
        """
        post_form 뷰가 렌더링하는 페이지에 base.html의 title 태그가 포함되어 있는지 확인
        """
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('blog:post_new'))
        self.assertContains(response, '<title>Django TDD Blog</title>')

    def test_post_confirm_delete_uses_base_template(self):
        """
        post_confirm_delete 뷰가 렌더링하는 페이지에 base.html의 title 태그가 포함되어 있는지 확인
        """
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('blog:post_delete', kwargs={'pk': self.post.pk}))
        self.assertContains(response, '<title>Django TDD Blog</title>')

    def test_search_results_uses_base_template(self):
        """
        search_results 뷰가 렌더링하는 페이지에 base.html의 title 태그가 포함되어 있는지 확인
        """
        response = self.client.get(reverse('blog:search') + '?q=test')
        self.assertContains(response, '<title>Django TDD Blog</title>')
