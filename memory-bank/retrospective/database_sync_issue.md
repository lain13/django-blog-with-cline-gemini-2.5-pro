# 회고: 데이터베이스 동기화 오류 해결

## 1. 문제 상황

- **오류**: `python manage.py runserver` 실행 후, 홈페이지 접근 시 `OperationalError at / no such table: users_user` 발생.
- **원인 분석**:
    1.  `users` 앱에 커스텀 User 모델을 도입하고 `0001_initial` 마이그레이션을 생성했음.
    2.  테스트 환경에서는 매번 새 DB를 생성하므로 문제가 없었으나, 실제 개발 DB(`db.sqlite3`)에는 해당 마이그레이션이 적용되지 않았음.
    3.  `migrate` 명령 실행 시 `No migrations to apply`가 표시되는 것으로 보아, `django_migrations` 테이블에는 마이그레이션이 적용된 것으로 기록되어 있으나 실제 테이블은 생성되지 않은, DB와 마이그레이션 기록 간의 불일치 상태로 추정됨.

## 2. 해결 과정

- **1차 시도**: `migrate users zero --fake` 후 `migrate` 재시도.
    - **결과**: `table "users_profile" already exists` 라는 새로운 오류 발생. `0001_initial` 마이그레이션이 `users_user`와 `users_profile`을 모두 생성하는데, DB에는 `users_user`는 없고 `users_profile`만 있는 기형적인 상태였음.

- **2차 시도 (최종 해결)**: 데이터베이스 재생성
    1.  `rm db.sqlite3`: 기존의 불일치 상태에 있는 데이터베이스 파일을 완전히 삭제.
    2.  `python manage.py migrate`: 모든 앱의 마이그레이션을 처음부터 순서대로 적용하여 깨끗하고 일관된 상태의 새 데이터베이스를 생성.

## 3. 교훈

-   **개발 환경 DB의 중요성**: 테스트 통과와 별개로, 실제 개발용 데이터베이스의 상태도 주기적으로 확인하고 마이그레이션을 적용하는 것이 중요하다.
-   **DB-마이그레이션 불일치**: `no such table` 오류와 `No migrations to apply`가 동시에 발생할 경우, DB와 마이그레이션 기록 간의 불일치를 의심해야 한다.
-   **가장 확실한 해결책**: 복잡한 마이그레이션 꼬임 문제가 발생했을 때, 개발 환경에서는 데이터를 보존할 필요가 없다면 DB 파일을 삭제하고 처음부터 다시 마이그레이션하는 것이 가장 빠르고 확실한 해결책이다.
