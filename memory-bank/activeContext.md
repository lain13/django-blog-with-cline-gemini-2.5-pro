# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **RSS 피드 기능 구현 (RSS Feed)**
- '좋아요/싫어요' 기능 구현을 성공적으로 완료했으며, 이제 `progress.md`에 명시된 다음 작업인 'RSS 피드 기능'을 구현할 준비가 되었습니다.

## 2. 최근 변경 사항 (Recent Changes)

- **좋아요/싫어요 기능 구현 완료**: TDD 사이클을 통해 `Vote` 모델 기반의 좋아요/싫어요 기능을 성공적으로 구현했습니다.
  - `Vote` 모델을 정의하고 모델 테스트(`test_models.py`)를 작성하여 통과시켰습니다.
  - `VoteView`를 작성하고 관련 뷰 테스트(`test_views.py`)를 작성하여 통과시켰습니다. 이 과정에서 `JSONDecodeError`와 `AttributeError`를 해결했습니다.
  - `post_detail.html` 템플릿에 AJAX를 사용하여 비동기적으로 투표를 처리하는 UI와 스크립트를 추가했습니다.
  - `PostDetailView`에 `user_vote` 컨텍스트를 추가하고, `base.html`에 `extra_js` 블록을 추가하여 스크립트가 올바르게 작동하도록 수정했습니다.
  - `systemPatterns.md`의 ERD와 `progress.md`의 진행 상황을 최신 상태로 업데이트했습니다.

## 3. 다음 단계 (Next Steps)

- **TDD를 통한 RSS 피드 기능 구현**
  1.  **Red**: Django의 `syndication` 프레임워크를 사용하여 최신 게시글 피드를 제공하는 기능에 대한 **실패하는 테스트**를 작성합니다.
  2.  **Green**: 테스트를 통과하는 최소한의 코드를 작성합니다. (`feeds.py` 생성, `urls.py`에 연동)
  3.  **Refactor**: 코드를 정리하고, 필요한 경우 커스텀 피드 로직을 추가합니다.
  4.  **Documentation**: `progress.md`와 `activeContext.md`를 업데이트합니다.
