from django.test import TestCase
from django.urls import reverse
from ..models import Post, Tag
from .helpers import create_user, create_post


class PostListViewTest(TestCase):
    """Post 목록 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        # Given
        cls.user = create_user(username='listuser')
        for i in range(5):
            create_post(author=cls.user, title=f"Test Post {i}")

    def test_view_url_exists_at_desired_location(self):
        """루트 URL(/)에 뷰가 존재하는지 테스트"""
        # When
        response = self.client.get('/')
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """'post_list' URL name으로 뷰에 접근 가능한지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list'))
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """뷰가 올바른 템플릿을 사용하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list'))
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_pagination_is_correct(self):
        """포스트 목록이 컨텍스트에 포함되어 있고, 모든 포스트가 표시되는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list'))
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertTrue('posts' in response.context)
        self.assertEqual(len(response.context['posts']), 5)

    def test_view_displays_tags(self):
        """포스트 목록에 태그가 표시되는지 테스트"""
        # Given
        post = Post.objects.first()
        tag1 = Tag.objects.create(name="tag1")
        post.tags.add(tag1)

        # When
        response = self.client.get(reverse('blog:post_list'))

        # Then
        self.assertContains(response, "tag1")


class PostDetailViewTest(TestCase):
    """Post 상세 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        # Given
        cls.user = create_user(username='detailuser')
        cls.post = create_post(cls.user, title="A good title")

    def test_view_url_exists_at_desired_location(self):
        """상세 뷰 URL에 접근 시 200 응답을 반환하는지 테스트"""
        # When
        response = self.client.get(f'/post/{self.post.pk}/')
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """'post_detail' URL name으로 뷰에 접근 가능한지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """뷰가 올바른 템플릿을 사용하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_view_displays_correct_content(self):
        """뷰가 포스트의 제목과 내용을 올바르게 표시하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        # Then
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.content)

    def test_view_displays_tags(self):
        """상세 뷰에 태그가 표시되는지 테스트"""
        # Given
        tag1 = Tag.objects.create(name="tag1")
        tag2 = Tag.objects.create(name="tag2")
        self.post.tags.add(tag1, tag2)

        # When
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))

        # Then
        self.assertContains(response, "tag1")
        self.assertContains(response, "tag2")

    def test_view_increases_view_count(self):
        """상세 페이지에 접근할 때마다 조회수가 1씩 증가하는지 테스트"""
        # Given
        initial_view_count = self.post.view_count
        url = reverse('blog:post_detail', kwargs={'pk': self.post.pk})

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.status_code, 200)
        self.post.refresh_from_db()
        self.assertEqual(self.post.view_count, initial_view_count + 1)

    def test_view_displays_view_count(self):
        """상세 페이지에 조회수가 올바르게 표시되는지 테스트"""
        # Given
        url = reverse('blog:post_detail', kwargs={'pk': self.post.pk})

        # When
        response = self.client.get(url)

        # Then
        self.assertEqual(response.status_code, 200)
        # 뷰가 호출되면서 조회수는 1이 되어야 합니다.
        self.assertContains(response, "Views: 1")


class PostCreateViewTest(TestCase):
    """Post 생성 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        cls.user = create_user(username='createuser')
        cls.url = reverse('blog:post_new')

    def setUp(self):
        """각 테스트 전에 클라이언트 로그인"""
        self.client.login(username=self.user.username, password='password')

    def test_view_url_exists_at_desired_location(self):
        """생성 뷰 URL에 접근 시 200 응답을 반환하는지 테스트"""
        # When
        response = self.client.get(self.url)
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """뷰가 올바른 템플릿을 사용하는지 테스트"""
        # When
        response = self.client.get(self.url)
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

    def test_post_creation(self):
        """새로운 포스트를 성공적으로 생성하는지 테스트"""
        # Given
        initial_post_count = Post.objects.count()
        post_data = {
            'title': 'New Test Title',
            'content': 'New Test Content',
            'tags': ''
        }

        # When
        response = self.client.post(self.url, data=post_data)

        # Then
        # 1. 포스트 개수가 1 증가했는지 확인
        self.assertEqual(Post.objects.count(), initial_post_count + 1)

        # 2. 새로 생성된 포스트의 내용이 올바른지 확인
        new_post = Post.objects.latest('id')
        self.assertEqual(new_post.title, 'New Test Title')
        self.assertEqual(new_post.content, 'New Test Content')

        # 3. 생성 후 상세 페이지로 리다이렉트되는지 확인
        self.assertRedirects(response, reverse('blog:post_detail', kwargs={'pk': new_post.pk}))

    def test_post_creation_with_tags(self):
        """태그와 함께 새로운 포스트를 성공적으로 생성하는지 테스트"""
        # Given
        initial_post_count = Post.objects.count()
        post_data = {
            'title': 'Post with Tags',
            'content': 'Content for post with tags',
            'tags': 'django, tdd, python'
        }

        # When
        response = self.client.post(self.url, data=post_data)

        # Then
        self.assertEqual(Post.objects.count(), initial_post_count + 1)
        new_post = Post.objects.latest('id')
        self.assertEqual(new_post.tags.count(), 3)
        tag_names = {tag.name for tag in new_post.tags.all()}
        self.assertIn('django', tag_names)
        self.assertIn('tdd', tag_names)
        self.assertIn('python', tag_names)
        self.assertRedirects(response, reverse('blog:post_detail', kwargs={'pk': new_post.pk}))


class PostUpdateViewTest(TestCase):
    """Post 수정 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        cls.user = create_user(username='updateuser')
        cls.post = create_post(cls.user, title='Original Title')
        cls.url = reverse('blog:post_edit', kwargs={'pk': cls.post.pk})

    def setUp(self):
        """각 테스트 전에 클라이언트 로그인"""
        self.client.login(username=self.user.username, password='password')

    def test_view_url_exists_at_desired_location(self):
        """수정 뷰 URL에 접근 시 200 응답을 반환하는지 테스트"""
        # When
        response = self.client.get(self.url)
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """뷰가 올바른 템플릿을 사용하는지 테스트"""
        # When
        response = self.client.get(self.url)
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

    def test_post_update(self):
        """포스트를 성공적으로 수정하는지 테스트"""
        # Given
        updated_data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
            'tags': ''
        }

        # When
        response = self.client.post(self.url, data=updated_data)

        # Then
        # 1. 수정 후 상세 페이지로 리다이렉트되는지 확인
        self.assertRedirects(response, reverse('blog:post_detail', kwargs={'pk': self.post.pk}))

        # 2. 포스트 내용이 실제로 수정되었는지 확인
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.content, 'Updated Content')

    def test_post_update_with_tags(self):
        """태그를 포함하여 포스트를 성공적으로 수정하는지 테스트"""
        # Given
        tag1 = Tag.objects.create(name="initial_tag")
        self.post.tags.add(tag1)
        
        updated_data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
            'tags': 'new_tag, another_tag'
        }

        # When
        response = self.client.post(self.url, data=updated_data)

        # Then
        self.assertRedirects(response, reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        self.post.refresh_from_db()
        tag_names = {tag.name for tag in self.post.tags.all()}
        self.assertEqual(self.post.tags.count(), 2)
        self.assertIn('new_tag', tag_names)
        self.assertIn('another_tag', tag_names)
        self.assertNotIn('initial_tag', tag_names)
