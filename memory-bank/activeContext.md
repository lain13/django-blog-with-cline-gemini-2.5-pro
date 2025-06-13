# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **TDD: REST API - 주요 엔드포인트 구현**
- `Post` API에 토큰 기반 인증 시스템을 성공적으로 도입했습니다. 이제 `Comment`, `Category` 등 다른 핵심 모델에 대한 API 엔드포인트를 구현할 차례입니다.

## 2. 최근 변경 사항 (Recent Changes)

- **TDD: API 토큰 인증 시스템 구현 완료**:
    - `rest_framework.authtoken`을 사용하여 토큰 발급 엔드포인트(`/users/api/token/`)를 추가했습니다.
    - `PostListAPIView`에 `IsAuthenticatedOrReadOnly` 권한을 적용하여, 인증된 사용자만 게시글을 생성할 수 있도록 수정했습니다.
    - 관련 테스트 케이스를 작성하고 모두 통과시켰습니다.
    - `progress.md`에 관련 작업 완료를 기록했습니다.

## 3. 다음 단계 (Next Steps)

- `progress.md`의 "REST API 기능" 계획에 따라 다음 Task를 진행합니다.
- **주요 목표**:
    1.  **TDD: `Comment` 모델에 대한 API 구현**:
        - `Comment` 목록 및 상세 조회를 위한 Serializer와 View를 작성합니다.
        - 인증된 사용자만 댓글을 작성/수정/삭제할 수 있도록 권한을 설정하고 테스트합니다.
    2.  **TDD: `Category` 모델에 대한 API 구현**:
        - `Category` 목록 및 상세 조회를 위한 Serializer와 View를 작성합니다.
        - 일반적으로 카테고리는 읽기 전용이므로, `ReadOnlyModelViewSet` 사용을 고려합니다.
