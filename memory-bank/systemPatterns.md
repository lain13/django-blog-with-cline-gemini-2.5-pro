# System Patterns: Django TDD 블로그

## 1. 시스템 아키텍처 (System Architecture)

이 프로젝트는 Django 프레임워크의 기본 아키텍처인 **MVT (Model-View-Template)** 패턴을 따른다.

- **Model**: 데이터베이스의 구조를 정의한다. `blog/models.py`에 `Post` 모델을 정의하여 블로그 게시글 데이터를 관리한다.
- **View**: 비즈니스 로직을 처리한다. 사용자의 요청(Request)을 받아 필요한 데이터를 모델에서 가져와 가공한 후, 템플릿에 전달하여 응답(Response)을 생성한다. `blog/views.py`에 구현된다.
- **Template**: 사용자에게 보여지는 UI를 담당한다. View로부터 전달받은 데이터를 HTML에 렌더링한다. `blog/templates/` 디렉토리 내에 위치한다.

## 2. 디자인 패턴 (Design Patterns)

- **TDD (Test-Driven Development)**: Red-Green-Refactor 사이클을 따른다.
    1.  **Red**: 실패하는 테스트 케이스를 작성한다.
    2.  **Green**: 테스트를 통과하는 최소한의 코드를 작성한다.
    3.  **Refactor**: 코드의 구조를 개선한다.
- **Fat Models, Thin Views**: 가능한 한 비즈니스 로직은 모델(Model)에 집중시키고, 뷰(View)는 모델과 템플릿을 연결하는 역할에 충실하도록 유지한다.
- **URL 분리**: 프로젝트의 최상위 `urls.py`는 각 앱의 `urls.py`를 `include`하는 역할만 담당하여 URL 관리를 분산시킨다.

## 3. 컴포넌트 관계 (Component Relationships)

```mermaid
graph TD
    subgraph "User Request"
        URL[URL 요청]
    end

    subgraph "Django"
        URL_Resolver[URL Resolver] --> View[View]
        View --> Model[Model]
        View --> Template[Template]
        Model --> DB[(Database)]
        Template --> Rendered_HTML[Rendered HTML]
    end

    subgraph "User Response"
        Response[HTTP 응답]
    end

    URL --> URL_Resolver
    Rendered_HTML --> Response
