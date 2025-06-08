# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **계층형 카테고리 기능 개발 (Hierarchical Category Feature Development)**
- TDD의 첫 단계인 **실패하는 테스트 코드 작성 완료**. (`blog/tests/test_models.py`)
- 가상 환경 활성화의 중요성을 인지하고, 다음 단계에서 테스트를 실행할 준비.

## 2. 최근 변경 사항 (Recent Changes)

- **`test(model)`**: `Category` 모델과 `Post.category` 필드에 대한 실패하는 테스트 케이스 추가.
- **`fix(model)`**: `Post` 모델에 `author` ForeignKey 필드 추가 (`null=False`).
- **`fix(migration)`**: 2단계 마이그레이션 전략 사용, 기존 `Post` 데이터에 기본 `author` 할당 및 `makemigrations` 문제 해결.
- **`refactor(test)`**: `author` 필드 추가에 따라 `test_models.py`, `test_views.py`, `test_forms.py` 테스트 코드 리팩토링.
- **`refactor(view)`**: `PostCreateView`가 요청 보낸 사용자를 `author`로 자동 할당하도록 수정.
- **`docs(memory-bank)`**: `activeContext.md`와 `progress.md` 현재 상태에 맞게 업데이트.

## 3. 다음 단계 (Next Steps)

- **실패하는 테스트(Red) 확인**
  - **중요**: `venv\Scripts\activate` 명령으로 가상 환경을 반드시 활성화한 후, `python manage.py test blog`를 실행하여 `Category` 모델이 없어 테스트가 실패하는지(Red) 확인한다.
  - 이 확인 작업은 다음 태스크에서 진행한다.
