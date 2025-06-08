# Progress: Django TDD 블로그

## 1. 현재 상태 (Current Status)

- **진행률** 
  - v1.0: 100% 완료
  - v1.1: 50% 완료

- **현재 단계**: 신규 기능 개발 계획 수립

## 2. 완료된 작업 (What Works)

- **v1.0**: 기본 블로그 기능 (게시글 CRUD, 댓글, 태그, 검색)
- **v1.1**: `Post` 모델에 `author` 필드 추가 및 2단계 마이그레이션을 통한 `makemigrations` 문제 해결

## 3. 남은 작업 (What's Left to Build)

- **1. 계층형 카테고리 (Hierarchical Category)**
  - [ ] `Category` 모델 정의 (self-referencing FK)
  - [ ] `Post` 모델에 `category` FK 추가
  - [ ] 카테고리 모델/관계 테스트 코드 작성 (TDD)
  - [ ] 카테고리별 포스트 목록 뷰/템플릿 구현
- **2. 댓글 시스템 개선 (Nested Comments)**
  - [ ] `Comment` 모델 수정 (`author` FK, `parent` self-referencing FK, updated_at 필드 추가)
  - [ ] 댓글 모델 테스트 코드 작성 (TDD)
  - [ ] 댓글 생성/수정/삭제 로직 및 뷰/템플릿 업데이트
- **3. 조회수 카운터 (View Count)**
  - [ ] `Post` 모델에 `view_count` 필드 추가
  - [ ] 중복 방지 로직을 포함한 조회수 증가 메서드 모델에 구현
  - [ ] 조회수 기능 테스트 코드 작성 (TDD)
  - [ ] 상세 페이지 뷰에 조회수 증가 로직 적용
- **4. 좋아요/싫어요 기능 (Like/Dislike System)**
  - [ ] `Vote` 모델 정의 (`User` FK, `Post` FK, `value` field)
  - [ ] `Post` 모델에 `votes` 관계 추가
  - [ ] `Vote` 모델 테스트 코드 작성 (TDD)
  - [ ] 좋아요/싫어요 처리 뷰/로직 구현 (AJAX)

## 4. 알려진 이슈 (Known Issues)

- (해결됨) `makemigrations` 실패
