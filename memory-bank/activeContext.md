# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **최종 버그 수정 및 프로젝트 완료 (Final Bug Fix and Project Completion)**
- `progress.md`에 문서화되어 있던 간헐적 테스트 실패 이슈(`test_search_by_title`)를 해결했습니다.
- 원인은 검색 결과의 비결정적 순서와 `highlight` 템플릿 필터로 인한 `assertContains`의 오작동이었습니다.
- `SearchView`에 `order_by('pk')`를 추가하고, 테스트 코드에서 불안정한 `assertContains` 대신 컨텍스트 데이터를 직접 검증하도록 수정하여 문제를 해결했습니다.
- 모든 테스트(49개)가 안정적으로 통과하는 것을 확인했습니다.

## 2. 최근 변경 사항 (Recent Changes)

- **`fix(blog)`**: `SearchView`에 `order_by('pk')`를 추가하여 검색 결과의 순서를 보장.
- **`fix(tests)`**: `test_search_by_title` 테스트가 `highlight` 필터와 무관하게 컨텍스트 데이터를 검증하도록 수정.
- **`chore(deps)`**: `lxml` 패키지를 추가하여 HTML 파싱 안정성 확보 시도.
- **`docs(memory-bank)`**: `progress.md`와 `activeContext.md`를 최종 상태로 업데이트.

## 3. 다음 단계 (Next Steps)

- 모든 요구사항이 완료되었고, 알려진 이슈도 해결되었습니다. 프로젝트 완료를 보고합니다.
