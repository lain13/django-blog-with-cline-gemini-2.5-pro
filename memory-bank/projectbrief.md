# Project Brief: Django TDD 블로그

## 1. 프로젝트 목표 (Core Objective)

Test-Driven Development (TDD) 방법론에 기반하여 Django 프레임워크를 사용해 기능적으로 완전한 블로그 애플리케이션을 개발한다. 개발의 모든 단계는 Git을 통해 버전 관리되며, UI 테스트는 최소화하고 백엔드 로직과 기능 구현에 집중한다.

## 2. 핵심 기능 (Key Features)

- **게시글 (Post) CRUD**: 사용자는 블로그 게시글을 생성(Create), 조회(Read), 수정(Update), 삭제(Delete)할 수 있다.
- **TDD 접근 방식**: 모든 기능은 실패하는 테스트를 먼저 작성하고, 이를 통과시키는 코드를 구현하는 방식으로 개발한다.
- **버전 관리**: 각 기능 구현 단계별로 Git commit을 통해 변경 사항을 추적하고 관리한다.
- **댓글 기능**: 사용자는 각 게시물에 댓글을 작성하고 조회할 수 있다.
- **검색 기능**: 사용자는 키워드를 통해 게시물을 검색할 수 있다.

## 3. 기술 스택 (Tech Stack)

- **Backend**: Python, Django
- **Database**: SQLite
- **Testing**: Django's built-in test framework
- **Version Control**: Git

## 4. 제약 조건 (Constraints)

- UI/UX 테스트는 최소화한다. 기능의 핵심 로직 테스트에 집중한다.
- 데이터베이스는 프로젝트 설정의 복잡성을 줄이기 위해 SQLite를 사용한다.
- 모든 문서는 한글을 기본으로 하되, 기술 용어는 영문 표기를 병기하여 명확성을 높인다.
