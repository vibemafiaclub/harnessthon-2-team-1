# 검증 스크립트 테스트

하네스 자체가 아니라 **검사 스크립트가 제대로 동작하는지** 확인하는 최소 픽스처.

```bash
bash tests/run_tests.sh
```

- `fixture-fail/` — 일부러 깨뜨린 산출물. 깨진 참조(`SCR-77`), `partial` 요구사항, 미판정 `RISK-10`, 플로우 없는 역할이 들어 있다
- `fixture-pass/` — 위를 고친 것
- `fixture-wf-pass/` — STEP 8 입력 패키지 검사기(`check_wireframe_input.py`)용. `planning/`(상위기획 최소 산출물)과 `package/`(패키지 5종)이 짝을 이루며 통과해야 정상이다
- `fixture-wf-fail/` — 같은 짝에서 패키지만 다섯 가지로 깨뜨린 것. 절 삭제, 상위기획에 없는 `SCR-99`, 누락된 `ONB-01`, 빠진 `RISK-12` 행, 남아 있는 자리표시자 `{프로젝트명}`
- `fixture-fail-onboarding/` — 참조는 전부 정상이지만 온보딩만 깨진 것. `ROLE-02`에 온보딩 경로가 없고, `required: true` 단계에 근거가 비어 있고, `ONB-01`이 `partial`이다. `validate_ids.py`는 통과하고 `check_coverage.py`만 실패해야 정상이다

스크립트를 수정했으면 이걸 먼저 돌려본다.
