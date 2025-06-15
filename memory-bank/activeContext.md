# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **Phase 1: 주요 API 엔드포인트 추가 (Major API Endpoints)**
- `Post`와 `User` 외에 다른 주요 모델들(Comment, Category, Tag)에 대한 API 엔드포인트를 TDD 방식으로 구현합니다.
- 첫 번째 목표는 `Comment` 모델에 대한 CRUD API를 구현하는 것입니다.

## 2. 최근 변경 사항 (Recent Changes)

- **작업 계획 수립**: `progress.md`에 명시된 미완료 작업을 바탕으로, API 기능 추가 및 문서 자동화를 위한 3단계 계획(Phase 1-3)을 수립했습니다.
- **국제화(i18n) 기능 구현 완료**: 모델, 뷰, 템플릿 번역 및 언어 전환 기능 구현을 모두 완료했습니다.

## 3. 다음 단계 (Next Steps)

- **TDD: Comment API 구현**
  - `CommentSerializer` 생성
  - `CommentListCreateAPIView` 및 `CommentRetrieveUpdateDestroyAPIView` 생성
  - 관련 URL 설정
  - 기능 및 권한을 검증하는 테스트 코드 작성 (`blog/tests/test_api_views.py`)
