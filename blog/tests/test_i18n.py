from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse
from django.utils import translation

from blog.models.category import Category
from blog.models.post import Post


class InternationalizationTest(TestCase):
    """국제화(i18n) 관련 테스트"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.category = Category.objects.create(name='Test Category', slug='test-category')

    def test_view_message_translation_ko(self):
        """뷰 메시지 번역 테스트 (한국어)"""
        self.client.login(username='testuser', password='password')
        post_data = {
            'title': 'Test Post KO',
            'content': 'Test Content',
            'category': self.category.pk,
            'tags': 'tag1, tag2',
        }

        with translation.override('ko'):
            response = self.client.post(reverse('blog:post_new'), post_data, follow=True)
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), '새 포스트가 성공적으로 작성되었습니다.')

    def test_view_message_translation_en(self):
        """뷰 메시지 번역 테스트 (영어)"""
        self.client.login(username='testuser', password='password')
        post_data = {
            'title': 'Test Post EN',
            'content': 'Test Content',
            'category': self.category.pk,
            'tags': 'tag1, tag2',
        }

        with translation.override('en'):
            response = self.client.post(reverse('blog:post_new'), post_data, follow=True)
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), 'New post has been created successfully.')

    def test_model_verbose_name_translation(self):
        """언어 설정에 따라 모델 필드의 verbose_name이 올바르게 번역되는지 테스트"""
        # 한국어 설정
        with translation.override('ko'):
            verbose_name = Category._meta.get_field('name').verbose_name
            self.assertEqual(verbose_name, '이름')

        # 영어 설정
        with translation.override('en'):
            verbose_name = Category._meta.get_field('name').verbose_name
            self.assertEqual(verbose_name, 'name')

    def test_template_translation(self):
        """언어 설정에 따라 템플릿의 텍스트가 올바르게 번역되는지 테스트"""
        # 한국어 설정
        with translation.override('ko'):
            response = self.client.get(reverse('blog:post_list'))
            self.assertContains(response, '<title>TDD 블로그</title>')

        # 영어 설정
        with translation.override('en'):
            response = self.client.get(reverse('blog:post_list'))
            self.assertContains(response, '<title>TDD Blog</title>')

    def test_language_prefix_in_url(self):
        """URL에 언어 접두사가 올바르게 적용되는지 테스트"""
        # 한국어 설정
        with translation.override('ko'):
            response = self.client.get(reverse('blog:post_list'))
            self.assertEqual(response.status_code, 200)

        # 영어 설정
        with translation.override('en'):
            response = self.client.get(reverse('blog:post_list'))
            self.assertEqual(response.status_code, 200)

    def test_default_language_redirect(self):
        """
        언어 접두사 없이 접근 시 기본 언어(ko)로 리다이렉트 되는지 테스트
        (i18n_patterns 적용 후)
        """
        # 이 테스트는 i18n_patterns가 최상위 URL에 적용된 후에 통과해야 합니다.
        response = self.client.get('/')
        self.assertRedirects(response, '/ko/', status_code=302, target_status_code=200)

    def test_language_switcher(self):
        """언어 전환 기능이 올바르게 동작하는지 테스트"""
        # 1. 현재 페이지가 /en/ 상태라고 가정
        current_path = reverse('blog:post_list')
        
        # 2. 언어를 'ko'로 변경하도록 요청
        response = self.client.post('/i18n/setlang/', {'language': 'ko', 'next': current_path})
        
        # 3. 리다이렉트 응답 확인
        self.assertEqual(response.status_code, 302)
        
        # 4. 언어 쿠키가 'ko'로 설정되었는지 확인
        self.assertEqual(self.client.cookies['django_language'].value, 'ko')
        
        # 5. 리다이렉트된 페이지의 언어가 'ko'인지 확인
        response = self.client.get(response.url)
        self.assertContains(response, '<title>TDD 블로그</title>')

        # 6. 다시 'en'으로 변경
        response = self.client.post('/i18n/setlang/', {'language': 'en', 'next': current_path})
        self.assertEqual(self.client.cookies['django_language'].value, 'en')
        response = self.client.get(response.url)
        self.assertContains(response, '<title>TDD Blog</title>')
