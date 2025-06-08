# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **사용자 인증 시스템 개발 (User Authentication System Development)**
- 계층형 카테고리 기능의 마지막 단계인 뷰와 템플릿 구현을 완료했으며, 이제 새로운 기능인 사용자 인증 시스템 구현을 시작할 준비가 되었습니다.

## 2. 최근 변경 사항 (Recent Changes)

- **`feat(view)`**: TDD 사이클(Red-Green)을 통해 `CategoryPostListView`를 구현하여 카테고리별 게시글 목록 기능을 완성했습니다.
- **`feat(url)`**: `blog/urls/` 패키지 내에 `category_urls.py`를 추가하고, `__init__.py`를 수정하여 카테고리 URL을 프로젝트에 통합했습니다.
- **`test(view)`**: `CategoryPostListView`에 대한 실패하는 테스트를 먼저 작성하고, 기능 구현 후 테스트가 통과함을 확인했습니다.
- **`fix(url)`**: `NoReverseMatch` 오류 해결을 위해 `blog/urls/__init__.py`가 URL 설정의 중심이 되도록 구조를 수정하고 정리했습니다.
- **`docs(memory-bank)`**: `activeContext.md`와 `progress.md`를 현재 상태에 맞게 업데이트했습니다.

## 3. 다음 단계 (Next Steps)

- **사용자 인증 시스템 구현**
  - **TDD (Red)**: Django의 내장 `AuthenticationForm`을 사용한 로그인 뷰에 대한 실패하는 테스트(`test_views.py` 또는 신규 `test_auth.py`)를 작성합니다.
  - **URL 설계**: `login/`, `logout/` URL을 `users/urls.py` (신규 앱 `users` 생성 후) 또는 `blog/urls/auth_urls.py`에 정의합니다.
  - **뷰 구현**: 로그인/로그아웃 기능을 처리하는 뷰를 작성합니다.
  - **템플릿 생성**: `login.html` 템플릿을 생성합니다.
