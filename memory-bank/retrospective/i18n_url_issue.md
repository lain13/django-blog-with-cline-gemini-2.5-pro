# 회고: 국제화(i18n) URL `NoReverseMatch` 오류

## 1. 문제 현상

- 개발 서버 실행 후 메인 페이지(`/`) 접근 시 `django.urls.exceptions.NoReverseMatch: Reverse for 'set_language' not found.` 오류 발생
- 오류의 근원지는 `blog/templates/blog/base.html` 템플릿의 `{% url 'set_language' %}` 태그 부분으로 확인됨.

## 2. 근본 원인 분석 (Git 로그 분석)

- 국제화 기능이 처음 도입된 커밋(`7f7b7df83dc827c32ee6d0adef2786081f4ba747`)을 `git show`로 분석한 결과, 당시에는 `config/urls.py`에 `path('i18n/', include('django.conf.urls.i18n'))` 설정이 올바르게 추가되었었음.
- 하지만, 이후 다른 기능 추가 및 리팩토링 과정에서 `config/urls.py`의 `urlpatterns` 구조가 변경되면서 해당 라인이 누락되어 현재의 오류가 발생한 것으로 판단됨.

## 3. 테스트 코드의 한계 (Test Blind Spot)

- `blog/tests/test_i18n.py`에 `test_language_switcher`라는 언어 전환 기능 테스트가 존재했음에도 불구하고 이 오류를 사전에 발견하지 못했음.
- 원인은 테스트 코드 내에서 URL을 `reverse('set_language')`로 생성하지 않고, `self.client.post('/i18n/setlang/', ...)` 와 같이 **하드코딩된 URL 경로**를 직접 사용했기 때문임.
- 이로 인해 테스트는 언어 전환 기능의 로직(쿠키 설정, 리다이렉트 등)은 검증했지만, 템플릿의 `{% url 'set_language' %}` 태그가 정상적으로 URL을 리졸브(resolve)하는지는 검증하지 못하는 '맹점(Blind Spot)'이 존재했음.

## 4. 재발 방지 및 해결 계획 (Action Plan)

1.  **실패하는 테스트 작성 (다음 태스크)**:
    - `test_language_switcher` 테스트를 수정하여 하드코딩된 URL 대신 `reverse('set_language')`를 사용하도록 변경한다. 이 테스트는 현재 상태에서 `NoReverseMatch` 오류를 발생시키며 실패할 것이다 (Red).
    - 또는, `post_list` 페이지와 같이 언어 전환 폼이 포함된 페이지를 GET으로 요청하여 템플릿 렌더링이 성공하는지 확인하는 테스트를 추가한다.

2.  **코드 수정 (다음 태스크)**:
    - `config/urls.py`의 `urlpatterns`에 `path('i18n/', include('django.conf.urls.i18n'))`를 추가하여 테스트를 통과시킨다 (Green).

3.  **테스트 원칙 강화**:
    - 향후 테스트 코드 작성 시, URL을 사용하는 기능은 반드시 `reverse()` 함수를 사용하여 URL을 동적으로 생성하도록 `.clinerules/testing.md`에 명시한다. 이는 URL 구조 변경 시 관련 테스트가 실패하도록 보장하여 회귀(regression)를 방지한다.
