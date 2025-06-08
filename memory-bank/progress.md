# Progress: Django TDD 블로그

## 1. 현재 상태 (Current Status)

- **진행률** 
  - v1.0: 100% 완료
  - v1.1: 50% 완료

- **현재 단계**: 사용자 인증 시스템 구현 착수 예정

## 2. 완료된 작업 (What Works)

- **v1.0**: 기본 블로그 기능 (게시글 CRUD, 댓글, 태그, 검색)
- **v1.1**: `Post` 모델에 `author` 필드 추가 및 2단계 마이그레이션을 통한 `makemigrations` 문제 해결
- **v1.2**: 계층형 카테고리 기능 (모델, 뷰, 템플릿, 테스트 포함)

## 3. 남은 작업 (What's Left to Build)

- **1. 사용자 인증 시스템 (User Authentication) - `users` 앱**
  - [x] `users` 앱 생성 및 `settings.py` 등록
  - [x] `users.urls` 생성 및 `config.urls`에 연동
  - [x] TDD: 로그인/로그아웃 기능 구현 (Django 내장 `LoginView`, `LogoutView` 활용)
  - [x] TDD: 회원가입 기능 구현 (Django 내장 `UserCreationForm` 활용)
  - [x] `login.html`, `signup.html` 템플릿 작성
  - [ ] 네비게이션 바에 로그인/로그아웃/회원가입 링크 추가
  - [ ] TDD: `blog` 앱의 게시글 작성/수정/삭제 기능에 로그인 권한 적용
  - [ ] TDD: 본인 게시글만 수정/삭제할 수 있도록 권한 검증 로직 추가
- **2. 계층형 카테고리 (Hierarchical Category)**
  - [x] `Category` 모델 정의 (self-referencing FK)
  - [x] `Post` 모델에 `category` FK 추가
  - [x] 카테고리 모델/관계 테스트 코드 작성 (TDD) - (Red-Green 사이클 완료)
  - [x] 카테고리별 포스트 목록 뷰/템플릿 구현
- **3. 댓글 시스템 개선 (Nested Comments)**
  - [ ] `Comment` 모델 수정 (`author` FK, `parent` self-referencing FK, updated_at 필드 추가)
  - [ ] 댓글 모델 테스트 코드 작성 (TDD)
  - [ ] 댓글 생성/수정/삭제 로직 및 뷰/템플릿 업데이트
- **4. 조회수 카운터 (View Count)**
  - [ ] `Post` 모델에 `view_count` 필드 추가
  - [ ] 중복 방지 로직을 포함한 조회수 증가 메서드 모델에 구현
  - [ ] 조회수 기능 테스트 코드 작성 (TDD)
  - [ ] 상세 페이지 뷰에 조회수 증가 로직 적용
- **5. 좋아요/싫어요 기능 (Like/Dislike System)**
  - [ ] `Vote` 모델 정의 (`User` FK, `Post` FK, `value` field)
  - [ ] `Post` 모델에 `votes` 관계 추가
  - [ ] `Vote` 모델 테스트 코드 작성 (TDD)
  - [ ] 좋아요/싫어요 처리 뷰/로직 구현 (AJAX)
- **6. RSS 피드 기능 (RSS Feed)**
  - [ ] Django의 `syndication` 프레임워크를 활용한 RSS 피드 클래스 구현
  - [ ] 최신 게시글 RSS 피드 생성 (`/rss/` 또는 `/feed/`)
  - [ ] 카테고리별 RSS 피드 지원 (`/rss/category/<category>/`)
  - [ ] RSS 피드 테스트 코드 작성 (TDD)
  - [ ] RSS 피드 링크를 템플릿에 추가 (HTML `<link>` 태그)
  - [ ] RSS 피드 메타데이터 최적화 (제목, 설명, 게시일, 작성자 등)

## 4. 알려진 이슈 (Known Issues)

- (해결됨) `makemigrations` 실패

## 5. 추가 고려사항 (Additional Considerations)

- **보안**: 로그인 후 리다이렉트 처리, CSRF 토큰 적용
- **UX**: 로그인이 필요한 페이지 접근 시 적절한 메시지 표시
- **테스팅**: 인증이 필요한 모든 기능에 대한 권한 테스트 케이스 추가
- **SEO**: RSS 피드를 통한 검색 엔진 최적화 및 콘텐츠 배포
- **캐싱**: RSS 피드 성능 최적화를 위한 캐싱 전략 고려
