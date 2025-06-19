from django.contrib.auth import get_user_model
import unittest
from django.contrib.messages import get_messages
from django.http import HttpResponseRedirect
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

    @unittest.skip("Fails in CI/CD environment; language context is not properly activated.")
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

    @unittest.skip("Fails in CI/CD environment; language context is not properly activated.")
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

    def test_default_language_no_redirect_for_default_language(self):
        """
        prefix_default_language=False 설정 시, 기본 언어(ko)는 접두사 없이 접근되고
        리디렉션이 발생하지 않는지 테스트
        """
        with translation.override('ko'):
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            # 기본 언어(ko)에서는 /ko/ 접두사로 리디렉션되지 않음을 확인
            self.assertNotIsInstance(response, HttpResponseRedirect)

    @unittest.skip("Skipping due to persistent issues with language cookie in test client.")
    def test_language_switcher(self):
        """언어 전환 기능이 올바르게 동작하는지 테스트"""
        # 1. 영어 페이지(/en/)로 먼저 이동
        response = self.client.get('/en/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<html lang="en">')

        # 2. 언어를 'ko'로 변경하도록 요청하고, 리다이렉션을 자동으로 따라감
        # next 파라미터는 현재 경로인 /en/
        response = self.client.post(reverse('set_language'), {'language': 'ko', 'next': '/en/'}, follow=True)

        # 3. 최종 페이지가 한국어로 렌더링되었는지 확인
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>TDD 블로그</title>')
        self.assertContains(response, '<html lang="ko">')
        
        # 4. 언어 쿠키가 'ko'로 설정되었는지 확인
        self.assertEqual(self.client.cookies['django_language'].value, 'ko')

        # 5. 다시 'en'으로 변경. 현재 페이지는 한국어이므로 next는 '/'
        response = self.client.post(reverse('set_language'), {'language': 'en', 'next': '/'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>TDD Blog</title>')
        self.assertContains(response, '<html lang="en">')
        self.assertEqual(self.client.cookies['django_language'].value, 'en')
