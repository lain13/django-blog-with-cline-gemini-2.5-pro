# Workflow Rules

이 문서를 개발 프로세스의 일관성과 품질을 유지하기 위해 필요한 규칙들을 명기한다.

## 1. 개발 프로세스 (Development Process)

- **작업 계획 가이드**: `memory-bank`의 내용을 바탕으로 작업을 계획하기 전에는, `.clinerules` 디렉토리의 규칙들을 먼저 확인하고 숙지한다.

- **TDD (Test-Driven Development)**: 모든 기능은 다음의 Red-Green-Refactor 사이클을 엄격히 따른다.
    1.  **Red**: 실패하는 테스트를 먼저 작성한다. (`*test*.py`)
    2.  **Green**: 테스트를 통과하는 최소한의 코드를 작성한다.
    3.  **Refactor**: 중복을 제거하고 코드 구조를 개선한다.

- **작업 실행 원칙 (Execution Principles)**:
    1.  **최소 단위 작업 (Atomic Tasks)**: `progress.md`에 명시된 작업 항목(e.g., `Category` 모델 정의)을 가장 작은 논리적 단위로 분해하여 실행한다. (e.g., 필드 하나 추가, 메서드 하나 정의)
    2.  **순차적 진행 (Sequential Progress)**: 하나의 TDD 사이클(Red-Green-Refactor)이 완전히 종료된 후에 다음 사이클로 넘어간다.
    3.  **문서화 (Documentation)**: 하나의 주요 구성요소(e.g., 모델 전체, 뷰 전체) 개발이 완료될 때마다 `activeContext.md`와 `progress.md`를 업데이트하여 진행 상황을 명확히 기록한다.

## 2. 버전 관리 (Version Control)

- **Tool**: Git
- **Commit Message Convention**: Conventional Commits 명세를 따른다.
    - **Format**: `type(scope): subject`
    - **Types**:
        - `feat`: 새로운 기능 추가
        - `fix`: 버그 수정
        - `docs`: 문서 수정 (README, memory-bank, clinerules 등)
        - `style`: 코드 스타일 변경 (포매팅, 세미콜론 등)
        - `refactor`: 기능 변경 없는 코드 리팩토링
        - `test`: 테스트 코드 추가 또는 수정
        - `chore`: 빌드 프로세스, 패키지 매니저 설정 등 기타 변경사항
    - **Example**: `feat(blog): add Post model and initial test`

- **Commit 단위**: 논리적으로 독립된 최소 기능 단위로 커밋한다. (e.g., 모델 정의, 뷰 하나 구현 등)

## 3. 데이터베이스 마이그레이션 (Database Migrations)

- **모델 변경 후**: 데이터베이스 모델(`models.py`)이 변경되면, 반드시 마이그레이션 파일을 생성한다.
  - `python manage.py makemigrations <app_name>`
- **마이그레이션 적용**: 생성된 마이그레이션 파일을 데이터베이스에 적용한다.
  - `python manage.py migrate`
- **마이그레이션 파일 검토**: 생성된 마이그레이션 파일은 커밋하기 전에 내용을 검토한다.
- **Non-nullable 필드 추가 시 주의사항**: 기존 데이터가 있는 테이블에 `null=False`인 필드를 추가할 때는 반드시 기본값(`default`)을 설정하거나, `null=True`로 필드를 추가한 뒤 데이터 마이그레이션을 통해 기존 레코드의 값을 채우고, 이후 `null=False`로 변경하는 **2단계 마이그레이션(Two-Phase Migration)** 전략을 사용한다.

## 4. 테스트 구조 (Test Structure)
- 모든 테스트 코드 작성 및 실행은 `testing.md` 파일에 정의된 규칙을 따른다.
