# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **REST API 리팩토링 계획 반영 및 실행 (Reflecting and Executing REST API Refactoring Plan)**
- 기존에 구현된 토큰 인증 시스템을 회고하고, 코드의 유지보수성, 확장성, 일관성을 높이기 위한 리팩토링을 준비합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **리팩토링 계획 수립 완료**:
    - 기존 API 인증 시스템의 코드(`views`, `serializers`, `tests`, `urls`)를 검토했습니다.
    - `.clinerules` 및 모범 사례를 기반으로 권한 체계, URL 구조, 테스트 코드, Serializer 구조 개선을 위한 4단계 리팩토링 계획을 수립했습니다.
    - 사용자와 계획에 대한 합의를 완료했습니다.

## 3. 다음 단계 (Next Steps)

- 수립된 리팩토링 계획을 `progress.md`에 반영하고, 순서대로 실행합니다.
- **주요 목표**:
    1.  **Phase 1: 권한 체계 강화 (Permission System Enhancement)**
        - TDD: `IsOwnerOrReadOnly` 커스텀 권한 클래스를 구현하여 자신의 객체만 수정/삭제할 수 있도록 보장합니다.
    2.  **Phase 2: URL 구조 개선 (URL Structure Refinement)**
        - API 관련 URL을 `users/urls/api_urls.py` 등으로 분리하여 책임과 역할을 명확히 합니다.
    3.  **Phase 3: 테스트 코드 리팩토링 (Test Code Refactoring)**
        - 테스트 내 중복된 인증 로직을 `authenticate()` 헬퍼 메서드로 추상화하여 가독성과 재사용성을 높입니다.
    4.  **Phase 4: Serializer 구조화 (Serializer Structuring)**
        - `UserSerializer`를 도입하여 `PostSerializer`와의 관계를 재정의하고, 응답 데이터 구조의 유연성을 확보합니다.
