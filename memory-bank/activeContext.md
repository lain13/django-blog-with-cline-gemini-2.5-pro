# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **Phase 3: API 문서 자동화 (API Documentation)**
- `drf-spectacular` 라이브러리를 도입하여 API 문서를 자동으로 생성합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **TDD: API 정렬(Ordering) 기능 구현**: `rest_framework.filters.OrderingFilter`를 사용하여 `Post` 목록 API에 `created_at`, `view_count`, `title` 기반 정렬 기능을 적용했습니다.
- **TDD: API 검색(Search) 기능 구현**: `rest_framework.filters.SearchFilter`를 사용하여 `Post` 목록 API에 `title`, `content` 기반 검색 기능을 적용했습니다.
- **TDD: API 필터링 기능 구현**: `django-filter`를 사용하여 `Post` 목록 API에 카테고리, 태그 기반 필터링 기능을 적용했습니다.
- **TDD: API 페이징 기능 구현**: Django REST Framework의 `PageNumberPagination`을 사용하여 `Post` 목록 API에 페이지네이션을 적용했습니다.
- **코드 주석 개선**: 프로젝트 전반의 소스 코드에 포함된 영어 주석을 한국어로 번역하여 코드 가독성을 향상시켰습니다.
- **작업 계획 수립**: `progress.md`에 명시된 미완료 작업을 바탕으로, API 기능 추가 및 문서 자동화를 위한 3단계 계획(Phase 1-3)을 수립했습니다.
- **국제화(i18n) 기능 구현 완료**: 모델, 뷰, 템플릿 번역 및 언어 전환 기능 구현을 모두 완료했습니다.

## 3. 다음 단계 (Next Steps)

- **API 문서 자동화 (`drf-spectacular`)**
  - `drf-spectacular` 라이브러리 설치 및 `requirements.txt` 업데이트
  - `settings.py`에 `drf_spectacular` 앱 등록 및 설정 추가
  - `config/urls.py`에 Swagger/OpenAPI 문서 경로 추가
  - 자동 생성된 API 문서 확인
