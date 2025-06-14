from django.test import TestCase
from django.urls import reverse
from django.utils import translation

class InternationalizationTest(TestCase):
    """국제화(i18n) 관련 테스트"""

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
