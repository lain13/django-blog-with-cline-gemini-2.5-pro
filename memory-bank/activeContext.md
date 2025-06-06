# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **3. 포스트 목록 페이지 개발 (TDD)**
- 포스트 목록이 올바르게 표시되는지 확인하는 View 테스트 작성 준비

## 2. 최근 변경 사항 (Recent Changes)

- **Post 모델 개발 (TDD) 완료**
    - 실패하는 테스트 작성 (Red)
    - `Post` 모델 구현 (Green)
    - `blog` 앱 등록 및 마이그레이션
    - 테스트 통과 확인
    - 관련 변경사항 Git 커밋 완료

## 3. 다음 단계 (Next Steps)

1.  `blog/tests.py`에 포스트 목록 페이지(`post_list`)에 대한 테스트 코드 작성 (Red)
2.  `blog/views.py`에 `post_list` 뷰 구현 (Green)
3.  `config/urls.py`와 `blog/urls.py`에 URL 라우팅 설정
4.  `blog/templates/blog/post_list.html` 템플릿 생성
5.  테스트 실행하여 통과 확인
