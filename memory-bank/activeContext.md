# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **사용자 인증 시스템 (로그인/로그아웃) 구현 완료 및 다음 단계 준비**
- TDD를 통해 `users` 앱에 로그인 및 로그아웃 기능을 성공적으로 구현했습니다. 이제 다음 작업인 회원가입 기능 구현을 준비합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **`feat(users)`**: `users` 앱 생성 및 `settings.py` 등록
- **`feat(users)`**: `users.urls` 생성 및 `config.urls`에 연동
- **`feat(users)`**: TDD를 통해 로그인/로그아웃 기능 구현 완료 (`LoginView`, `LogoutView` 활용)
- **`fix(tests)`**: 로그아웃 테스트 시 `GET` 대신 `POST`를 사용하도록 수정
- **`fix(settings)`**: `LOGOUT_REDIRECT_URL`을 설정하여 로그아웃 후 리다이렉트 문제 해결
- **`docs(memory-bank)`**: `progress.md`에 로그인/로그아웃 기능 완료 상태 반영

## 3. 다음 단계 (Next Steps)

- **TDD: 회원가입 기능 구현**
  - 다음 태스크에서 `progress.md`에 정의된 계획에 따라 회원가입 기능 개발을 시작합니다.
