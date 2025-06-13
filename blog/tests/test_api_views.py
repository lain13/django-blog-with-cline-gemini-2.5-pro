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
