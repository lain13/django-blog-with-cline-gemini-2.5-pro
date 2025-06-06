# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **7. 포스트 삭제 기능 개발 (TDD)**
- 기존 포스트를 삭제하는 기능에 대한 테스트 작성 준비

## 2. 최근 변경 사항 (Recent Changes)

- **포스트 수정 기능 개발 (TDD) 완료**
    - 실패하는 View 테스트 작성 (Red)
    - `post_edit` 뷰 구현 및 `post_form` 템플릿 재사용 (Green)
    - 테스트 통과 확인
    - 관련 변경사항 Git 커밋 완료

## 3. 다음 단계 (Next Steps)

1.  `blog/tests.py`에 포스트 삭제 기능(`post_delete`)에 대한 테스트 코드 작성 (Red)
2.  `blog/views.py`에 `post_delete` 뷰 구현 (Green)
3.  `blog/urls.py`에 URL 라우팅 설정
4.  `blog/templates/blog/post_confirm_delete.html` 템플릿 생성
5.  테스트 실행하여 통과 확인
