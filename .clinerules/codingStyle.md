# Coding Style Rules

## 1. 아키텍처 패턴 (Architectural Patterns)

- **MVT (Model-View-Template)**: Django의 기본 MVT 패턴을 충실히 따른다.
- **Fat Models, Thin Views**: 비즈니스 로직은 가능한 모델(Model)에 집중시키고, 뷰(View)는 모델과 템플릿 간의 중개 역할에 집중한다.
- **모델 분리 (Model Separation)**: `models.py` 파일이 비대해지는 것을 방지하기 위해, 각 모델 클래스는 `models/` 디렉토리 내의 개별 파일로 분리하여 관리한다. (예: `blog/models/post.py`)
- **뷰 분리 (View Separation)**: `views.py` 파일이 비대해지는 것을 방지하기 위해, 각 기능(또는 모델)과 관련된 뷰는 `views/` 디렉토리 내의 개별 파일로 분리하여 관리한다. (예: `blog/views/post_views.py`)
- **폼 분리 (Form Separation)**: `forms.py` 파일이 비대해지는 것을 방지하기 위해, 각 폼 클래스는 `forms/` 디렉토리 내의 개별 파일로 분리하여 관리한다. (예: `blog/forms/post_forms.py`)

## 2. URL 설계 (URL Design)

- **URL 분리 (URL Separation)**: 프로젝트 최상위 `urls.py`는 각 앱(app)의 `urls.py`를 `include`하는 역할만 담당하여 URL 관리를 분산시킨다.

## 3. 의존성 관리 (Dependency Management)

- **내장 기능 우선 활용 (Prioritize Built-in Features)**: 외부 라이브러리 사용을 최소화하고, Django 프레임워크의 내장 기능(ORM, 테스트 프레임워크 등)을 최대한 활용한다.

## 4. 명명 규칙 (Naming Conventions)

- **Python**: [PEP 8](https://www.python.org/dev/peps/pep-0008/) 스타일 가이드를 따른다.
- **Django**: Django 코딩 스타일 가이드라인을 참고한다. (필요시 구체적인 규칙 추가)

## 5. 주석 (Comments)

- 복잡한 로직이나 특정 결정의 배경을 설명하기 위해 필요한 경우에만 주석을 작성한다. 코드는 자체적으로 설명 가능하도록 작성하는 것을 지향한다.

## 6. 코드 포매팅 (Code Formatting)

- **일관성 유지**: 프로젝트 전반에 걸쳐 일관된 코드 스타일을 유지한다.

## 7. 보안 (Security)

- **`SECRET_KEY` 관리**: `SECRET_KEY`는 환경 변수 등을 통해 안전하게 관리하며, 버전 관리 시스템에 직접 포함시키지 않는다.
- **`DEBUG` 모드**: 개발 환경에서는 `DEBUG = True`를 사용할 수 있으나, 프로덕션 환경에서는 반드시 `DEBUG = False`로 설정한다.

## 8. 템플릿 구조 (Template Structure)

- **앱별 템플릿 디렉토리**: 각 앱(app)의 템플릿은 해당 앱 디렉토리 내의 `templates/<app_name>/` 경로에 위치시켜 이름 충돌을 방지한다. (예: `blog/templates/blog/post_list.html`)

## 9. 정적 파일 관리 (Static Files Management)

- **앱별 정적 파일 디렉토리**: 각 앱(app)의 정적 파일(CSS, JavaScript, 이미지 등)은 해당 앱 디렉토리 내의 `static/<app_name>/` 경로에 위치시킨다. (예: `blog/static/blog/style.css`)
- **`STATICFILES_DIRS`**: 프로젝트 전반에서 사용되는 정적 파일은 `settings.py`의 `STATICFILES_DIRS`에 명시된 디렉토리에 위치시킨다.

## 10. 리팩토링 (Refactoring)

- **시기 (When to Refactor)**:
    - TDD (Test-Driven Development) 사이클의 Refactor 단계에서 수행한다.
    - 코드 스멜(Code Smells)이 발견될 때 (예: 중복 코드, 긴 함수, 과도하게 복잡한 로직 등).
    - 새로운 기능을 추가하거나 기존 기능을 수정하기 전후에 코드 구조를 개선할 필요가 있을 때.
- **단위 및 대상 (Unit and Target)**:
    - **DRY (Don't Repeat Yourself)**: 중복된 코드를 식별하고 제거한다. (함수, 클래스, 템플릿 조각 등으로 추상화)
    - **함수/메서드 분리**: 하나의 함수나 메서드가 너무 많은 일을 하거나 길어지면, 논리적인 단위로 분리한다.
    - **클래스 책임 명확화**: 클래스가 단일 책임 원칙(SRP)을 잘 따르고 있는지 검토하고, 필요시 분리하거나 재구성한다.
    - **가독성 향상**: 변수명, 함수명 등을 명확하게 개선하고, 복잡한 조건문이나 로직을 단순화한다.
- **원칙 (Principles)**:
- **점진적 개선**: 한 번에 너무 많은 변경을 하기보다는 작은 단위로 나누어 점진적으로 리팩토링한다.
    - **테스트 기반**: 리팩토링 전후로 테스트 코드가 항상 통과하는지 확인하여 기능의 안정성을 보장한다.
    - **목표 지향**: 가독성, 유지보수성, 확장성 향상 등 명확한 목표를 가지고 리팩토링을 진행한다.

## 11. 템플릿 로직 (Template Logic)

- **커스텀 템플릿 필터/태그 활용 (Use Custom Template Filters/Tags)**: 뷰(View)의 부담을 줄이고 템플릿의 재사용성을 높이기 위해, 단순한 표시(presentation) 관련 로직은 커스텀 템플릿 필터나 태그로 분리하여 구현한다. (예: 검색 결과 하이라이팅)
