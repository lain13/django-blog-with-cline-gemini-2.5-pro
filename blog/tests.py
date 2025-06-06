from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    """Post 모델 관련 테스트"""

    def test_post_model_can_be_created(self):
        """Post 모델 인스턴스가 올바르게 생성되는지 테스트"""
        # Given
        post = Post.objects.create(
            title="Test Title",
            content="Test Content"
        )

        # When
        saved_post = Post.objects.get(pk=post.pk)

        # Then
        self.assertEqual(saved_post.title, "Test Title")
        self.assertEqual(saved_post.content, "Test Content")
        self.assertIsNotNone(saved_post.created_at)
        self.assertIsNotNone(saved_post.updated_at)


class PostListViewTest(TestCase):
    """Post 목록 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        # Given
        for i in range(5):
            Post.objects.create(
                title=f"Test Post {i}",
                content=f"Test Content {i}"
            )

    def test_view_url_exists_at_desired_location(self):
        """루트 URL(/)에 뷰가 존재하는지 테스트"""
        # When
        response = self.client.get('/')
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """'post_list' URL name으로 뷰에 접근 가능한지 테스트"""
        # When
        response = self.client.get(reverse('post_list'))
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """뷰가 올바른 템플릿을 사용하는지 테스트"""
        # When
        response = self.client.get(reverse('post_list'))
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_pagination_is_correct(self):
        """포스트 목록이 컨텍스트에 포함되어 있고, 모든 포스트가 표시되는지 테스트"""
        # When
        response = self.client.get(reverse('post_list'))
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertTrue('posts' in response.context)
        self.assertEqual(len(response.context['posts']), 5)


class PostDetailViewTest(TestCase):
    """Post 상세 뷰 관련 테스트"""

    def setUp(self):
        """테스트를 위한 데이터 사전 생성"""
        # Given
        self.post = Post.objects.create(
            title="A good title",
            content="Nice body content"
        )

    def test_view_url_exists_at_desired_location(self):
        """상세 뷰 URL에 접근 시 200 응답을 반환하는지 테스트"""
        # When
        response = self.client.get(f'/post/{self.post.pk}/')
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """'post_detail' URL name으로 뷰에 접근 가능한지 테스트"""
        # When
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """뷰가 올바른 템플릿을 사용하는지 테스트"""
        # When
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        # Then
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_view_displays_correct_content(self):
        """뷰가 포스트의 제목과 내용을 올바르게 표시하는지 테스트"""
        # When
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        # Then
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.content)


class PostCreateViewTest(TestCase):
    """Post 생성 뷰 관련 테스트"""

    def setUp(self):
        """테스트를 위한 데이터 사전 생성"""
        self.url = reverse('post_new')

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
            'content': 'New Test Content'
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
        self.assertRedirects(response, reverse('post_detail', kwargs={'pk': new_post.pk}))


class PostUpdateViewTest(TestCase):
    """Post 수정 뷰 관련 테스트"""

    def setUp(self):
        """테스트를 위한 데이터 사전 생성"""
        self.post = Post.objects.create(
            title='Original Title',
            content='Original Content'
        )
        self.url = reverse('post_edit', kwargs={'pk': self.post.pk})

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
            'content': 'Updated Content'
        }

        # When
        response = self.client.post(self.url, data=updated_data)

        # Then
        # 1. 수정 후 상세 페이지로 리다이렉트되는지 확인
        self.assertRedirects(response, reverse('post_detail', kwargs={'pk': self.post.pk}))

        # 2. 포스트 내용이 실제로 수정되었는지 확인
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.content, 'Updated Content')


class PostDeleteViewTest(TestCase):
    """Post 삭제 뷰 관련 테스트"""

    def setUp(self):
        """테스트를 위한 데이터 사전 생성"""
        self.post = Post.objects.create(
            title='To be deleted',
            content='Delete me'
        )
        self.url = reverse('post_delete', kwargs={'pk': self.post.pk})

    def test_view_url_exists_at_desired_location(self):
        """삭제 확인 뷰 URL에 접근 시 200 응답을 반환하는지 테스트"""
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
        self.assertTemplateUsed(response, 'blog/post_confirm_delete.html')

    def test_post_deletion(self):
        """포스트를 성공적으로 삭제하는지 테스트"""
        # Given
        initial_post_count = Post.objects.count()

        # When
        response = self.client.post(self.url)

        # Then
        # 1. 삭제 후 목록 페이지로 리다이렉트되는지 확인
        self.assertRedirects(response, reverse('post_list'))

        # 2. 포스트 개수가 1 감소했는지 확인
        self.assertEqual(Post.objects.count(), initial_post_count - 1)
