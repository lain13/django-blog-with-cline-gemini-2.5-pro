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
