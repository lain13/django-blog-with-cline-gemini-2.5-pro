# Workflow Rules

## 1. 개발 프로세스 (Development Process)

- **TDD (Test-Driven Development)**: 모든 기능은 다음의 Red-Green-Refactor 사이클을 엄격히 따른다.
    1.  **Red**: 실패하는 테스트를 먼저 작성한다. (`*test*.py`)
    2.  **Green**: 테스트를 통과하는 최소한의 코드를 작성한다.
    3.  **Refactor**: 중복을 제거하고 코드 구조를 개선한다.

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
