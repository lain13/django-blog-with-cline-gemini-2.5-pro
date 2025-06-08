from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def highlight(text, query):
    if not query:
        return text
    
    # 대소문자 구분 없이 query를 찾기 위해 re.IGNORECASE 사용
    # re.escape를 사용하여 query에 포함될 수 있는 정규표현식 특수 문자를 이스케이프 처리
    highlighted_text = re.sub(
        f'({re.escape(query)})', 
        r'<mark>\1</mark>', 
        text, 
        flags=re.IGNORECASE
    )
    
    return mark_safe(highlighted_text)
