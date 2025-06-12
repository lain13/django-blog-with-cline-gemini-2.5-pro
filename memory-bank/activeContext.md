# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **TDD: RSS 피드 기능 개선**
- 로그인 및 댓글 폼에 CAPTCHA 적용이 완료되었습니다. 이제 `progress.md`에 따라 다음 작업인 RSS 피드 기능 개선을 시작합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **TDD: 로그인 및 댓글 폼에 CAPTCHA 적용 완료**:
    - **로그인 폼**: `LoginForm` 생성, `CaptchaField` 추가, 관련 뷰/URL/템플릿 수정 및 테스트 통과 완료.
    - **댓글 폼**: `CommentForm`에 `CaptchaField` 추가, 관련 템플릿 수정 및 테스트 통과 완료.
    - `progress.md`에 모든 관련 작업 완료를 기록했습니다.

## 3. 다음 단계 (Next Steps)

- `progress.md`의 "RSS 피드 기능" 계획에 따라 다음 Task를 진행합니다.
- **주요 목표**:
    1.  TDD 사이클에 따라, 카테고리별 RSS 피드 기능을 구현합니다. (`/rss/category/<category>/`)
    2.  TDD 사이클에 따라, RSS 피드의 메타데이터(제목, 설명 등)를 최적화합니다.
    3.  관련 기능이 모두 정상적으로 동작하는지 최종 확인합니다.
