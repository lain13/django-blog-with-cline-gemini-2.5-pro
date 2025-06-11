# Testing Rules

이 문서는 프로젝트의 테스트 코드 작성 및 관리에 대한 일관된 규칙을 정의하여, 코드의 안정성과 품질을 보장하는 것을 목표로 한다.

## 1. 테스트 구조 (Test Structure)

- **테스트 패키지**: 각 앱의 테스트는 `tests` 패키지 내에 작성한다. (e.g., `blog/tests/`)
- **파일 분리**: 테스트 코드는 기능(모델, 뷰, 폼 등)에 따라 별도의 파일로 분리하여 작성한다. `views`, `forms`, `urls`와 같이 기능/모델 단위로 세분화된 경우, 테스트 파일도 동일한 구조를 따라 분리한다.
    - **`test_models.py` 분리 예시**: 모델 클래스별로 테스트 파일을 분리한다.
        - `test_models.py` → `test_post_model.py`, `test_comment_model.py`, `test_category_model.py` 등
    - **`test_views.py` 분리 예시**: 뷰의 기능 단위(e.g., Post CRUD, 검색, 태그 필터링)별로 테스트 파일을 분리한다.
        - `test_views.py` → `test_post_views.py`, `test_search_views.py`, `test_tag_views.py` 등
    - **기타**: `test_forms.py` 등 다른 테스트 파일도 복잡해질 경우 동일한 원칙에 따라 분리한다.
- **테스트 실행**: Django의 테스트 검색 기능이 `tests` 패키지 내의 테스트를 발견할 수 있도록 `tests/__init__.py` 파일에서 각 테스트 모듈을 임포트한다.

## 2. 테스트 데이터 (Test Data)

- **데이터 생성 위치**: 테스트 데이터는 각 `TestCase` 클래스의 `setUp` 또는 `setUpTestData` 메서드 내에서 생성한다.
- **`setUpTestData` 활용**: 여러 테스트 메서드에서 공통으로 사용되는 데이터는 클래스 레벨에서 한 번만 생성되는 `setUpTestData`를 활용하여 테스트 효율성을 높인다.
