# 회고: 사용자 프로필 모델 구현 (Phase 1)

## 1. 작업 개요

- **목표**: '사용자 프로필' 기능의 기반이 되는 `Profile` 모델을 정의하고, `User` 생성 시 `Profile`이 자동으로 생성되도록 Signal을 구현한다.
- **기간**: 2025-06-19
- **주요 작업**:
    - `Profile` 모델 정의 및 테스트 코드 작성 (TDD)
    - `users` 앱의 모델 구조 리팩토링 (`models.py` -> `models/` 패키지)
    - `AUTH_USER_MODEL` 설정 및 관련 문제 해결
    - `UserCreationForm` 커스터마이징
    - `post_save` Signal을 이용한 `Profile` 자동 생성 기능 구현 (TDD)

## 2. 문제 해결 과정 (Troubleshooting)

`Profile` 모델을 추가하고 커스텀 `User` 모델을 본격적으로 사용하는 과정에서 여러 설정 관련 문제가 발생했다. 각 문제의 원인과 해결 과정을 TDD 사이클에 따라 기록한다.

### 문제 1: `ModuleNotFoundError: No module named 'users.models.profile'`

- **상황 (Red)**: `test_profile_model.py`에서 `from users.models.profile import Profile` 구문이 실패했다.
- **원인 분석**: `users/models.py`가 파일로 존재하고 있었기 때문에, `users/models`는 파이썬 패키지로 인식되지 않았다. 따라서 하위 모듈인 `profile`을 임포트할 수 없었다.
- **해결 (Green)**: `.clinerules/codingStyle.md`의 **모델 분리(Model Separation)** 원칙에 따라 `users/models`를 패키지 구조로 리팩토링했다.
    1.  `users/models/user.py` 파일을 생성하여 기존 `User` 모델 코드를 이전했다.
    2.  `users/models/profile.py`에 `Profile` 모델을 정의했다.
    3.  `users/models/__init__.py`를 생성하여 `User`와 `Profile` 모델을 임포트했다.
    4.  불필요해진 `users/models.py` 파일을 삭제했다.

### 문제 2: `SystemCheckError: Reverse accessor for '...' clashes`

- **상황 (Red)**: 테스트 실행 시, `auth.User`와 `users.User`의 `related_name`이 충돌하는 시스템 체크 오류가 발생했다.
- **원인 분석**: 커스텀 User 모델(`users.User`)을 정의했지만, `settings.py`에 `AUTH_USER_MODEL` 설정을 명시하지 않아 Django가 기본 `auth.User`와 커스텀 `users.User`를 모두 인식하면서 충돌이 발생했다.
- **해결 (Green)**: `config/settings.py` 파일에 `AUTH_USER_MODEL = 'users.User'` 설정을 명시적으로 추가하여 Django가 커스텀 User 모델을 기본 인증 모델로 사용하도록 지정했다.

### 문제 3: `ValueError: Dependency on app with no migrations: users`

- **상황 (Red)**: `AUTH_USER_MODEL` 설정 후 테스트 실행 시, `users` 앱에 마이그레이션 파일이 없다는 오류가 발생했다.
- **원인 분석**: `AUTH_USER_MODEL`을 설정하면 Django는 해당 앱의 마이그레이션 기록을 추적해야 한다. 하지만 `users` 앱에는 `migrations` 디렉토리만 있고 실제 마이그레이션 파일(`0001_initial.py`)이 없어 의존성 해결에 실패했다.
- **해결 (Green)**: `python manage.py makemigrations users` 명령을 실행하여 `User`와 `Profile` 모델에 대한 초기 마이그레이션 파일을 생성했다.

### 문제 4: `AttributeError: Manager isn't available; 'auth.User' has been swapped for 'users.User'`

- **상황 (Red)**: `SignupForm`을 사용하는 테스트(`test_auth_views.py`, `test_user_forms.py`)에서 오류가 발생했다.
- **원인 분석**: Django의 내장 `UserCreationForm`은 기본적으로 `auth.User` 모델을 사용하도록 설계되어 있다. `AUTH_USER_MODEL`을 `users.User`로 변경했으므로, `UserCreationForm`을 상속받는 `SignupForm`이 더 이상 올바르게 동작하지 않았다.
- **해결 (Green)**: `users/forms/auth_forms.py`의 `SignupForm`을 수정하여 커스텀 User 모델을 사용하도록 명시했다.
    ```python
    from users.models import User

    class SignupForm(UserCreationForm):
        class Meta(UserCreationForm.Meta):
            model = User
            fields = ('username', 'email')
        
        captcha = CaptchaField()
    ```

## 3. 최종 결과 및 교훈

- **결과**: 위 문제들을 순차적으로 해결한 후, `Profile` 모델과 Signal 기능이 모두 TDD 사이클에 따라 성공적으로 구현되었다. 모든 테스트가 통과하는 안정적인 상태(`Green`)에서 작업을 마무리했다.
- **교훈**:
    - Django의 `AUTH_USER_MODEL` 커스터마이징은 프로젝트 초기에 수행하는 것이 가장 이상적이다. 프로젝트 중간에 변경할 경우, 모델, 폼, 마이그레이션 등 여러 부분에 걸쳐 연쇄적인 수정이 필요하다.
    - TDD 접근 방식은 복잡한 설정 변경 과정에서 발생하는 오류를 각 단계에서 명확하게 식별하고 해결하는 데 매우 유용했다. 각 오류(Red)는 다음 해결 단계(Green)를 명확히 제시해주었다.
    - `.clinerules`에 정의된 코딩 스타일(모델 분리)과 워크플로우 원칙을 따르는 것이 장기적으로 코드의 일관성과 안정성을 유지하는 데 중요하다는 것을 다시 한번 확인했다.
