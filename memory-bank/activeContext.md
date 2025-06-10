# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **댓글 시스템 개선 (Nested Comments)**
- 게시글 CRUD에 대한 인증/권한 제어 기능 구현을 완료했습니다. 이제 `progress.md`에 명시된 다음 작업인 '댓글 시스템 개선'을 진행할 준비가 되었습니다.

## 2. 최근 변경 사항 (Recent Changes)

- **인증/권한 제어 구현 완료**: TDD 사이클을 통해 `blog` 앱의 핵심 기능에 인증 및 권한 제어를 성공적으로 적용했습니다.
  - `LoginRequiredMixin`을 사용하여 로그인한 사용자만 게시글을 생성/수정/삭제할 수 있도록 제한했습니다.
  - `UserPassesTestMixin`을 상속한 `AuthorRequiredMixin`을 만들어, 게시글 작성자 본인만 수정/삭제할 수 있도록 권한을 설정했습니다.
  - `settings.py`에 `LOGIN_URL`을 명시하여 리다이렉트 문제를 해결했습니다.
  - `blog/tests/test_views.py`에 `PostProtectionTest` 테스트 스위트를 추가하여 위 기능들이 올바르게 동작하는지 검증했습니다.

## 3. 다음 단계 (Next Steps)

- **TDD를 통한 댓글 시스템 개선 구현**
  - `Comment` 모델 개선 및 관련 테스트 작성을 완료했습니다.
  - 다음 Task에서는 아래의 TDD 사이클에 따라 댓글 관련 뷰의 인증/권한 제어를 구현합니다.
  1.  **Red**: 익명 사용자가 아닌 로그인한 사용자만 댓글을 작성할 수 있는지, 그리고 본인의 댓글만 수정/삭제할 수 있는지 검증하는 **실패하는 테스트**를 `blog/tests/test_views.py`에 작성합니다.
  2.  **Green**: 댓글 관련 뷰(`Create`, `Update`, `Delete`)를 수정하여 테스트를 통과시킵니다.
  3.  **Refactor**: 전체 테스트가 통과하는지 확인하고 코드를 정리합니다.
