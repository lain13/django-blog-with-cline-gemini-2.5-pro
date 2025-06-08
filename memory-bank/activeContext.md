# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **테스트 코드 리팩토링 (Test Code Refactoring)**
- `blog/tests.py` 파일을 `blog/tests/` 패키지 구조로 리팩토링하여 가독성과 유지보수성을 향상시킵니다.

## 2. 최근 변경 사항 (Recent Changes)

- **`refactor(blog)`**: `blog/tests.py`를 `blog/tests/` 디렉토리 구조로 리팩토링.
  - `blog/tests/test_models.py` 생성
  - `blog/tests/test_views.py` 생성
  - `blog/tests/test_forms.py` 생성
  - `blog/tests/__init__.py` 수정하여 테스트 로더 설정
- **`docs(.clinerules)`**: `workflow.md`에 테스트 구조 관련 규칙 추가.

## 3. 다음 단계 (Next Steps)

- `progress.md` 업데이트.
- Git에 변경 사항 커밋 후, 프로젝트 완료 보고.
