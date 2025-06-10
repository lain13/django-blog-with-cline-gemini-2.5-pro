# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **조회수 카운터 기능 구현 (View Count)**
- 댓글 시스템의 인증/권한 제어 기능 구현을 완료했습니다. 이제 `progress.md`에 명시된 다음 작업인 '조회수 카운터' 기능을 구현할 준비가 되었습니다.

## 2. 최근 변경 사항 (Recent Changes)

- **댓글 시스템 인증/권한 제어 구현 완료**: TDD 사이클을 통해 `blog` 앱의 댓글 기능에 인증 및 권한 제어를 성공적으로 적용했습니다.
  - `CommentCreateView`, `CommentUpdateView`, `CommentDeleteView`를 구현하고 `LoginRequiredMixin`과 `AuthorRequiredMixin`을 적용했습니다.
  - `blog/tests/test_views.py`에 `CommentProtectionTest` 테스트 스위트를 추가하여 로그인 및 작성자 권한을 검증했습니다.
  - `post_detail.html` 템플릿을 리팩토링하여, 커스텀 템플릿 태그(`comment_form_tag`)를 통해 댓글 폼을 분리하고, 권한에 따라 수정/삭제 링크를 동적으로 표시하도록 개선했습니다.
  - 관련 테스트 코드(`PostDetailViewTest`, `TemplateInheritanceTest`)를 리팩토링하여 변경된 사항을 반영하고 모든 테스트가 통과하도록 수정했습니다.

## 3. 다음 단계 (Next Steps)

- **TDD를 통한 조회수 카운터 기능 구현**
  1.  **Red**: `Post` 모델에 `view_count` 필드를 추가하고, 조회수 증가 로직에 대한 **실패하는 테스트**를 `blog/tests/test_models.py`에 작성합니다. (중복 조회 방지 로직 포함)
  2.  **Green**: 테스트를 통과하는 최소한의 코드를 `Post` 모델에 작성합니다.
  3.  **Refactor**: 코드를 정리하고, `PostDetailView`에 조회수 증가 로직을 적용합니다.
  4.  **Documentation**: `progress.md`와 `activeContext.md`를 업데이트합니다.
