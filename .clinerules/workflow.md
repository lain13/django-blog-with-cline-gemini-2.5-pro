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

- **선행 리팩토링 원칙 (Principle of Upfront Refactoring)**: 새로운 기능이 기존 코드의 구조적 변경을 요구할 경우, 기능 구현에 앞서 구조를 개선하는 리팩토링 작업을 먼저 식별하고 실행하는 것을 우선으로 한다.

- **선행 기술 검증 원칙 (Principle of Upfront Technical Validation)**: 새로운 외부 라이브러리나 기술을 도입하기 전, 본 프로젝트에 통합하기에 앞서 독립적인 최소 기능 테스트(PoC, Proof of Concept)를 통해 해당 기술의 동작 방식, 설정, 테스트 전략을 검증하는 것을 원칙으로 한다.

- **TDD 예외 처리 가이드 (TDD Exception Handling Guide)**: 테스트 실패(Red)의 원인이 코드 로직이 아닌 외부 환경, 라이브러리 설정, 인프라 문제로 판단될 경우, TDD 사이클을 잠시 중단하고 원인 분석 및 해결을 우선시한다. 문제 해결 과정을 문서화하고, 필요시 `@unittest.skip`과 함께 명확한 사유를 명시한다.

- **작업 완료의 정의 (Definition of Done)**: 모든 작업은 아래의 '작업 완료 검증 체크리스트'를 통과해야만 '완료'로 간주한다.
    1.  **기능 요구사항 충족 (Functional Requirements Met)**: 작업의 핵심 기능이 TDD에 따라 구현되고 모든 관련 테스트가 통과했는가?
    2.  **시스템 일관성 확인 (System Consistency Check)**: 변경 사항이 영향을 미치는 모든 부분에서 시스템이 일관성을 유지하는가? (예: `base.html` 수정 시, 이를 상속하는 **모든** 페이지에서 올바르게 보이는가?)
    3.  **문서 최신화 (Documentation Updated)**: `progress.md`, `activeContext.md` 등 관련 문서가 모두 최신 상태로 업데이트되었는가?
    4.  **최종 검증 (Final Verification)**: 개발 서버를 실행하는 등, 최종 사용자 관점에서 변경 사항이 의도대로 작동하는지 확인했는가?

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

## 5. 협업 및 도움 요청 (Collaboration and Asking for Help)

- **교착 상태 정의 (Defining a Stuck State)**: 동일한 근본 원인으로 추정되는 문제에 대해 2회 이상 연속으로 해결에 실패할 경우, 이는 '교착 상태(Stuck State)'로 간주한다.
- **프로토콜 (Protocol)**:
    1.  **상태 보고 (Report Status)**: `ask_followup_question` 도구를 사용하여 현재까지 시도한 방법, 실패 로그, 그리고 문제의 근본 원인에 대한 추론을 사용자에게 명확히 보고한다.
    2.  **도움 요청 (Ask for Guidance)**: "이 문제에 대한 다른 접근 방식이나 조언이 있으신가요?" 와 같이 명확한 질문을 통해 사용자의 경험과 지식을 구한다.
- **목표 (Goal)**: 이 규칙은 비효율적인 시도를 방지하고, 개발자의 통찰력을 활용하여 문제를 더 빠르게 해결하는 것을 목표로 한다.
