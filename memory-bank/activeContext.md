# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **뷰 리팩토링 (View Refactoring)**
- 기존의 함수 기반 뷰(FBV)를 클래스 기반 뷰(CBV)로 성공적으로 리팩토링했습니다.
- 모든 관련 테스트 케이스를 수정하고 통과를 확인하여 TDD 원칙을 준수했습니다.
- `.clinerules`와 `memory-bank` 문서를 최신 상태로 업데이트했습니다.

## 2. 최근 변경 사항 (Recent Changes)

- **`refactor(blog)`**: 모든 FBV를 CBV로 전환 (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`).
- **`fix(tests)`**: URL 네임스페이스 변경에 따라 `reverse()` 호출을 수정하고 모든 테스트가 통과하도록 수정.
- **`docs(.clinerules)`**: `codingStyle.md`에 CBV 우선 사용 규칙 추가.
- **`docs(memory-bank)`**: `progress.md` 및 `activeContext.md` 업데이트.

## 3. 다음 단계 (Next Steps)

- 모든 요구사항이 완료되었습니다. 프로젝트 완료를 보고합니다.
