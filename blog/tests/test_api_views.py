from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ..models import Post
from rest_framework.authtoken.models import Token

class PostAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(username='apiuser', password='password')
        Post.objects.create(author=cls.user, title='Test Post 1', content='Content 1')
        Post.objects.create(author=cls.user, title='Test Post 2', content='Content 2')
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
        self.assertEqual(response.data[0]['title'], 'Test Post 1')
        self.assertEqual(response.data[1]['title'], 'Test Post 2')

    def test_get_post_detail(self):
        """
        GET /api/posts/<pk>/ - Should return a single post's data
        """
        post = Post.objects.get(title='Test Post 1')
        url = reverse('blog-api:post-detail-api', kwargs={'pk': post.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post 1')

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
        # Get token
        token_url = reverse('users:api_token_auth')
        token_response = self.client.post(token_url, {'username': 'apiuser', 'password': 'password'}, format='json')
        self.assertEqual(token_response.status_code, status.HTTP_200_OK)
        token = token_response.data['token']

        # Use token to create post
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        url = reverse('blog-api:post-list-api')
        data = {'title': 'Authenticated Post', 'content': 'Content by authenticated user'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 3)
        self.assertEqual(Post.objects.latest('id').title, 'Authenticated Post')
