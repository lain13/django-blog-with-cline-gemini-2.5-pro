# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **사용자 인증 시스템 권한 적용**
- `blog` 앱의 템플릿 상속 구조 리팩토링을 완료하여 UI 일관성을 확보했습니다. 이제 `progress.md`에 명시된 다음 작업인 '게시글 작성/수정/삭제 기능에 로그인 권한 적용'을 진행할 준비가 되었습니다.

## 2. 최근 변경 사항 (Recent Changes)

- **템플릿 리팩토링 완료**: TDD 사이클을 통해 `blog` 앱의 모든 주요 템플릿(`post_list`, `post_detail`, `post_form`, `post_confirm_delete`, `search_results`)이 `base.html`을 상속하도록 수정했습니다.
- **템플릿 테스트 추가**: `blog/tests/test_templates.py`를 생성하여 템플릿 상속 구조를 검증하는 테스트 케이스를 추가했습니다. 이로써 향후 유사한 기술 부채가 발생하는 것을 방지하는 안전망을 확보했습니다.

## 3. 다음 단계 (Next Steps)

- **TDD를 통한 인증/권한 제어 구현**
  - 다음 Task에서는 아래의 TDD 사이클에 따라 `blog` 앱의 핵심 기능에 인증 및 권한 제어를 적용합니다.
  1.  **Red**: 로그아웃 상태에서 게시글 생성/수정/삭제 페이지 접근 시 로그인 페이지로 리다이렉트되는지 확인하는 **실패하는 테스트**를 작성합니다.
  2.  **Green**: Django의 `LoginRequiredMixin`을 `PostCreateView`, `PostUpdateView`, `PostDeleteView`에 적용하여 테스트를 통과시킵니다.
  3.  **Red**: 다른 사용자의 게시글 수정/삭제 페이지에 접근 시 `403 Forbidden` 오류가 발생하는지 확인하는 **실패하는 테스트**를 작성합니다.
  4.  **Green**: `UserPassesTestMixin` 또는 유사한 권한 제어 로직을 `PostUpdateView`, `PostDeleteView`에 추가하여 본인 게시글만 수정/삭제할 수 있도록 제한하고 테스트를 통과시킵니다.
  5.  **Refactor**: 전체 테스트가 통과하는지 확인하고 코드를 정리합니다.
