# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **계층형 카테고리 기능 개발 (Hierarchical Category Feature Development)** 
- `makemigrations` 문제 성공적 해결 및 `Post` 모델에 `author` 필드 추가 완료.
- `progress.md`에 계획된 다음 작업인 '계층형 카테고리' 기능 개발 시작 준비 완료.

## 2. 최근 변경 사항 (Recent Changes)

- **`fix(model)`**: `Post` 모델에 `author` ForeignKey 필드 추가 (`null=False`).
- **`fix(migration)`**: 2단계 마이그레이션 전략 사용, 기존 `Post` 데이터에 기본 `author` 할당 및 `makemigrations` 문제 해결.
- **`refactor(test)`**: `author` 필드 추가에 따라 `test_models.py`, `test_views.py`, `test_forms.py` 테스트 코드 리팩토링.
- **`refactor(view)`**: `PostCreateView`가 요청 보낸 사용자를 `author`로 자동 할당하도록 수정.
- **`docs(memory-bank)`**: `activeContext.md`와 `progress.md` 현재 상태에 맞게 업데이트.

## 3. 다음 단계 (Next Steps)

- **계층형 카테고리 기능 개발 (Hierarchical Category Feature Development)**
  - `progress.md` 계획 순서에 따라 '계층형 카테고리' 기능 개발을 TDD 사이클에 맞춰 진행.
  - 첫 단계는 `Category` 모델 정의 및 실패하는 테스트 작성.
