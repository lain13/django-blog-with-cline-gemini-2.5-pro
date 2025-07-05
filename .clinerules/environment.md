# Environment Rules

이 문서는 일관성을 보장하기 위해 프로젝트의 개발, 테스트 및 프로덕션 환경 규칙을 정의한다.

## 1. 개발 환경 (Development Environment)

- **OS**: Windows 11
- **Shell**: Git Bash
- **Python**: 3.12
- **IDE**: Visual Studio Code

## 2. 가상 환경 (Virtual Environment)

- **Tool**: `venv`
- **생성 (Creation)**: `python -m venv venv`
- **활성화 (Activation)**: `source venv/Scripts/activate`
- **비활성화 (Deactivation)**: `deactivate`

## 3. 패키지 관리 (Package Management)

- **Tool**: `pip`
- **패키지 설치 (Installation)**: 가상 환경 활성화 후 `pip install <package_name>`
- **의존성 파일 (Dependencies File)**: `requirements.txt`
    - **생성/업데이트 (Freeze)**: `pip freeze > requirements.txt`
    - **설치 (Installation from file)**: `pip install -r requirements.txt`

## 4. 프레임워크 (Framework)

- **Name**: Django
- **Version**: 5.2.x (latest stable)

## 5. 프로덕션 환경 (Production Environment)

- **웹 서버 (Web Server)**: Nginx (권장)
- **WSGI 서버 (WSGI Server)**: Gunicorn (권장)
- **데이터베이스 (Database)**: PostgreSQL (권장)
- **환경 변수**: 모든 민감 정보는 `.env` 파일을 통해 관리한다. (`.clinerules/security.md` 참조)
- **배포 절차**:
    1. `git pull`
    2. `pip install -r requirements.txt`
    3. `python manage.py migrate`
    4. `python manage.py collectstatic --noinput`
    5. `python manage.py check --deploy`
    6. WSGI 서버 재시작

## 6. 환경 변수 (Environment Variables)
- **민감 정보 관리**: 모든 민감 정보(`SECRET_KEY`, `DB_PASSWORD` 등)는 `.env` 파일을 통해 관리합니다.
- **설정 방법**:
    1. 프로젝트 루트의 `.env.example` 파일을 복사하여 `.env` 파일을 생성합니다.
    2. `.env` 파일 내에 필요한 환경 변수 값을 설정합니다.
    3. `.env` 파일은 `.gitignore`에 등록되어 버전 관리에서 제외됩니다.
