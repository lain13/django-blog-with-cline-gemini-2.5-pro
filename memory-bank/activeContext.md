# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **페이징 기능 구현 (Pagination)**
- `ListView`를 사용하는 모든 뷰(게시글 목록, 카테고리별, 태그별, 검색 결과)에 페이지네이션 기능을 TDD 방식으로 구현합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **RSS 피드 기능 구현 완료**: TDD 사이클에 따라 최신 게시글을 제공하는 기본 RSS 피드(`LatestPostsFeed`)를 구현하고, `base.html`에 링크를 추가했습니다.
- **테스트 코드 리팩토링 완료**: `test_views.py`와 `test_models.py`를 기능/모델 단위로 분리하는 작업을 완료했습니다.

## 3. 다음 단계 (Next Steps)

- **1. 페이징 기능 테스트 코드 작성 (TDD - Red)**
  - `blog/tests/test_pagination.py` 파일을 생성하고, 페이지네이션 관련 테스트 케이스를 작성합니다. (e.g., 페이지 번호 유효성, 컨텍스트 변수 확인, 템플릿 렌더링 등)

- **2. 페이징 기능 구현 (TDD - Green)**
  - `PostListView` 및 관련 뷰에 `Paginator`를 적용하여 페이징 로직을 추가합니다.
  - 템플릿에 페이지 네비게이션 UI를 추가합니다.

- **3. 코드 리팩토링 (TDD - Refactor)**
  - 페이징 관련 코드의 가독성과 효율성을 개선합니다.
