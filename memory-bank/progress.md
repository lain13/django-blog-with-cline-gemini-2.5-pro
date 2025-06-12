# Progress: Django TDD 블로그

## 1. 현재 상태 (Current Status)

- **진행률** 
  - v1.0: 100% 완료
  - v1.1: 100% 완료
  - v1.2: 100% 완료

- **현재 단계**: 사용자 인증 시스템 구현 착수 예정

## 2. 완료된 작업 (What Works)

- **v1.0**: 기본 블로그 기능 (게시글 CRUD, 댓글, 태그, 검색)
- **v1.1**: `Post` 모델에 `author` 필드 추가 및 2단계 마이그레이션을 통한 `makemigrations` 문제 해결
- **v1.2**: 계층형 카테고리 기능 (모델, 뷰, 템플릿, 테스트 포함)

## 3. 남은 작업 (What's Left to Build)

- **1. 템플릿 시스템 리팩토링 (Template System Refactoring)**
  - [x] TDD: `blog` 앱의 모든 주요 템플릿이 `base.html`을 상속하도록 리팩토링
  - [x] TDD: 템플릿 상속 구조를 검증하는 테스트(`test_templates.py`) 추가
- **2. 사용자 인증 시스템 (User Authentication) - `users` 앱**
  - [x] `users` 앱 생성 및 `settings.py` 등록
  - [x] `users.urls` 생성 및 `config.urls`에 연동
  - [x] TDD: 로그인/로그아웃 기능 구현 (Django 내장 `LoginView`, `LogoutView` 활용)
  - [x] TDD: 회원가입 기능 구현 (Django 내장 `UserCreationForm` 활용)
  - [x] `login.html`, `signup.html` 템플릿 작성
  - [x] 네비게이션 바에 로그인/로그아웃/회원가입 링크 추가
  - [x] TDD: `blog` 앱의 게시글 작성/수정/삭제 기능에 로그인 권한 적용
  - [x] TDD: 본인 게시글만 수정/삭제할 수 있도록 권한 검증 로직 추가
- **3. 계층형 카테고리 (Hierarchical Category)**
  - [x] `Category` 모델 정의 (self-referencing FK)
  - [x] `Post` 모델에 `category` FK 추가
  - [x] 카테고리 모델/관계 테스트 코드 작성 (TDD) - (Red-Green 사이클 완료)
  - [x] 카테고리별 포스트 목록 뷰/템플릿 구현
- **4. 댓글 시스템 개선 (Nested Comments)**
  - [x] `Comment` 모델 수정 (`author` FK, `parent` self-referencing FK, updated_at 필드 추가)
  - [x] 댓글 모델 테스트 코드 작성 (TDD)
  - [x] 댓글 생성/수정/삭제 로직 및 뷰/템플릿 업데이트 (인증/권한 적용)
- **5. 조회수 카운터 (View Count)**
  - [x] `Post` 모델에 `view_count` 필드 추가
  - [x] 중복 방지 로직을 포함한 조회수 증가 메서드 모델에 구현
  - [x] 조회수 기능 테스트 코드 작성 (TDD)
  - [x] 상세 페이지 뷰에 조회수 증가 로직 적용
- **6. 좋아요/싫어요 기능 (Like/Dislike System)**
  - [x] `Vote` 모델 정의 (`User` FK, `Post` FK, `value` field)
  - [x] `Post` 모델에 `votes` 관계 추가
  - [x] `Vote` 모델 테스트 코드 작성 (TDD)
  - [x] 좋아요/싫어요 처리 뷰/로직 구현 (AJAX)
  - [x] 좋아요/싫어요 카운트를 별도로 처리하기
- **7. 테스트 구조 리팩토링 (Test Structure Refactoring)**
  - [x] **계획 수립 및 문서화 (Planning & Documentation)**
    - [x] `activeContext.md`에 리팩토링 계획 반영
    - [x] `.clinerules/testing.md`에 파일 분리 예시 추가
    - [x] `.clinerules/workflow.md`에 선행 리팩토링 원칙 추가
    - [x] `progress.md`에 상세 리팩토링 계획 반영
  - [x] **`test_models.py` 분리 (Separate `test_models.py`)**
    - [x] `test_category_model.py` 생성 및 관련 테스트 이동
    - [x] `test_tag_model.py` 생성 및 관련 테스트 이동
    - [x] `test_post_model.py` 생성 및 관련 테스트 이동
    - [x] `test_comment_model.py` 생성 및 관련 테스트 이동
    - [x] `test_vote_model.py` 생성 및 관련 테스트 이동
    - [x] 기존 `test_models.py` 파일 삭제
  - [x] **`test_views.py` 분리 (Separate `test_views.py`)**
    - [x] `test_search_views.py` 생성 및 관련 테스트 이동
    - [x] `test_tag_views.py` 생성 및 관련 테스트 이동
    - [x] `test_category_views.py` 생성 및 관련 테스트 이동
    - [x] `test_post_views.py`는 Post CRUD 관련 테스트만 남도록 정리
  - [x] **`tests/__init__.py` 업데이트 (Update `tests/__init__.py`)**
    - [x] 분리된 모든 테스트 파일이 인식되도록 임포트 구문 수정
- **8. RSS 피드 기능 (RSS Feed)**
  - [x] RSS 피드 테스트 코드 작성 (TDD)
  - [x] Django의 `syndication` 프레임워크를 활용한 RSS 피드 클래스 구현
  - [x] 최신 게시글 RSS 피드 생성 (`/feed/`)
  - [x] RSS 피드 링크를 템플릿에 추가 (HTML `<link>` 태그)
  - [ ] 카테고리별 RSS 피드 지원 (`/rss/category/<category>/`)
  - [ ] RSS 피드 메타데이터 최적화 (제목, 설명, 게시일, 작성자 등)
- **8. 페이징 기능 (Pagination)**
  - [x] ListView 기반 뷰에 Django 기본 페이징 기능 적용 (Paginator, page_obj)
  - [x] 템플릿에 페이지 네비게이션 UI 추가 (has_previous, has_next, page_obj.paginator.page_range)
  - [x] 페이지 번호 쿼리스트링(?page=2)을 고려한 테스트 케이스 작성 (TDD)
  - [x] 태그별, 카테고리별, 검색결과 페이지에도 페이징 적용
  - [x] UX 향상을 위한 페이지 번호 하이라이트 및 비활성화 처리
  - [x] 페이지당 게시글 수 설정 (기본값: 10개, 설정값으로 조정 가능하게)
  - [x] 검색 결과와 페이징 동시 적용 시 쿼리스트링 보존 로직 추가 (?page=2&query=foo)
  - [x] 페이징 관련 테스트 코드 작성: 페이지 경계 테스트(첫 페이지, 마지막 페이지 등), 존재하지 않는 페이지 접근 시 graceful fallback
- **9. 캡차 기능 (CAPTCHA)**
  - [x] **환경 설정 (Environment Setup)**
    - [x] `django-simple-captcha` 패키지 설치 및 `requirements.txt` 업데이트
    - [x] `settings.py`에 `captcha` 앱 등록 및 `urls.py`에 연동
  - [x] **TDD: 회원가입 폼 적용**
    - [x] 회원가입 폼에 CAPTCHA 필드 적용
  - **[DONE] CAPTCHA 구현 리팩토링 및 안정화**
    - [x] **테스트 구조 복원**: `users/tests.py`를 `users/tests/` 패키지 구조로 복원
    - [x] **건너뛴 테스트 해결**: `@unittest.skip` 처리된 `test_signup_creates_new_user` 테스트 해결
    - [x] **코드 일관성 점검**: CAPTCHA 관련 코드 전반의 일관성 점검 및 리팩토링
  - **[TODO] TDD: 로그인/댓글 폼 적용**
    - [x] TDD: 로그인 폼에 CAPTCHA 필드 적용
    - [x] TDD: 댓글 작성 폼에 CAPTCHA 필드 적용
    - [ ] API 키는 .env 파일에 분리하여 관리
    - [ ] 유효성 검사는 clean() 또는 form_valid() 메서드에서 처리
    - [ ] 실패 시 표준 Django 폼 에러 메시지 표시
    - [ ] 관리자(admin) 페이지에는 reCAPTCHA 제외 (편의성 고려)
    - [ ] 기본 단위 테스트 및 폼 유효성 테스트 추가 (TDD 기반)
    - [ ] UX 고려: 로딩 최적화 및 접근성(A11Y) 기본 확보
- **10. REST API 기능**
  - [ ] Django REST Framework (DRF) 활용
  - [ ] 인증 시스템: Token 또는 JWT 인증
  - [ ] 주요 API 엔드포인트: 게시글, 댓글, 카테고리, 태그 등
  - [ ] 고급 기능: 검색, 필터링, 정렬, 페이징
  - [ ] 문서화: Swagger/OpenAPI 자동 문서 생성

## 4. 알려진 이슈 (Known Issues)

### 현재 알려진 이슈 (Current Issues)
 - **[리팩토링 계획 완료]** `test_views.py` 파일이 너무 커서 수정하기 어려움. (다음 Task에서 분리 작업 예정)

### 과거에 해결된 이슈 (Resolved Issues)
 - **좋아요/싫어요 카운트 분리**: `Vote` 모델의 `value` 필드 하나로 집계되던 것을 `like_count`와 `dislike_count`로 분리하여 명확하게 표시하도록 개선했습니다.
 - **로그인/로그아웃 오류**: 로그인 시 `Page not found` 오류 및 로그아웃 시 `HTTP 405` 오류를 해결했습니다. (`settings.py`에 `LOGIN_REDIRECT_URL` 추가 및 `base.html`의 로그아웃 링크를 POST 방식으로 수정)
 - **`makemigrations` 실패**: Non-nullable 필드(`author`) 추가 시 `makemigrations`가 실패했으나, 2단계 마이그레이션 전략을 도입하여 해결했습니다. (관련 커밋: `6fecd16b`, `2599705c`)
 - **간헐적으로 실패하는 테스트**: `SearchView`의 비결정적 결과 순서로 인해 테스트가 간헐적으로 실패했으나, `order_by()`를 추가하고 테스트 방식을 개선하여 해결했습니다. (관련 커밋: `ca14c3e0`)
 - **템플릿 상속 구조 부재**: 초기 템플릿에 `base.html` 상속이 누락되어 UI 일관성이 부족했으나, 템플릿 리팩토링을 통해 해결했습니다. (관련 커밋: `9b375d9`, `19a7774`)
 - **태그 저장 로직 오류**: `PostForm`에서 태그를 저장하는 로직의 버그를 수정했습니다. (관련 커밋: `44159978`)
 - **네비게이션 링크 누락**: 일부 템플릿에 네비게이션 링크가 누락되었던 문제를 해결했습니다. (관련 커밋: `c9588974`)

## 5. 추가 고려사항 (Additional Considerations)

- **보안**: 로그인 후 리다이렉트 처리, CSRF 토큰 적용
- **UX**: 로그인이 필요한 페이지 접근 시 적절한 메시지 표시
- **테스팅**: 인증이 필요한 모든 기능에 대한 권한 테스트 케이스 추가
- **SEO**: RSS 피드를 통한 검색 엔진 최적화 및 콘텐츠 배포
- **캐싱**: RSS 피드 성능 최적화를 위한 캐싱 전략 고려
