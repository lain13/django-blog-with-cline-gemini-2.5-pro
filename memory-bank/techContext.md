# Tech Context: Django TDD 블로그

## 1. 기술 스택 (Technology Stack)

- **언어 (Language)**: Python 3.x
- **프레임워크 (Framework)**: Django 5.2.x
- **데이터베이스 (Database)**: SQLite
- **버전 관리 (Version Control)**: Git

## 2. 개발 환경 설정 (Development Setup)

1.  **Python 가상 환경 (Virtual Environment)**:
    - 프로젝트 의존성을 시스템 라이브러리와 분리하기 위해 `venv` 모듈을 사용하여 가상 환경을 생성한다.
    - 명령어: `python -m venv venv`

2.  **의존성 설치 (Dependency Installation)**:
    - 가상 환경을 활성화한 후, `pip`을 사용하여 필요한 패키지를 설치한다.
    - 초기에는 `Django`만 설치한다.
    - 명령어: `pip install django`
    - `requirements.txt` 파일을 생성하여 의존성을 관리한다.

3.  **Django 프로젝트 구조 (Project Structure)**:
    - `django-admin startproject config .` 명령어로 현재 디렉토리에 `config`라는 이름의 프로젝트를 생성한다.
    - `python manage.py startapp blog` 명령어로 `blog` 앱을 생성한다.

## 3. 기술적 제약사항 (Technical Constraints)

- 외부 라이브러리 사용을 최소화하고 Django의 내장 기능(테스트 프레임워크, ORM 등)을 최대한 활용한다.
- 데이터베이스는 개발의 편의성을 위해 SQLite를 사용하며, 별도의 데이터베이스 서버 설정은 하지 않는다.
