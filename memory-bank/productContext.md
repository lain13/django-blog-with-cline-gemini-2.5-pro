# Product Context: Django TDD 블로그

## 1. 문제 정의 (Problem Statement)

개발자들이 TDD (Test-Driven Development) 방법론을 실제 Django 프로젝트에 어떻게 적용하는지 학습하고 연습할 수 있는 구체적인 예제가 필요하다. 많은 튜토리얼이 최종 코드만 보여줄 뿐, TDD의 점진적인 개발 과정을 보여주는 경우는 드물다.

## 2. 해결 방안 (Solution)

기본적인 블로그 애플리케이션을 TDD 방식으로 처음부터 끝까지 구축하는 과정을 보여준다. 각 기능 단위(모델, 뷰, 폼 등)를 테스트 코드로 먼저 정의하고, 해당 테스트를 통과시키는 코드를 작성하는 전체 흐름을 기록한다.

## 3. 사용자 경험 목표 (User Experience Goals)

- **개발자 중심**: 이 프로젝트의 사용자는 개발자이다. 따라서 최종 결과물보다는 개발 과정 자체가 명확하고 따라하기 쉬워야 한다.
- **기능의 명확성**: 각 기능(CRUD, 댓글, 검색 등)은 URL을 통해 명확하게 접근하고 사용할 수 있어야 한다.
- **예측 가능한 동작**: 모든 기능은 테스트된 대로 정확하게 동작해야 한다.

## 4. 기능 요구사항 (Functional Requirements)

### 4.1. 데이터 모델 (Data Models)

- **`Post` (게시글)**
  - `author`: 작성자 (User 모델과 연결, ForeignKey)
  - `title`: 제목 (CharField)
  - `content`: 내용 (TextField)
  - `created_at`: 생성일 (DateTimeField, 자동 생성)
  - `updated_at`: 수정일 (DateTimeField, 자동 갱신)
  - `tags`: 태그 (Tag 모델과 다대다 관계, ManyToManyField)

- **`Comment` (댓글)**
  - `post`: 원본 게시글 (Post 모델과 연결, ForeignKey)
  - `author`: 작성자 이름 (CharField)
  - `text`: 댓글 내용 (TextField)
  - `created_at`: 생성일 (DateTimeField, 자동 생성)

- **`Tag` (태그)**
  - `name`: 태그 이름 (CharField, 고유값)

### 4.2. URL 라우팅 (URL Routing)

- **Post (게시글)**
  - `GET /`: 게시글 목록
  - `GET /post/<int:pk>/`: 게시글 상세
  - `GET, POST /post/new/`: 새 게시글 작성
  - `GET, POST /post/<int:pk>/edit/`: 게시글 수정
  - `GET, POST /post/<int:pk>/delete/`: 게시글 삭제

- **Comment (댓글)**
  - `POST /post/<int:pk>/comment/`: 특정 게시글에 댓글 작성

- **Tag (태그)**
  - `GET /tag/<str:tag_name>/`: 특정 태그를 포함하는 게시글 목록

- **Search (검색)**
  - `GET /search/?q=<keyword>`: 키워드로 게시글 검색
