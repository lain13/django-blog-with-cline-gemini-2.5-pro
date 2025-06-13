# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **`users` 앱 폼 구조 리팩토링 실행**
- `.clinerules/codingStyle.md`에 정의된 '폼 분리' 원칙에 따라 `users/forms.py` 파일의 구조를 개선하는 작업을 진행합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **리팩토링 계획 수립**: `users/forms.py`를 `users/forms/` 디렉토리 구조로 변경하고, 인증 관련 폼(`LoginForm`, `SignupForm`)을 `auth_forms.py`로 분리하는 구체적인 계획을 수립했습니다.
- **`progress.md` 업데이트**: 수립된 리팩토링 계획을 `progress.md`의 '리팩토링' 섹션에 상세 작업으로 추가했습니다.

## 3. 다음 단계 (Next Steps)

- **1. `users` 앱 폼 리팩토링 실행**:
    - **1-1. 구조 생성**: `users/forms/` 디렉토리 및 `auth_forms.py`, `__init__.py` 파일을 생성합니다.
    - **1-2. 코드 이동**: `LoginForm`과 `SignupForm`을 `auth_forms.py`로 이동시킵니다.
    - **1-3. 의존성 수정**: `users/views/auth_views.py`와 `users/tests/test_user_forms.py`의 임포트 경로를 수정합니다.
    - **1-4. 기존 파일 삭제**: 리팩토링 완료 후 기존 `users/forms.py` 파일을 삭제합니다.
- **2. 다음 리팩토링 대상 검토**: `users` 앱 폼 리팩토링 완료 후, `progress.md`에 명시된 다음 리팩토링 작업을 진행합니다.
