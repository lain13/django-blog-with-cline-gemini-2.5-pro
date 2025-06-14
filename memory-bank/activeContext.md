# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **국제화(i18n) 기능 구현 완료**
- 모델 필드, 뷰 메시지, 템플릿 번역 및 언어 전환 기능 구현을 모두 완료했습니다.

## 2. 최근 변경 사항 (Recent Changes)

- **TDD: 언어 전환 기능 구현**: Django의 내장 `set_language` 뷰를 활용하여 언어 전환 기능을 구현하고, 관련 테스트(`test_language_switcher`)를 작성 및 통과했습니다.
- **TDD: 뷰 메시지 번역**: `PostCreateView`의 성공 메시지에 `gettext`를 적용하고, 한국어/영어 번역이 올바르게 표시되는지 검증하는 테스트(`test_view_message_translation_ko`, `test_view_message_translation_en`)를 작성 및 통과했습니다.
- **TDD: 모델 필드 번역**: `Category` 모델의 `name` 필드 `verbose_name`에 `gettext_lazy`를 적용하고, 관련 테스트를 통과했습니다.
- **번역 파일 업데이트**: `makemessages` 및 `compilemessages`를 실행하여 모델 필드 및 뷰 메시지 번역을 모두 적용했습니다.

## 3. 다음 단계 (Next Steps)

- 다음 작업 계획을 수립합니다.
