# STEP 5 — 검증

산출물: `validation.csv`
템플릿: `templates/validation.template.csv`

이 스텝의 목적은 **스스로 놓친 것을 찾아내는 것**이다. "잘 만들었다"를 확인하는 스텝이 아니다.
통과할 때까지 STEP 2~4로 되돌아간다.

## 1. 요구사항 추적표 작성

`definition.md`의 모든 `REQ-`를 한 행씩 놓고, 어느 화면·플로우가 커버하는지 채운다.

```csv
type,id,description,covered_by_screen,covered_by_flow,policy,status
REQ,REQ-01,지인을 이름·관계·연락처로 등록한다,SCR-03,FLW-01,POL-02,covered
```

`status`는 셋 중 하나다.

- `covered` — 화면과 플로우가 모두 있음
- `partial` — 화면은 있으나 플로우가 없거나 그 반대
- `gap` — 어느 쪽도 없음

`partial`과 `gap`이 하나라도 있으면 **이 스텝은 실패다.** STEP 2 또는 STEP 3으로 돌아간다.

## 2. 리스크 패턴 순회 (건너뛰지 않는다)

`references/risk-patterns.md`의 `RISK-01` ~ `RISK-12`를 **전부** 한 행씩 놓는다. 12행이 반드시 존재해야 한다.

```csv
type,id,description,covered_by_screen,covered_by_flow,policy,status
RISK,RISK-01,다대다 귀속 모호성 → EC-01 한 지인이 두 그룹에 소속,SCR-04,FLW-01,POL-05,covered
RISK,RISK-11,알림·리마인드,,,,not-applicable
```

- 해당되면 `EC-` 발현형을 `description`에 쓰고 대응 화면·정책을 채운다
- 해당 없으면 `status`를 `not-applicable`로 두되, **비워두지 않는다**
- `not-applicable` 판정에는 근거가 필요하다. 근거가 애매하면 해당된다고 보는 편이 안전하다

12행 중 하나라도 비어 있으면 실패다.

## 3. 스크립트 검증

```bash
python scripts/validate_ids.py   {프로젝트명}/01-planning
python scripts/check_coverage.py {프로젝트명}/01-planning
```

| 스크립트 | 잡아내는 것 |
|---|---|
| `validate_ids.py` | 정의되지 않은 ID 참조, 아무도 참조하지 않는 고아 ID, 중복 ID, 형식 오류 |
| `check_coverage.py` | `partial`·`gap` 요구사항, 12패턴 미판정, 역할별 플로우 누락 |

둘 다 exit code 0이어야 통과다.

### 실행 환경이 없을 때

스크립트를 돌릴 수 없으면 아래를 수동으로 수행하고, **수동 수행했음을 `_handoff.md`에 명시한다.**

- [ ] `flows.yaml`에 등장하는 모든 `SCR-`가 `ia.yaml`에 정의되어 있는가
- [ ] `ia.yaml`의 모든 `SCR-`가 `flows.yaml` 또는 `validation.csv`에서 참조되는가
- [ ] `policy.md`의 모든 `POL-`이 어딘가에서 참조되는가
- [ ] `validation.csv`에 `REQ-` 전체가 빠짐없이 있는가
- [ ] `RISK-01`~`RISK-12` 12행이 모두 있는가
- [ ] 모든 `ROLE-`에 최소 하나의 `FLW-`가 있는가

## 4. 되돌아가기 규칙

| 실패 유형 | 되돌아갈 곳 |
|---|---|
| 커버할 화면이 없음 | STEP 2 |
| 화면은 있으나 도달 경로가 없음 | STEP 3 |
| 예외 처리 규칙이 없음 | STEP 4 |
| 요구사항 자체가 모호함 | STEP 1 |

수정한 뒤에는 **STEP 5를 처음부터 다시 돌린다.** 고친 부분만 재확인하지 않는다.
