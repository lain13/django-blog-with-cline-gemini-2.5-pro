# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **4. 포스트 상세 페이지 개발 (TDD)**
- 특정 포스트의 내용이 올바르게 표시되는지 확인하는 View 테스트 작성 준비

## 2. 최근 변경 사항 (Recent Changes)

- **포스트 목록 페이지 개발 (TDD) 완료**
    - 실패하는 View 테스트 작성 (Red)
    - `post_list` 뷰, URL, 템플릿 구현 (Green)
    - 테스트 통과 확인
    - 관련 변경사항 Git 커밋 완료

## 3. 다음 단계 (Next Steps)

1.  `blog/tests.py`에 포스트 상세 페이지(`post_detail`)에 대한 테스트 코드 작성 (Red)
2.  `blog/views.py`에 `post_detail` 뷰 구현 (Green)
3.  `blog/urls.py`에 URL 라우팅 설정
4.  `blog/templates/blog/post_detail.html` 템플릿 생성
5.  테스트 실행하여 통과 확인
