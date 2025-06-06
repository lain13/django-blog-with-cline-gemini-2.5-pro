# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **5. 포스트 생성 기능 개발 (TDD)**
- 새로운 포스트를 생성하는 기능에 대한 테스트 작성 준비

## 2. 최근 변경 사항 (Recent Changes)

- **포스트 상세 페이지 개발 (TDD) 완료**
    - 실패하는 View 테스트 작성 (Red)
    - `post_detail` 뷰, URL, 템플릿 구현 (Green)
    - 테스트 통과 확인
    - 관련 변경사항 Git 커밋 완료

## 3. 다음 단계 (Next Steps)

1.  `blog/tests.py`에 포스트 생성 페이지(`post_new`)에 대한 테스트 코드 작성 (Red)
2.  `blog/forms.py`에 `PostForm` 생성
3.  `blog/views.py`에 `post_new` 뷰 구현 (Green)
4.  `blog/urls.py`에 URL 라우팅 설정
5.  `blog/templates/blog/post_form.html` 템플릿 생성
6.  테스트 실행하여 통과 확인
