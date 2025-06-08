# Progress: Django TDD 블로그

## 1. 현재 상태 (Current Status)

- **진행률**: 100% (v1.0 완료)
- **현재 단계**: 신규 기능 개발 계획 수립

## 2. 완료된 작업 (What Works)

- **v1.0**: 기본 블로그 기능 (게시글 CRUD, 댓글, 태그, 검색)

## 3. 남은 작업 (What's Left to Build)

- **1. `makemigrations` 문제 해결**: `Post` 모델에 `author` 필드 추가 시 발생하는 마이그레이션 문제를 해결해야 합니다.
- **2. 계층형 카테고리 (Hierarchical Category)**
  - [ ] `Category` 모델 정의 (self-referencing FK)
  - [ ] `Post` 모델에 `category` FK 추가
  - [ ] 카테고리 모델/관계 테스트 코드 작성 (TDD)
  - [ ] 카테고리별 포스트 목록 뷰/템플릿 구현
- **3. 댓글 시스템 개선 (Nested Comments)**
  - [ ] `Comment` 모델 수정 (`author` FK, `parent` self-referencing FK)
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

## 4. 알려진 이슈 (Known Issues)

- **`makemigrations` 실패**: 신규 기능 구현을 위해 `Post` 모델에 `author`와 같은 non-nullable 필드를 추가할 때, 기존 데이터에 대한 기본값 설정 문제로 마이그레이션 파일 생성이 실패합니다. 다음 작업 시 이 문제를 우선적으로 해결해야 합니다.
