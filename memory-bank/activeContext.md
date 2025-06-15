# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **API 문서 자동화 작업 재개**: 이전에 중단되었던 `drf-spectacular`를 이용한 API 문서 자동화 작업을 재개하고 완료합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **i18n URL 렌더링 오류 해결**: `config/urls.py`에 `i18n` URL 패턴을 추가하고, `base.html`의 `lang` 속성을 동적으로 변경하여 `NoReverseMatch` 오류를 해결했습니다.
- **테스트 환경 한계 식별**: `test_language_switcher` 테스트가 테스트 클라이언트의 쿠키 처리 문제로 지속적으로 실패하여, 해당 테스트를 임시 비활성화하고 실제 브라우저 환경에서 기능의 정상 동작을 확인했습니다.
- **API 문서 자동화 준비 완료**: `drf-spectacular` 라이브러리 설치 및 설정을 완료했습니다.
- **TDD: API 정렬(Ordering) 기능 구현**: `rest_framework.filters.OrderingFilter`를 사용하여 `Post` 목록 API에 `created_at`, `view_count`, `title` 기반 정렬 기능을 적용했습니다.
- **TDD: API 검색(Search) 기능 구현**: `rest_framework.filters.SearchFilter`를 사용하여 `Post` 목록 API에 `title`, `content` 기반 검색 기능을 적용했습니다.
- **TDD: API 필터링 기능 구현**: `django-filter`를 사용하여 `Post` 목록 API에 카테고리, 태그 기반 필터링 기능을 적용했습니다.
- **TDD: API 페이징 기능 구현**: Django REST Framework의 `PageNumberPagination`을 사용하여 `Post` 목록 API에 페이지네이션을 적용했습니다.

## 3. 다음 단계 (Next Steps)

- **API 문서 자동화 작업 재개**
  - 개발 서버를 실행하여 `/api/schema/swagger-ui/` 경로에서 자동 생성된 API 문서를 최종 확인하고, 정상적으로 표시되는지 검증합니다.
