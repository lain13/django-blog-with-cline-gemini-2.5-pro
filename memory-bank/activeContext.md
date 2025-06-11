# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **테스트 코드 리팩토링 계획 수립 및 문서화**
- `blog/tests/test_post_views.py`와 `blog/tests/test_models.py` 파일의 복잡도를 낮추기 위한 리팩토링 계획을 수립하고, 관련 규칙과 진행 상황을 문서에 반영합니다. 실제 코드 리팩토링은 다음 Task에서 진행합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **작업 방향 전환**: 기존 'RSS 피드 기능 구현'에서 '테스트 코드 리팩토링 계획 수립'으로 작업 우선순위를 변경했습니다.

## 3. 다음 단계 (Next Steps)

- **1. `.clinerules` 업데이트**
  - `testing.md`: 테스트 파일 분리 규칙에 구체적인 예시를 추가하여 명확성을 강화합니다.
  - `workflow.md`: '선행 리팩토링 원칙'을 추가하여, 기능 구현 전 코드 구조 개선의 중요성을 명시합니다.

- **2. `progress.md` 업데이트**
  - '테스트 구조 리팩토링' 작업 항목을 이번에 수립한 상세 계획으로 구체화하고, 현재 진행 상태를 반영합니다.

- **3. 다음 Task 준비**
  - 문서화가 완료되면, 다음 Task에서 아래의 리팩토링을 실행할 준비를 합니다.
    - **`test_post_views.py` 분리**: `test_search_views.py`, `test_tag_views.py`, `test_category_views.py` 파일 생성
    - **`test_models.py` 분리**: `test_post_model.py`, `test_comment_model.py`, `test_tag_model.py`, `test_category_model.py`, `test_vote_model.py` 파일 생성 및 기존 파일 삭제
    - **`tests/__init__.py` 업데이트**: 분리된 테스트 모듈 임포트
