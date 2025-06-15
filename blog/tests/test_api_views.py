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
        cls.post_by_user = Post.objects.create(author=cls.user, title='Post by User', content='Content 1')
        cls.post_by_other_user = Post.objects.create(author=cls.other_user, title='Post by Other', content='Content 2')

    def _get_token_and_authenticate(self, user):
        """Helper method to get token and set credentials."""
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    def test_get_post_list(self):
        """
        GET /api/posts/ - Should return status 200
        """
        url = reverse('blog-api:post-list-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_post_list_returns_data(self):
        """
        GET /api/posts/ - Should return a list of posts
        """
        url = reverse('blog-api:post-list-api')
        response = self.client.get(url)
        
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Post by User')
        self.assertEqual(response.data[1]['title'], 'Post by Other')

    def test_get_post_detail(self):
        """
        GET /api/posts/<pk>/ - Should return a single post's data
        """
        url = reverse('blog-api:post-detail-api', kwargs={'pk': self.post_by_user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Post by User')

    def test_post_detail_author_field(self):
        """
        GET /api/posts/<pk>/ - The author field should be a nested object.
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
        POST /api/posts/ - Should return 401 for unauthenticated user
        """
        url = reverse('blog-api:post-list-api')
        data = {'title': 'New Post', 'content': 'Some content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_post(self):
        """
        POST /api/posts/ - Should create a post for an authenticated user
        """
        self._get_token_and_authenticate(self.user)
        
        url = reverse('blog-api:post-list-api')
        data = {'title': 'Authenticated Post', 'content': 'Content by authenticated user'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 3)
        self.assertEqual(Post.objects.latest('id').title, 'Authenticated Post')

    def test_user_cannot_update_other_users_post(self):
        """
        PUT /api/posts/<pk>/ - Should return 403 for user trying to update other's post
        """
        self._get_token_and_authenticate(self.user)
        
        url = reverse('blog-api:post-detail-api', kwargs={'pk': self.post_by_other_user.pk})
        data = {'title': 'Updated Title', 'content': 'Updated content'}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_update_own_post(self):
        """
        PUT /api/posts/<pk>/ - Should return 200 for user updating their own post
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
        DELETE /api/posts/<pk>/ - Should return 403 for user trying to delete other's post
        """
        self._get_token_and_authenticate(self.user)
        
        url = reverse('blog-api:post-detail-api', kwargs={'pk': self.post_by_other_user.pk})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_post(self):
        """
        DELETE /api/posts/<pk>/ - Should return 204 for user deleting their own post
        """
        self._get_token_and_authenticate(self.user)
        
        url = reverse('blog-api:post-detail-api', kwargs={'pk': self.post_by_user.pk})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 1)


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
        """Helper method to get token and set credentials."""
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_comment_list(self):
        """
        GET /api/comments/ - Should return a list of comments.
        """
        url = reverse('blog-api:comment-list-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_comment_detail(self):
        """
        GET /api/comments/<pk>/ - Should return a single comment.
        """
        url = reverse('blog-api:comment-detail-api', kwargs={'pk': self.comment.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], 'A comment')

    def test_unauthenticated_user_cannot_create_comment(self):
        """
        POST /api/comments/ - Should return 401 for unauthenticated user.
        """
        url = reverse('blog-api:comment-list-api')
        data = {'post': self.post.pk, 'text': 'New comment text'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_comment(self):
        """
        POST /api/comments/ - Should create a comment for an authenticated user.
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
        PUT /api/comments/<pk>/ - Should return 200 for user updating their own comment.
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
        PUT /api/comments/<pk>/ - Should return 403 for user trying to update other's comment.
        """
        self._get_token_and_authenticate(self.user)
        url = reverse('blog-api:comment-detail-api', kwargs={'pk': self.other_comment.pk})
        data = {'text': 'Malicious update'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_comment(self):
        """
        DELETE /api/comments/<pk>/ - Should return 204 for user deleting their own comment.
        """
        self._get_token_and_authenticate(self.user)
        url = reverse('blog-api:comment-detail-api', kwargs={'pk': self.comment.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 1)

    def test_user_cannot_delete_other_users_comment(self):
        """
        DELETE /api/comments/<pk>/ - Should return 403 for user trying to delete other's comment.
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
        GET /api/categories/ - Should return a list of categories.
        """
        url = reverse('blog-api:category-list-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Django')

    def test_get_category_detail(self):
        """
        GET /api/categories/<pk>/ - Should return a single category.
        """
        url = reverse('blog-api:category-detail-api', kwargs={'pk': self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Django')

    def test_unauthenticated_user_cannot_create_category(self):
        """
        POST /api/categories/ - Should return 401 for unauthenticated user.
        """
        url = reverse('blog-api:category-list-api')
        data = {'name': 'New Category', 'slug': 'new-category'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_cannot_create_category(self):
        """
        POST /api/categories/ - Should return 403 for authenticated user as it's read-only.
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
        GET /api/tags/ - Should return a list of tags.
        """
        url = reverse('blog-api:tag-list-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'TDD')

    def test_get_tag_detail(self):
        """
        GET /api/tags/<pk>/ - Should return a single tag.
        """
        url = reverse('blog-api:tag-detail-api', kwargs={'pk': self.tag.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'TDD')

    def test_unauthenticated_user_cannot_create_tag(self):
        """
        POST /api/tags/ - Should return 401 for unauthenticated user.
        """
        url = reverse('blog-api:tag-list-api')
        data = {'name': 'New Tag'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_cannot_create_tag(self):
        """
        POST /api/tags/ - Should return 405 for authenticated user as it's read-only.
        """
        User = get_user_model()
        user = User.objects.create_user(username='testuser', password='password')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = reverse('blog-api:tag-list-api')
        data = {'name': 'New Tag'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
