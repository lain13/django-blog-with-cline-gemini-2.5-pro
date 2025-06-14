# Tech Context: Django TDD 블로그

## 1. 기술 스택 (Technology Stack)

- **언어 (Language)**: Python 3.12.x
- **프레임워크 (Framework)**: Django 5.2.2
- **데이터베이스 (Database)**: SQLite
- **API**: Django REST Framework 3.16.0
- **보안 (Security)**: django-simple-captcha 0.6.0
- **Frontend/Communication**: AJAX, JSON
- **버전 관리 (Version Control)**: Git

## 2. 개발 환경 설정 (Development Setup)

1.  **Python 가상 환경 (Virtual Environment)**:
    - 프로젝트 의존성을 시스템 라이브러리와 분리하기 위해 `venv` 모듈을 사용하여 가상 환경을 생성한다.
    - 명령어: `python -m venv venv`

2.  **의존성 설치 (Dependency Installation)**:
    - 가상 환경을 활성화한 후, `pip`을 사용하여 `requirements.txt` 파일에 명시된 모든 패키지를 설치한다.
    - 명령어: `pip install -r requirements.txt`

3.  **Django 프로젝트 구조 (Project Structure)**:
    - `django-admin startproject config .` 명령어로 현재 디렉토리에 `config`라는 이름의 프로젝트를 생성한다.
    - `python manage.py startapp <app_name>` 명령어로 `blog`, `users` 등의 앱을 생성한다.

## 3. 외부 라이브러리 사용 원칙 (External Library Usage)

- **Django REST Framework (DRF)**: RESTful API 엔드포인트를 빠르고 일관성 있게 구축하기 위해 사용한다. 제네릭 뷰, 시리얼라이저, 권한 시스템을 적극 활용한다.
- **django-simple-captcha**: 회원가입, 댓글 작성 등 주요 폼에 CAPTCHA를 추가하여 스팸 봇으로부터 시스템을 보호하기 위해 사용한다.
- 그 외의 기능은 가급적 Django 내장 기능(테스트 프레임워크, ORM 등)을 최대한 활용하여 의존성을 낮게 유지한다.

## 4. 기술적 결정 사항 (Technical Decisions)

- **한글 슬러그 지원**: `Category` 모델의 `slug` 필드에 `allow_unicode=True` 옵션을 적용하여, URL에서 한글을 사용할 수 있도록 지원한다.
- **AJAX 통신**: '좋아요/싫어요' 기능과 같이 페이지 새로고침 없이 서버와 통신이 필요한 경우, JavaScript의 `fetch` API와 `JsonResponse`를 사용한 AJAX 통신을 구현한다.
