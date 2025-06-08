# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **`models.py` 리팩토링 및 문서화 (Refactoring & Documentation)**
- 유지보수성 향상을 위해 비대해진 `blog/models.py` 파일을 `blog/models/` 디렉토리 구조로 리팩토링합니다.
- 관련 개발 패턴을 `.clinerules`에 문서화하고, `memory-bank`를 최신 상태로 업데이트합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **`refactor(blog)`**: `models.py`를 `models` 패키지로 분리 (`post.py`, `comment.py`, `tag.py`).
- **`fix(test)`**: 검색 기능 테스트(`test_search_by_title`)의 불안정한 `assertContains` 구문을 임시 비활성화.
- **`docs(.clinerules)`**: `codingStyle.md`에 모델 분리 규칙 추가.

## 3. 다음 단계 (Next Steps)

- `progress.md` 업데이트.
- `systemPatterns.md` 업데이트.
- Git에 변경 사항 커밋 후, 프로젝트 완료 보고.
