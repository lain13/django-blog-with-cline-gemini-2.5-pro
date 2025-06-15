# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **i18n `NoReverseMatch` 오류 해결**: `base.html` 템플릿에서 발생하는 `set_language` URL 렌더링 오류를 해결합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **i18n URL 렌더링 오류 원인 분석 및 회고**: Git 로그 분석을 통해 `NoReverseMatch` 오류의 근본 원인을 파악하고, 테스트 코드의 맹점을 분석하여 `memory-bank/retrospective/i18n_url_issue.md`에 회고 문서를 작성했습니다.
- **API 문서 자동화 준비 완료**: `drf-spectacular` 라이브러리 설치 및 설정을 완료했습니다. (오류로 인해 중단)
- **TDD: API 정렬(Ordering) 기능 구현**: `rest_framework.filters.OrderingFilter`를 사용하여 `Post` 목록 API에 `created_at`, `view_count`, `title` 기반 정렬 기능을 적용했습니다.
- **TDD: API 검색(Search) 기능 구현**: `rest_framework.filters.SearchFilter`를 사용하여 `Post` 목록 API에 `title`, `content` 기반 검색 기능을 적용했습니다.
- **TDD: API 필터링 기능 구현**: `django-filter`를 사용하여 `Post` 목록 API에 카테고리, 태그 기반 필터링 기능을 적용했습니다.
- **TDD: API 페이징 기능 구현**: Django REST Framework의 `PageNumberPagination`을 사용하여 `Post` 목록 API에 페이지네이션을 적용했습니다.

## 3. 다음 단계 (Next Steps)

- **`NoReverseMatch` 오류 해결 (TDD)**
  1.  **Red**: `test_i18n.py`의 `test_language_switcher` 테스트가 `reverse('set_language')`를 사용하도록 수정하여 실패하는 것을 확인합니다.
  2.  **Green**: `config/urls.py`에 `path('i18n/', include('django.conf.urls.i18n'))`를 추가하여 테스트를 통과시킵니다.
  3.  **Refactor**: 관련 코드를 검토하고 개선합니다.
- **API 문서 자동화 작업 재개**
  - 개발 서버를 실행하여 자동 생성된 API 문서를 최종 확인합니다.
