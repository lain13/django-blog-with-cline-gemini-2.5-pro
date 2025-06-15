from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ..models import Post, Comment, Category, Tag
from rest_framework.authtoken.models import Token

class PostAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(username='apiuser', password='password')
        cls.other_user = User.objects.create_user(username='otheruser', password='password')
        
        # Create 15 posts for pagination testing
        for i in range(15):
            Post.objects.create(author=cls.user, title=f'Post {i}', content=f'Content {i}')

        cls.post_by_user = Post.objects.last()
        cls.post_by_other_user = Post.objects.create(author=cls.other_user, title='Post by Other', content='Content Other')


    def _get_token_and_authenticate(self, user):
        """헬퍼 메서드: 사용자의 토큰을 가져와 인증 헤더를 설정합니다."""
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    def test_get_post_list(self):
        """
        GET /api/posts/ - 200 상태 코드를 반환해야 합니다.
        """
        url = reverse('blog-api:post-list-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_post_list_returns_data(self):
        """
        GET /api/posts/ - 게시글 목록을 반환해야 합니다.
        """
        url = reverse('blog-api:post-list-api')
        response = self.client.get(url)
        
        # 페이지네이션 적용 시, response.data는 딕셔너리입니다.
        self.assertIsInstance(response.data, dict)
        self.assertEqual(len(response.data['results']), 10)
        self.assertEqual(response.data['results'][0]['title'], 'Post by Other')

    def test_post_list_pagination(self):
        """
        GET /api/posts/ - 페이지네이션된 응답을 반환해야 합니다.
        """
        url = reverse('blog-api:post-list-api')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('count', response.data)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertIn('results', response.data)
        
        self.assertEqual(response.data['count'], 16)
        self.assertEqual(len(response.data['results']), 10) # 기본 페이지 크기

    def test_get_post_detail(self):
        """
        GET /api/posts/<pk>/ - 단일 게시글 데이터를 반환해야 합니다.
        """
        url = reverse('blog-api:post-detail-api', kwargs={'pk': self.post_by_user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Post 14')

    def test_post_detail_author_field(self):
        """
        GET /api/posts/<pk>/ - 'author' 필드는 중첩된 객체여야 합니다.
        """
        url = reverse('blog-api:post-detail-api', kwargs={'pk': self.post_by_user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('author', response.data)
        self.assertIsInstance(response.data['author'], dict)
        self.assertIn('id', response.data['author'])
        self.assertIn('username', response.data['author'])
        self.assertEqual(response.data['author']['username'], self.user.username)

    def test_unauthenticated_user_cannot_create_post(self):
        """
        POST /api/posts/ - 인증되지 않은 사용자는 401을 반환해야 합니다.
        """
        url = reverse('blog-api:post-list-api')
        data = {'title': 'New Post', 'content': 'Some content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_post(self):
        """
        POST /api/posts/ - 인증된 사용자는 게시글을 생성할 수 있어야 합니다.
        """
        self._get_token_and_authenticate(self.user)
        
        url = reverse('blog-api:post-list-api')
        data = {'title': 'Authenticated Post', 'content': 'Content by authenticated user'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 17)
        self.assertEqual(Post.objects.latest('id').title, 'Authenticated Post')

    def test_user_cannot_update_other_users_post(self):
        """
        PUT /api/posts/<pk>/ - 다른 사용자의 게시글을 수정하려는 경우 403을 반환해야 합니다.
        """
        self._get_token_and_authenticate(self.user)
        
        url = reverse('blog-api:post-detail-api', kwargs={'pk': self.post_by_other_user.pk})
        data = {'title': 'Updated Title', 'content': 'Updated content'}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_update_own_post(self):
        """
        PUT /api/posts/<pk>/ - 자신의 게시글을 수정하는 경우 200을 반환해야 합니다.
        """
        self._get_token_and_authenticate(self.user)
        
        url = reverse('blog-api:post-detail-api', kwargs={'pk': self.post_by_user.pk})
        data = {'title': 'Updated Title', 'content': 'Updated content'}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post_by_user.refresh_from_db()
        self.assertEqual(self.post_by_user.title, 'Updated Title')

    def test_user_cannot_delete_other_users_post(self):
        """
        DELETE /api/posts/<pk>/ - 다른 사용자의 게시글을 삭제하려는 경우 403을 반환해야 합니다.
        """
        self._get_token_and_authenticate(self.user)
        
        url = reverse('blog-api:post-detail-api', kwargs={'pk': self.post_by_other_user.pk})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_post(self):
        """
        DELETE /api/posts/<pk>/ - 자신의 게시글을 삭제하는 경우 204를 반환해야 합니다.
        """
        self._get_token_and_authenticate(self.user)
        
        url = reverse('blog-api:post-detail-api', kwargs={'pk': self.post_by_user.pk})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 15)

    def test_post_list_filtering_by_category(self):
        """
        GET /api/posts/?category__name=<category_name> - 카테고리 이름으로 필터링되어야 합니다.
        """
        category = Category.objects.create(name='Test Category', slug='test-category')
        Post.objects.create(author=self.user, title='Post in Category', content='Content', category=category)

        url = reverse('blog-api:post-list-api')
        response = self.client.get(url, {'category__name': 'Test Category'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Post in Category')

    def test_post_list_filtering_by_tag(self):
        """
        GET /api/posts/?tags__name=<tag_name> - 태그 이름으로 필터링되어야 합니다.
        """
        tag = Tag.objects.create(name='Test Tag')
        post_with_tag = Post.objects.create(author=self.user, title='Post with Tag', content='Content')
        post_with_tag.tags.add(tag)

        url = reverse('blog-api:post-list-api')
        response = self.client.get(url, {'tags__name': 'Test Tag'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Post with Tag')

    def test_post_list_search(self):
        """
        GET /api/posts/?search=<keyword> - 검색어로 필터링되어야 합니다.
        """
        Post.objects.create(author=self.user, title='A post about Django', content='Django is a web framework.')
        Post.objects.create(author=self.user, title='A post about Python', content='Python is a programming language.')

        url = reverse('blog-api:post-list-api')
        response = self.client.get(url, {'search': 'Django'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'A post about Django')


class CommentAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(username='apiuser', password='password')
        cls.other_user = User.objects.create_user(username='otheruser', password='password')
        cls.post = Post.objects.create(author=cls.user, title='Test Post', content='Test Content')
        cls.comment = Comment.objects.create(post=cls.post, author=cls.user, text='A comment')
        cls.other_comment = Comment.objects.create(post=cls.post, author=cls.other_user, text='Another comment')

    def _get_token_and_authenticate(self, user):
        """헬퍼 메서드: 사용자의 토큰을 가져와 인증 헤더를 설정합니다."""
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_comment_list(self):
        """
        GET /api/comments/ - 댓글 목록을 반환해야 합니다.
        """
        url = reverse('blog-api:comment-list-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(len(response.data['results']), 2)

    def test_get_comment_detail(self):
        """
        GET /api/comments/<pk>/ - 단일 댓글을 반환해야 합니다.
        """
        url = reverse('blog-api:comment-detail-api', kwargs={'pk': self.comment.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'A comment')

    def test_unauthenticated_user_cannot_create_comment(self):
        """
        POST /api/comments/ - 인증되지 않은 사용자는 401을 반환해야 합니다.
        """
        url = reverse('blog-api:comment-list-api')
        data = {'post': self.post.pk, 'text': 'New comment text'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_comment(self):
        """
        POST /api/comments/ - 인증된 사용자는 댓글을 생성할 수 있어야 합니다.
        """
        self._get_token_and_authenticate(self.user)
        url = reverse('blog-api:comment-list-api')
        data = {'post': self.post.pk, 'text': 'New comment from authenticated user'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 3)
        self.assertEqual(Comment.objects.latest('id').text, 'New comment from authenticated user')

    def test_user_can_update_own_comment(self):
        """
        PUT /api/comments/<pk>/ - 자신의 댓글을 수정하는 경우 200을 반환해야 합니다.
        """
        self._get_token_and_authenticate(self.user)
        url = reverse('blog-api:comment-detail-api', kwargs={'pk': self.comment.pk})
        data = {'post': self.post.pk, 'text': 'Updated comment text'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.text, 'Updated comment text')

    def test_user_cannot_update_other_users_comment(self):
        """
        PUT /api/comments/<pk>/ - 다른 사용자의 댓글을 수정하려는 경우 403을 반환해야 합니다.
        """
        self._get_token_and_authenticate(self.user)
        url = reverse('blog-api:comment-detail-api', kwargs={'pk': self.other_comment.pk})
        data = {'text': 'Malicious update'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_comment(self):
        """
        DELETE /api/comments/<pk>/ - 자신의 댓글을 삭제하는 경우 204를 반환해야 합니다.
        """
        self._get_token_and_authenticate(self.user)
        url = reverse('blog-api:comment-detail-api', kwargs={'pk': self.comment.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 1)

    def test_user_cannot_delete_other_users_comment(self):
        """
        DELETE /api/comments/<pk>/ - 다른 사용자의 댓글을 삭제하려는 경우 403을 반환해야 합니다.
        """
        self._get_token_and_authenticate(self.user)
        url = reverse('blog-api:comment-detail-api', kwargs={'pk': self.other_comment.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CategoryAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Django', slug='django')
        cls.category2 = Category.objects.create(name='Python', slug='python')

    def test_get_category_list(self):
        """
        GET /api/categories/ - 카테고리 목록을 반환해야 합니다.
        """
        url = reverse('blog-api:category-list-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['name'], 'Python')

    def test_get_category_detail(self):
        """
        GET /api/categories/<pk>/ - 단일 카테고리를 반환해야 합니다.
        """
        url = reverse('blog-api:category-detail-api', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Django')

    def test_unauthenticated_user_cannot_create_category(self):
        """
        POST /api/categories/ - 인증되지 않은 사용자는 401을 반환해야 합니다.
        """
        url = reverse('blog-api:category-list-api')
        data = {'name': 'New Category', 'slug': 'new-category'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_cannot_create_category(self):
        """
        POST /api/categories/ - 인증된 사용자는 읽기 전용이므로 405를 반환해야 합니다.
        """
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = reverse('blog-api:category-list-api')
        data = {'name': 'New Category', 'slug': 'new-category'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class TagAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(name='TDD')
        cls.tag2 = Tag.objects.create(name='Django')

    def test_get_tag_list(self):
        """
        GET /api/tags/ - 태그 목록을 반환해야 합니다.
        """
        url = reverse('blog-api:tag-list-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['name'], 'Django')

    def test_get_tag_detail(self):
        """
        GET /api/tags/<pk>/ - 단일 태그를 반환해야 합니다.
        """
        url = reverse('blog-api:tag-detail-api', kwargs={'pk': self.tag.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'TDD')

    def test_unauthenticated_user_cannot_create_tag(self):
        """
        POST /api/tags/ - 인증되지 않은 사용자는 401을 반환해야 합니다.
        """
        url = reverse('blog-api:tag-list-api')
        data = {'name': 'New Tag'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_cannot_create_tag(self):
        """
        POST /api/tags/ - 인증된 사용자는 읽기 전용이므로 405를 반환해야 합니다.
        """
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = reverse('blog-api:tag-list-api')
        data = {'name': 'New Tag'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
