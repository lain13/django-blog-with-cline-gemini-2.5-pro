import unittest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import translation
from ..models import Post, Tag


class SearchViewTest(TestCase):
    """검색 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        User = get_user_model()
        cls.user = User.objects.create_user(username='searchuser', password='password')
        Post.objects.create(title="Apple Banana", content="Content one", author=cls.user)
        Post.objects.create(title="Second Post", content="Content with Apple", author=cls.user)
        Post.objects.create(title="Third Banana", content="Content three", author=cls.user)

    def test_search_view_url_exists(self):
        """검색 뷰 URL에 접근 시 200 응답을 반환하는지 테스트"""
        response = self.client.get(reverse('blog:search'))
        self.assertEqual(response.status_code, 200)

    def test_search_view_uses_correct_template(self):
        """검색 뷰가 올바른 템플릿을 사용하는지 테스트"""
        response = self.client.get(reverse('blog:search'))
        self.assertTemplateUsed(response, 'blog/search_results.html')

    def test_search_by_title(self):
        """제목으로 검색이 올바르게 동작하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:search'), {'q': 'Apple'})

        # Then
        # 1. 응답 상태 코드 및 템플릿 확인
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/search_results.html')

        # 2. 컨텍스트의 쿼리셋 확인 (더 안정적인 방법)
        self.assertIn('posts', response.context)
        posts_in_context = response.context['posts']
        self.assertEqual(len(posts_in_context), 2)

        # 3. 예상되는 포스트가 포함되어 있는지 확인 (순서에 의존하지 않음)
        titles_in_context = [post.title for post in posts_in_context]
        self.assertIn("Apple Banana", titles_in_context)
        self.assertIn("Second Post", titles_in_context)
        self.assertNotIn("Third Banana", titles_in_context)

    def test_search_by_content(self):
        """내용으로 검색이 올바르게 동작하는지 테스트"""
        response = self.client.get(reverse('blog:search'), {'q': 'Content one'})
        self.assertContains(response, "Apple Banana")
        self.assertNotContains(response, "Second Post")
        self.assertNotContains(response, "Third Banana")

    def test_search_no_results(self):
        """검색 결과가 없을 때를 올바르게 처리하는지 테스트"""
        with translation.activate('en'):
            response = self.client.get(reverse('blog:search'), {'q': 'NonExistentTerm'})
            self.assertContains(response, "No posts found.")
            self.assertNotContains(response, "Apple Banana")

    def test_search_empty_query(self):
        """검색어가 비어있을 때 모든 포스트를 보여주지 않는지 테스트"""
        with translation.activate('en'):
            response = self.client.get(reverse('blog:search'), {'q': ''})
            self.assertContains(response, "Please enter a search term.")
            self.assertNotIn('posts', response.context)

    def test_search_by_tag(self):
        """태그로 검색이 올바르게 동작하는지 테스트"""
        # Given
        tag_post = Post.objects.create(title="Tag Post", content="Content for tag", author=self.user)
        tag = Tag.objects.create(name="unique-tag")
        tag_post.tags.add(tag)

        # When
        response = self.client.get(reverse('blog:search'), {'q': 'unique-tag'})

        # Then
        self.assertContains(response, "Tag Post")
        self.assertNotContains(response, "Apple Banana")

    def test_search_context_contains_query(self):
        """검색어가 context에 포함되어 템플릿으로 전달되는지 테스트"""
        # Given
        query = "test-query"

        # When
        response = self.client.get(reverse('blog:search'), {'q': query})

        # Then
        self.assertEqual(response.context.get('query'), query)
