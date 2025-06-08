# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **계층형 카테고리 기능 개발 (Hierarchical Category Feature Development)**
- `makemigrations` 문제를 성공적으로 해결하고 `Post` 모델에 `author` 필드를 추가했습니다.
- 이제 `progress.md`에 계획된 다음 작업인 '계층형 카테고리' 기능 개발을 시작할 준비가 되었습니다.

## 2. 최근 변경 사항 (Recent Changes)

- **`fix(model)`**: `Post` 모델에 `author` ForeignKey 필드를 추가했습니다. (`null=False`)
- **`fix(migration)`**: 2단계 마이그레이션 전략을 사용하여 기존 `Post` 데이터에 기본 `author`를 할당하고, `makemigrations` 문제를 해결했습니다.
- **`refactor(test)`**: `author` 필드 추가에 따라 `test_models.py`, `test_views.py`, `test_forms.py`의 테스트 코드를 리팩토링했습니다.
- **`refactor(view)`**: `PostCreateView`가 요청을 보낸 사용자를 `author`로 자동 할당하도록 수정했습니다.
- **`docs(memory-bank)`**: `activeContext.md`와 `progress.md`를 현재 상태에 맞게 업데이트했습니다.

## 3. 다음 단계 (Next Steps)

- **계층형 카테고리 기능 개발 (Hierarchical Category Feature Development)**
  - `progress.md`에 계획된 순서에 따라 '계층형 카테고리' 기능 개발을 TDD 사이클에 맞춰 진행합니다.
  - 첫 단계는 `Category` 모델을 정의하고, 실패하는 테스트를 작성하는 것입니다.
