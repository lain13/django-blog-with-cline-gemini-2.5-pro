# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **신규 기능 개발 (New Feature Development)**
- Post 수정일, 댓글, 검색 기능을 TDD 방법론에 따라 순차적으로 개발한다.

## 2. 최근 변경 사항 (Recent Changes)

- **`memory-bank/projectbrief.md` 업데이트**: 신규 기능 요구사항(댓글, 검색) 추가.

## 3. 다음 단계 (Next Steps)

1.  **`memory-bank/progress.md` 업데이트**: 신규 기능 개발 계획 반영.
2.  **Phase 1: Post 수정일 추가**:
    - `blog/models.py`의 `Post` 모델에 `modified_at` 필드 추가.
    - 데이터베이스 마이그레이션 실행.
    - `modified_at` 필드 검증 테스트 작성 및 실행.
    - 템플릿에 수정일 표시.
