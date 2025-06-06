# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **신규 기능 개발 (New Feature Development)**
- 댓글(Comment) 기능을 TDD 방법론에 따라 개발한다.

## 2. 최근 변경 사항 (Recent Changes)

- **`feat(blog)`**: `updated_at` 필드 동작을 검증하는 테스트를 추가하고, 템플릿에 생성/수정 시간을 표시하도록 수정함.
- **`docs(memory-bank)`**: 신규 기능 개발 계획을 문서에 반영함.

## 3. 다음 단계 (Next Steps)

1.  **`memory-bank/progress.md` 업데이트**: 'Phase 1' 완료 상태 반영.
2.  **Phase 2: 댓글 기능 추가**:
    - `Comment` 모델 정의 (Post와 Foreign Key 연결)
    - 데이터베이스 마이그레이션 실행.
    - `Comment` 모델 및 `CommentForm` 테스트 작성.
    - `CommentForm` 생성.
    - 댓글 생성/조회 View, URL, Template 구현.
