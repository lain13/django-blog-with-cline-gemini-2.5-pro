# Product Context: Django TDD 블로그

## 1. 문제 정의 (Problem Statement)

개발자들이 TDD (Test-Driven Development) 방법론을 실제 Django 프로젝트에 어떻게 적용하는지 학습하고 연습할 수 있는 구체적인 예제가 필요하다. 많은 튜토리얼이 최종 코드만 보여줄 뿐, TDD의 점진적인 개발 과정을 보여주는 경우는 드물다.

## 2. 해결 방안 (Solution)

기본적인 블로그 애플리케이션을 TDD 방식으로 처음부터 끝까지 구축하는 과정을 보여준다. 각 기능 단위(모델, 뷰, 폼 등)를 테스트 코드로 먼저 정의하고, 해당 테스트를 통과시키는 코드를 작성하는 전체 흐름을 기록한다.

## 3. 사용자 경험 목표 (User Experience Goals)

- **개발자 중심**: 이 프로젝트의 사용자는 개발자이다. 따라서 최종 결과물보다는 개발 과정 자체가 명확하고 따라하기 쉬워야 한다.
- **기능의 명확성**: 각 기능(CRUD)은 URL을 통해 명확하게 접근하고 사용할 수 있어야 한다.
- **예측 가능한 동작**: 모든 기능은 테스트된 대로 정확하게 동작해야 한다.

## 4. 기능 요구사항 (Functional Requirements)

- **Post (게시글) 모델**: `title`, `content`, `created_at`, `updated_at` 필드를 포함해야 한다.
- **URL 라우팅**:
    - `/`: 게시글 목록 (List View)
    - `/post/<int:pk>/`: 게시글 상세 (Detail View)
    - `/post/new/`: 새 게시글 작성 (Create View)
    - `/post/<int:pk>/edit/`: 게시글 수정 (Update View)
    - `/post/<int:pk>/delete/`: 게시글 삭제 (Delete View)
