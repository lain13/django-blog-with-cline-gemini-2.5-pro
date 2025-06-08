from django.test import TestCase
from ..models import Post, Tag
from ..forms import CommentForm, PostForm


class PostFormTest(TestCase):
    """PostForm 관련 테스트"""

    def test_form_has_tags_field(self):
        """폼에 tags 필드가 존재하는지 테스트"""
        form = PostForm()
        self.assertIn('tags', form.fields)

    def test_form_tags_are_optional(self):
        """태그 없이도 폼이 유효한지 테스트"""
        form_data = {'title': 'Test Title', 'content': 'Test Content', 'tags': ''}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_populates_tags_for_existing_post(self):
        """기존 포스트의 태그를 폼에 올바르게 채우는지 테스트"""
        # Given
        post = Post.objects.create(title="Test Post", content="Content")
        tag1 = Tag.objects.create(name="django")
        tag2 = Tag.objects.create(name="python")
        post.tags.add(tag1, tag2)

        # When
        form = PostForm(instance=post)

        # Then
        self.assertEqual(form.initial.get('tags'), 'django, python')


class CommentFormTest(TestCase):
    """CommentForm 관련 테스트"""

    def test_form_is_valid_with_data(self):
        """폼에 유효한 데이터가 입력되었을 때 폼이 유효한지 테스트"""
        # Given
        form_data = {'text': 'A valid comment'}
        form = CommentForm(data=form_data)
        # Then
        self.assertTrue(form.is_valid())

    def test_form_is_invalid_without_data(self):
        """폼에 데이터가 입력되지 않았을 때 폼이 유효하지 않은지 테스트"""
        # Given
        form = CommentForm(data={})
        # Then
        self.assertFalse(form.is_valid())
        self.assertIn('text', form.errors)
