# Django TDD Blog

## 1. 프로젝트 소개 (Introduction)

이 프로젝트는 **Test-Driven Development (TDD)** 방법론에 기반하여 Django 프레임워크를 사용해 기능적으로 완전한 블로그 애플리케이션을 개발하는 과정을 보여줍니다. 개발의 모든 단계는 Git을 통해 버전 관리되며, UI 테스트는 최소화하고 백엔드 로직과 기능 구현에 집중합니다.

개발자들이 TDD를 실제 Django 프로젝트에 어떻게 적용하는지 학습하고 연습할 수 있는 구체적인 예제를 제공하는 것을 목표로 합니다.

## 2. 주요 기능 (Key Features)

### 2.1. 핵심 블로그 기능
- **게시글 (Post) CRUD**: 사용자는 블로그 게시글을 생성, 조회, 수정, 삭제할 수 있습니다.
- **댓글 (Comment)**: 각 게시물에 댓글을 작성하고, 대댓글을 포함한 계층 구조로 조회할 수 있습니다.
- **검색 (Search)**: 키워드를 통해 게시물을 검색할 수 있습니다.
- **태그 (Tag)**: 게시물에 태그를 추가하고, 태그를 통해 게시물을 필터링할 수 있습니다.
- **계층형 카테고리 (Hierarchical Category)**: 다단계 카테고리를 생성하고, 카테고리별로 게시물을 분류하고 조회할 수 있습니다.
- **조회수 및 투표**: 게시물별 조회수 카운트 및 좋아요/싫어요 투표 기능을 제공합니다.

### 2.2. 사용자 시스템
- **사용자 인증**: 회원가입, 로그인, 로그아웃 기능을 제공합니다.
- **권한 관리**: 게시물 및 댓글의 생성, 수정, 삭제는 작성자 본인만 가능하도록 제어됩니다.
- **사용자 프로필**: 사용자는 자신의 프로필(자기소개, 아바타)을 조회하고 수정할 수 있습니다.
- **스팸 방지**: 회원가입 및 댓글 작성 시 CAPTCHA를 통해 스팸을 방지합니다.

### 2.3. API (Django REST Framework)
- **RESTful API**: `Post`, `Comment`, `Category`, `Tag` 모델에 대한 CRUD API 엔드포인트를 제공합니다.
- **인증**: 토큰 기반 인증(Token Authentication)을 지원합니다.
- **고급 기능**: 페이징(Pagination), 검색(Search), 필터링(Filtering), 정렬(Ordering) 기능을 지원합니다.
- **API 문서**: `drf-spectacular`를 통해 Swagger UI 기반의 API 문서를 자동으로 생성합니다. (`/api/schema/swagger-ui/`)

### 2.4. 부가 기능
- **RSS 피드**: 블로그의 최신 게시물을 RSS로 구독할 수 있습니다. (`/feed/`)
- **국제화 (i18n)**: 한국어와 영어를 지원하며, URL을 통해 언어를 전환할 수 있습니다. (`/ko/`, `/en/`)
- **커스텀 템플릿 태그**: 재사용 가능한 UI 컴포넌트나 로직을 템플릿 태그로 만들어 사용합니다.

## 3. 기술 스택 (Tech Stack)

- **Backend**: Python 3.12, Django 5.2
- **API**: Django REST Framework
- **Database**: SQLite
- **Testing**: Django's built-in test framework, `unittest`
- **Security**: `django-simple-captcha`
- **API Docs**: `drf-spectacular`
- **Version Control**: Git

## 4. 설치 및 실행 (Setup and Run)

### 4.1. 환경 설정
```bash
# 1. 저장소 복제
git clone https://github.com/lain13/django-blog-with-cline-gemini-2.5-pro.git
cd django-tdd-blog

# 2. 가상 환경 생성 및 활성화
python -m venv venv
source venv/Scripts/activate  # Windows Git Bash
# venv\Scripts\activate  # Windows CMD

# 3. 의존성 패키지 설치
pip install -r requirements.txt

# 4. .env 파일 설정
# .env.example 파일을 복사하여 .env 파일을 생성하고, SECRET_KEY 등 필요한 값을 설정합니다.
cp .env.example .env
```

### 4.2. 데이터베이스 설정
```bash
# 데이터베이스 마이그레이션
python manage.py migrate
```

### 4.3. 개발 서버 실행
```bash
# 개발 서버 시작
python manage.py runserver
```
서버가 실행되면 `http://127.0.0.1:8000/` 주소로 접속할 수 있습니다.

## 5. 테스트 (Testing)

프로젝트의 모든 기능은 TDD로 개발되었으며, 아래 명령어로 전체 테스트를 실행할 수 있습니다.

```bash
# 모든 테스트 실행
python manage.py test
