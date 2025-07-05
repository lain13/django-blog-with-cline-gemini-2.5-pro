# Security Rules

이 문서는 프로젝트의 보안을 강화하고, 민감 정보 유출을 방지하며, 안정적인 서비스를 운영하기 위한 보안 규칙을 정의한다.

## 1. 민감 정보 관리 (Sensitive Information Management)

- **원칙**: `SECRET_KEY`, 데이터베이스 자격 증명, API 키 등 모든 민감 정보는 Git 저장소에 절대 포함시키지 않는다.
- **구현**:
    - **Tool**: `python-dotenv` 라이브러리를 사용한다.
    - **프로세스**:
        1. 프로젝트 루트에 `.env` 파일을 생성하여 모든 민감 정보를 `KEY=VALUE` 형식으로 저장한다.
        2. `config/settings.py`에서는 `os.getenv('KEY_NAME')` 또는 `os.environ.get('KEY_NAME')`을 사용하여 환경 변수를 로드한다.
        3. `.gitignore` 파일에 `.env`를 반드시 추가하여 버전 관리에서 제외한다.
    - **예시**:
        ```python
        # settings.py
        import os
        from dotenv import load_dotenv
        load_dotenv()
        SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
        ```

## 2. 디버그 모드 (DEBUG Mode)

- **원칙**: `DEBUG` 모드는 로컬 개발 환경에서만 `True`로 설정하고, 프로덕션(배포) 환경에서는 반드시 `False`로 설정한다.
- **구현**: 환경 변수를 사용하여 `DEBUG` 모드를 동적으로 설정한다.
    - **예시**:
        ```python
        # settings.py
        DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'
        ```

## 3. 허용 호스트 (ALLOWED_HOSTS)

- **원칙**: 프로덕션 환경에서는 `ALLOWED_HOSTS`에 서비스할 도메인과 IP 주소를 명시적으로 지정해야 한다.
- **구현**: 환경 변수를 사용하여 배포 환경에 맞는 호스트를 설정한다.
    - **예시**:
        ```python
        # settings.py
        ALLOWED_HOSTS_STRING = os.getenv('DJANGO_ALLOWED_HOSTS')
        if ALLOWED_HOSTS_STRING:
            ALLOWED_HOSTS = ALLOWED_HOSTS_STRING.split(',')
        else:
            ALLOWED_HOSTS = []
        ```

## 4. 보안 체크리스트 (Security Checklist)

- **원칙**: 코드를 프로덕션 환경에 배포하기 전, Django에서 제공하는 공식 보안 체크리스트를 반드시 실행하고 모든 항목을 점검한다.
- **명령어**: `python manage.py check --deploy`

## 5. 의존성 관리 (Dependency Management)

- **원칙**: 개발용과 프로덕션용 의존성을 분리하여 관리하는 것을 권장한다.
- **파일**:
    - `requirements.txt`: 프로덕션 환경에 필요한 최소한의 패키지.
    - `requirements-dev.txt`: `black`, `flake8` 등 개발 및 테스트에만 필요한 패키지.
