# Active Context: Django TDD 블로그

## 1. 현재 작업 포커스 (Current Focus)

- **국제화(i18n) 기능 구현: 모델 및 뷰 번역**
- URL 및 기본 템플릿의 국제화 설정을 완료했으며, 이제 모델 필드와 뷰에서 사용하는 메시지를 번역할 차례입니다.

## 2. 최근 변경 사항 (Recent Changes)

- **i18n 환경 설정**: `settings.py`에 `LocaleMiddleware` 추가, `LANGUAGES`, `LOCALE_PATHS` 등 국제화 기본 설정을 완료했습니다.
- **TDD: URL 국제화 구현**: `config/urls.py`에 `i18n_patterns`를 적용하고 관련 테스트를 통과시켰습니다.
- **TDD: 기본 템플릿 번역**: `base.html`에 `{% trans %}` 태그를 적용하고, 번역 파일(`.po`, `.mo`)을 생성 및 컴파일하여 관련 테스트를 통과시켰습니다.

## 3. 다음 단계 (Next Steps)

- **1. TDD: 모델 필드 번역**: `Category` 모델의 `name` 필드와 같이 사용자에게 표시되는 모델 필드에 `gettext_lazy`를 적용하고, 번역이 올바르게 표시되는지 검증하는 테스트를 작성합니다.
- **2. TDD: 뷰 메시지 번역**: 뷰에서 `messages` 프레임워크를 통해 사용자에게 전달하는 성공/오류 메시지를 번역하고, 이를 검증하는 테스트를 작성합니다.
- **3. 언어 전환 기능 구현**: 사용자가 언어를 선택할 수 있는 UI를 구현하고, 관련 뷰와 로직을 작성합니다.
