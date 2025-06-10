# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **RSS 피드 기능 구현**
- `progress.md`에 명시된 다음 작업인 RSS 피드 기능 구현을 TDD 사이클에 따라 진행합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **테스트 구조 리팩토링 완료**: `blog/tests/test_views.py` 파일을 `test_post_views.py`, `test_comment_views.py`, `test_vote_views.py`로 성공적으로 분리하여 테스트 코드의 가독성과 유지보수성을 향상시켰습니다.

## 3. 다음 단계 (Next Steps)

- **RSS 피드 기능 구현 (TDD)**
  1.  Django의 `syndication` 프레임워크를 활용한 RSS 피드 클래스 구현을 위한 실패하는 테스트(`test_feeds.py`)를 작성합니다.
  2.  테스트를 통과하는 최소한의 코드를 작성합니다. (Red-Green)
  3.  필요시 코드를 리팩토링합니다.
  4.  RSS 피드 관련 URL을 등록하고, 템플릿에 링크를 추가합니다.
  5.  기능 구현 완료 후 관련 문서를 업데이트합니다.
