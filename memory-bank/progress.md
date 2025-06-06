# Progress: Django TDD 블로그

## 1. 현재 상태 (Current Status)

- **진행률**: 98%
- **현재 단계**: 9. 버그 수정 및 안정화 (Bug Fixing & Stabilization)

## 2. 완료된 작업 (What Works)

- **1. 프로젝트 초기 설정 (Project Initialization)**
- **2. Post 모델 개발 (TDD)**
- **3. 포스트 목록 페이지 개발 (TDD)**
- **4. 포스트 상세 페이지 개발 (TDD)**
- **5. 포스트 생성 기능 개발 (TDD)**
- **6. 포스트 수정 기능 개발 (TDD)**
- **7. 포스트 삭제 기능 개발 (TDD)**
- **8. 프로젝트 문서화 (Documentation)**

## 3. 남은 작업 (What's Left to Build)

- **Phase 1: Post 수정일 추가**:
    - `Post` 모델에 `modified_at` 필드 추가 및 마이그레이션
    - `modified_at` 자동 업데이트 기능 테스트
    - 템플릿에 수정일 표시
- **Phase 2: 댓글 기능 추가**:
    - `Comment` 모델 및 `CommentForm` 정의
    - 댓글 생성/조회 관련 View, URL, Template 구현
    - 댓글 기능 TDD 테스트
- **Phase 3: 검색 기능 추가**:
    - 제목/내용 기반 검색 View, URL, Template 구현
    - 검색 기능 TDD 테스트

## 4. 알려진 이슈 (Known Issues)

- 현재 알려진 이슈 없음.
