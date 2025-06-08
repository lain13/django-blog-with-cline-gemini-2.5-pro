from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Post, Comment, Tag
from ..forms import CommentForm


class PostListViewTest(TestCase):
    """Post 목록 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        # Given
        User = get_user_model()
        cls.user = User.objects.create_user(username='listuser', password='password')
        for i in range(5):
            Post.objects.create(
                title=f"Test Post {i}",
                content=f"Test Content {i}",
                author=cls.user
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
        User = get_user_model()
        cls.user = User.objects.create_user(username='detailuser', password='password')
        cls.post = Post.objects.create(
            title="A good title",
            content="Nice body content",
            author=cls.user
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

    def test_comment_form_is_displayed(self):
        """상세 페이지에 댓글 폼이 표시되는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        # Then
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    def test_comment_creation(self):
        """새로운 댓글을 성공적으로 생성하는지 테스트"""
        # Given
        initial_comment_count = self.post.comments.count()
        comment_data = {
            'author': 'Test Author',
            'text': 'A new comment'
        }

        # When
        response = self.client.post(reverse('blog:add_comment_to_post', kwargs={'pk': self.post.pk}), data=comment_data)

        # Then
        self.assertEqual(self.post.comments.count(), initial_comment_count + 1)
        new_comment = self.post.comments.last()
        self.assertEqual(new_comment.author, 'Test Author')
        self.assertEqual(new_comment.text, 'A new comment')
        self.assertRedirects(response, reverse('blog:post_detail', kwargs={'pk': self.post.pk}))


class PostCreateViewTest(TestCase):
    """Post 생성 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        User = get_user_model()
        cls.user = User.objects.create_user(username='createuser', password='password')
        cls.url = reverse('blog:post_new')

    def setUp(self):
        """각 테스트 전에 클라이언트 로그인"""
        self.client.login(username='createuser', password='password')

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
        User = get_user_model()
        cls.user = User.objects.create_user(username='updateuser', password='password')
        cls.post = Post.objects.create(
            title='Original Title',
            content='Original Content',
            author=cls.user
        )
        cls.url = reverse('blog:post_edit', kwargs={'pk': cls.post.pk})

    def setUp(self):
        """각 테스트 전에 클라이언트 로그인"""
        self.client.login(username='updateuser', password='password')

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

        # 4. 렌더링된 HTML 내용 확인 (기존 테스트 유지)
        # highlight 필터로 인해 마크업이 추가되어 assertContains가 복잡해지므로,
        # 컨텍스트 데이터 검증으로 대체함.
        # self.assertContains(response, "Apple Banana", html=True)
        # self.assertContains(response, "Second Post", html=True)
        # self.assertNotContains(response, "Third Banana", html=True)

    def test_search_by_content(self):
        """내용으로 검색이 올바르게 동작하는지 테스트"""
        response = self.client.get(reverse('blog:search'), {'q': 'Content one'})
        self.assertContains(response, "Apple Banana")
        self.assertNotContains(response, "Second Post")
        self.assertNotContains(response, "Third Banana")

    def test_search_no_results(self):
        """검색 결과가 없을 때를 올바르게 처리하는지 테스트"""
        response = self.client.get(reverse('blog:search'), {'q': 'NonExistentTerm'})
        self.assertContains(response, "No posts found.")
        self.assertNotContains(response, "Apple Banana")

    def test_search_empty_query(self):
        """검색어가 비어있을 때 모든 포스트를 보여주지 않는지 테스트"""
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


class TagFilteredListViewTest(TestCase):
    """태그 필터링 목록 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        # Given
        User = get_user_model()
        cls.user = User.objects.create_user(username='taguser', password='password')
        cls.tag_python = Tag.objects.create(name="python")
        cls.tag_django = Tag.objects.create(name="django")

        cls.post1 = Post.objects.create(title="Post 1", content="Content 1", author=cls.user)
        cls.post1.tags.add(cls.tag_python)

        cls.post2 = Post.objects.create(title="Post 2", content="Content 2", author=cls.user)
        cls.post2.tags.add(cls.tag_django)

        cls.post3 = Post.objects.create(title="Post 3", content="Content 3", author=cls.user)
        cls.post3.tags.add(cls.tag_python, cls.tag_django)

    def test_view_url_exists_at_desired_location(self):
        """태그 필터링 뷰 URL에 접근 시 200 응답을 반환하는지 테스트"""
        # When
        response = self.client.get(f'/tag/{self.tag_python.name}/')
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """'post_list_by_tag' URL name으로 뷰에 접근 가능한지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_tag', args=[self.tag_python.name]))
        # Then
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """뷰가 올바른 템플릿(post_list.html)을 사용하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_tag', args=[self.tag_python.name]))
        # Then
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_filters_posts_by_tag(self):
        """뷰가 태그에 따라 포스트를 올바르게 필터링하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_tag', args=[self.tag_python.name]))
        # Then
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)
        self.assertContains(response, self.post3.title)
        self.assertEqual(len(response.context['posts']), 2)

    def test_non_existent_tag_returns_not_found(self):
        """존재하지 않는 태그로 접근 시 404를 반환하는지 테스트"""
        # When
        response = self.client.get(reverse('blog:post_list_by_tag', args=['non-existent-tag']))
        # Then
        self.assertEqual(response.status_code, 404)


class PostDeleteViewTest(TestCase):
    """Post 삭제 뷰 관련 테스트"""

    @classmethod
    def setUpTestData(cls):
        """테스트를 위한 데이터 사전 생성"""
        User = get_user_model()
        cls.user = User.objects.create_user(username='deleteuser', password='password')
        cls.post = Post.objects.create(
            title='To be deleted',
            content='Delete me',
            author=cls.user
        )
        cls.url = reverse('blog:post_delete', kwargs={'pk': cls.post.pk})

    def setUp(self):
        """각 테스트 전에 클라이언트 로그인"""
        self.client.login(username='deleteuser', password='password')

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
        self.assertRedirects(response, reverse('blog:post_list'))

        # 2. 포스트 개수가 1 감소했는지 확인
        self.assertEqual(Post.objects.count(), initial_post_count - 1)
