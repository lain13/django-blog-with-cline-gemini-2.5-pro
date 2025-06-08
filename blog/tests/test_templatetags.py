from django.test import TestCase
from ..templatetags.blog_tags import highlight

class TemplateTagsTest(TestCase):
    """Template tags 관련 테스트"""

    def test_highlight_filter(self):
        """highlight 필터가 검색어를 <mark> 태그로 감싸는지 테스트"""
        # Given
        text = "This is a simple test."
        query = "simple"
        
        # When
        highlighted_text = highlight(text, query)
        
        # Then
        expected_html = 'This is a <mark>simple</mark> test.'
        self.assertEqual(highlighted_text, expected_html)

    def test_highlight_filter_no_match(self):
        """일치하는 검색어가 없을 때 텍스트가 변경되지 않는지 테스트"""
        # Given
        text = "This is a simple test."
        query = "nomatch"
        
        # When
        highlighted_text = highlight(text, query)
        
        # Then
        self.assertEqual(highlighted_text, text)

    def test_highlight_filter_case_insensitive(self):
        """필터가 대소문자를 구분하지 않고 동작하는지 테스트"""
        # Given
        text = "This is a Simple test."
        query = "simple"
        
        # When
        highlighted_text = highlight(text, query)
        
        # Then
        expected_html = 'This is a <mark>Simple</mark> test.'
        self.assertEqual(highlighted_text, expected_html)
