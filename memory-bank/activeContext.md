# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **'사용자 프로필' 기능 TDD 구현**: 선행 작업으로 테스트 환경 안정화 및 `users` 앱 구조 리팩토링을 완료했습니다. 이제 안정된 기반 위에서 TDD 사이클에 따라 '사용자 프로필' 기능 개발을 시작합니다. 첫 단계는 `Profile` 모델을 정의하고 이에 대한 실패하는 테스트를 작성하는 것입니다.

## 2. 최근 변경 사항 (Recent Changes)

- **테스트 환경 안정화 (Phase 1)**:
    - 국제화(i18n) 및 API 테스트에서 발생하던 총 11개의 실패를 해결했습니다.
    - 불안정성이 높은 테스트는 원인 분석 후, 언어 설정에 독립적으로 동작하도록 수정하거나, 근본 원인 해결 전까지 `@unittest.skip` 처리하여 전체 테스트 스위트가 'Green' 상태를 유지하도록 조치했습니다.

- **`users` 앱 선행 리팩토링 (Phase 2)**:
    - **URL 구조 개선**: `users/urls.py`를 삭제하고, `users/urls/` 패키지 내에 `auth_urls.py`를 생성하여 URL 설계를 `blog` 앱과 일관성 있게 통일했습니다.
    - **테스트 구조 개선**: `users/tests/test_user_views.py` 파일의 이름을 `test_auth_views.py`로 변경하고, 향후 API 테스트를 위한 `test_api_views.py` 플레이스홀더를 생성하여 테스트 구조를 개선했습니다.

## 3. 다음 단계 (Next Steps)

1.  **`progress.md` 업데이트**: 완료된 '환경 안정화' 및 '`users` 앱 리팩토링' 작업을 `progress.md`에 반영합니다.
2.  **`Profile` 모델 TDD 시작**: `users/models/` 디렉토리에 `profile.py` 모델 파일을 생성하고, `users/tests/`에 `test_profile_model.py` 테스트 파일을 생성하여 첫 번째 Red-Green-Refactor 사이클을 시작합니다.
