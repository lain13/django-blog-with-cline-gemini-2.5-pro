# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **좋아요/싫어요 기능 구현 (Like/Dislike System)**
- 알려진 버그(로그인/로그아웃 오류)를 모두 해결했으며, 이제 `progress.md`에 명시된 다음 작업인 '좋아요/싫어요 기능'을 구현할 준비가 되었습니다.

## 2. 최근 변경 사항 (Recent Changes)

- **로그인/로그아웃 버그 수정 완료**:
  - `settings.py`에 `LOGIN_REDIRECT_URL = '/'`를 추가하여 로그인 후 'Page not found' 오류가 발생하는 문제를 해결했습니다.
  - `base.html`의 로그아웃 링크를 `<a>` 태그에서 `<form>`을 사용한 POST 요청 방식으로 변경하여 'HTTP 405' 오류를 해결했습니다.
- **조회수 카운터 기능 구현 완료**: TDD 사이클을 통해 `Post` 모델에 조회수 기능을 성공적으로 구현했습니다.
  - `Post` 모델에 `view_count` 필드와 `increase_view_count` 메서드를 추가하고 관련 모델 테스트를 작성했습니다.
  - `migrate` 과정에서 발생한 `IntegrityError`를 데이터베이스 및 마이그레이션 파일 초기화를 통해 해결했습니다.
  - `PostDetailView`의 `get_object` 메서드를 오버라이드하여 게시글 조회 시 `view_count`가 증가하도록 구현했습니다.
  - `post_detail.html` 템플릿에 조회수를 표시하고, 관련 뷰 테스트를 작성하여 모든 테스트가 통과하도록 수정했습니다.

## 3. 다음 단계 (Next Steps)

- **TDD를 통한 좋아요/싫어요 기능 구현**
  1.  **Red**: `Vote` 모델을 정의하고, 관련 기능에 대한 **실패하는 테스트**를 `blog/tests/test_models.py`에 작성합니다.
  2.  **Green**: 테스트를 통과하는 최소한의 코드를 `Vote` 모델과 `Post` 모델에 작성합니다.
  3.  **Refactor**: 코드를 정리하고, AJAX를 사용하여 좋아요/싫어요를 처리하는 뷰 로직을 구현합니다.
  4.  **Documentation**: `progress.md`와 `activeContext.md`를 업데이트합니다.
