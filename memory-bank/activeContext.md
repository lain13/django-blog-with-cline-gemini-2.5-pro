# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **테스트 파일 구조 리팩토링 계획 수립 및 문서화**
- `progress.md`에 명시된 `test_views.py` 파일의 비대화 문제를 해결하기 위해, 선행 리팩토링 원칙에 따라 테스트 파일 구조 개선 계획을 수립하고 관련 규칙 및 문서를 업데이트합니다.

## 2. 최근 변경 사항 (Recent Changes)

- **테스트 파일 분리 규칙 강화**: `.clinerules/testing.md` 파일을 수정하여, `views`, `forms`, `urls`와 같이 기능/모델 단위로 세분화된 경우 테스트 파일도 동일한 구조를 따르도록 규칙을 구체화했습니다.

## 3. 다음 단계 (Next Steps)

- **테스트 파일 리팩토링 실행**
  1.  계획에 따라 `blog/tests/test_views.py` 파일을 `test_post_views.py`, `test_comment_views.py` 등 기능/모델별 파일로 분리합니다.
  2.  분리된 테스트들이 모두 정상적으로 실행되는지 확인합니다. (`python manage.py test blog`)
  3.  리팩토링 완료 후 `progress.md`와 `activeContext.md`를 업데이트합니다.
  4.  리팩토링이 완료되면, 원래 계획이었던 **RSS 피드 기능 구현**을 TDD 사이클에 따라 진행합니다.
