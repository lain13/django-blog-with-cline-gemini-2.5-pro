# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **2. Post 모델 개발 (TDD)**
- `Post` 모델이 존재하는지 확인하는 테스트 코드 작성

## 2. 최근 변경 사항 (Recent Changes)

- **프로젝트 초기 설정 완료**
    - `.clinerules` 정의 및 생성
    - 가상 환경 설정 및 Django 설치 완료
    - `requirements.txt` 생성
    - `config` 프로젝트 및 `blog` 앱 생성
    - 모든 변경사항 Git 커밋 완료

## 3. 다음 단계 (Next Steps)

1.  `blog/tests.py`에 `Post` 모델 존재 여부를 확인하는 테스트 코드 작성 (Red)
2.  `blog/models.py`에 `Post` 모델 구현 (Green)
3.  `config/settings.py`에 `blog` 앱 등록
4.  `makemigrations` 및 `migrate` 실행
5.  테스트 실행하여 통과 확인
