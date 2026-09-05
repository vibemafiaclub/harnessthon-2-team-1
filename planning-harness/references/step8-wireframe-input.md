# STEP 8 — 와이어프레임 입력 패키지

산출물: `{wireframe_input_dir}/README.md`, `prd.md`, `user-flow.md`, `ia.md`, `constraints.md`
템플릿: `templates/wireframe-input/`
기본 출력 위치: `wireframes/input/` (`project-profile.yaml`의 `output.wireframe_input_dir`로 바꿀 수 있다)

## 이 스텝이 필요한 이유

STEP 1~7이 만든 9종은 **상위기획팀이 읽는 형식**이다. 다음 하네스인 `wireframe` 스킬은 다른 형식을 요구한다.

| `wireframe` 스킬이 요구하는 것 | 이 하네스가 가진 것 |
|---|---|
| PRD 1개 문서 | `definition.md` + `users.md` + 원본 요구자료 |
| User Flow 1개 문서 | `flows.yaml` + `onboarding.yaml` |
| IA 1개 문서 | `ia.yaml` + `validation.csv` |
| 제약사항·출력 매체 | `project-profile.yaml` 여기저기 |
| Dummy Content | `seed-data.json` (원본 그대로는 너무 큼) |
| 가정 로그 | 전 산출물에 흩어진 `TBD:` |

이 간극을 사람이 매번 손으로 메우면 그때마다 다르게 메워진다. STEP 8이 그 변환을 고정한다.

## 대원칙 — 변환이지 재기획이 아니다

- **새 정보를 만들지 않는다.** 패키지에 들어가는 모든 문장은 STEP 1~7 산출물이나 원본 요구자료에 근거가 있어야 한다.
- **ID를 다시 매기지 않는다.** `REQ-07`은 패키지에서도 `REQ-07`이다. 번호가 바뀌면 다음 하네스가 상위기획 문서를 역참조할 수 없다.
- **`TBD:`를 지우지 않는다.** 미결은 미결로 넘긴다. 넘기면서 "어느 화면이 이 결정에 걸려 있는지"를 붙인다.
- **화면 설계에 쓰이지 않는 것은 뺀다.** 상위기획 내부 논의, 스텝 간 되돌아간 이력, 스크립트 실행 로그는 패키지에 넣지 않는다.
- **요약본이 아니라 재구성이다.** 분량을 줄이는 게 목적이 아니다. 같은 내용을 다음 하네스가 읽는 순서로 다시 배열하는 것이다. 원본보다 얕아지면 실패다.

빠뜨린 것이 있으면 다음 하네스는 그것을 **상상해서 채운다.** 그러면 STEP 6까지 지킨 커버리지가 무의미해진다.

## 변환 매핑

이 표대로 채운다. 소스가 없는 절은 비워두지 말고 `TBD:`로 남긴다.

| 파일 | 절 | 소스 | 변환 |
|---|---|---|---|
| `prd.md` | 1 배경 | `definition.md` | 그대로. 도메인을 처음 보는 사람 기준으로 |
| | 2 목표 | `definition.md` | 그대로 |
| | 3 핵심 유저 스토리 | 원본 요구자료, `users.md` | 화면 구조에 영향 주는 것만 |
| | 4 사용자 상황 | `definition.md`, `project-profile.yaml` `data_scale` | 규모·빈도·예외를 숫자로 |
| | 5 사용자 역할 | `users.md` | ROLE 표 + 권한 대칭 여부 산문 |
| | 6 스코프 | `definition.md` | 포함 / 제외(근거 포함) / 보류(TBD) |
| | 7 기능 요구사항 | `definition.md` | REQ 표 그대로 |
| | 8 비기능 요구사항 | `definition.md` | NFR 표 그대로 |
| | 9 성공 기준 | `definition.md` | |
| | 10 평가 기준 | 원본 요구자료 | 심사·검수 기준이 있을 때만 |
| `user-flow.md` | 1 핵심 경로 | `flows.yaml`, `onboarding.yaml` | 역할군별로 `진입 → 입력 → 처리 → 결과 → 다음 행동` 5단 |
| | 2 상태 전이 | `flows.yaml` `states`·`transitions` | ST 표 + 전이 표 + 검토 포인트 3종 |
| | 3 유저 플로우 | `flows.yaml` `flows` | FLW별 트리거·단계표·결과·예외 |
| | 4 역할별 플로우 매핑 | `flows.yaml`, `users.md` | |
| | 5 온보딩 경로 | `onboarding.yaml` | ONB 요약표 + 경로별 단계표 |
| `ia.md` | 1 엔티티 | `ia.yaml` `entities` | 엔티티 표 + 관계 표 |
| | 2 화면 목록 | `ia.yaml` `screens` | SCR 표. 목적은 한 문장 |
| | 3 화면별 정보·행동·상태 | `ia.yaml`, `policy.md`, `validation.csv` | 화면당 한 블록 |
| | 4 내비게이션 구조 | `ia.yaml` `navigation` | 역할군별 트리 |
| | 5 커버리지 | `validation.csv` | REQ → SCR → FLW 요약 |
| `constraints.md` | 1 제약사항 | `project-profile.yaml`, NFR, `policy.md` | 플랫폼·너비·출력 매체·데이터 규모 |
| | 2 권한 정책 | `users.md`, `policy.md` | 행동 × 역할 매트릭스 |
| | 3 상태·예외 정책 | `policy.md` | 화면을 바꾸는 것만 |
| | 4 데이터 정책 | `policy.md` | |
| | 5 알림 정책 | `policy.md` | |
| | 6 리스크 패턴 | `validation.csv`, `references/risk-patterns.md` | 12패턴 전부 |
| | 7 화면별 주의점 | `_handoff.md` 7절 | |
| | 8 더미 콘텐츠 소스 | `seed-data.json` | 요약 + 필수 케이스 |
| | 9 가정 로그 초안 | 전 산출물 `TBD:`, `_handoff.md` 6절 | |
| `README.md` | 전체 | 위 4개, `_handoff.md` | 매핑표·실행법·화면 범위 참고·미결 |

### 벤치마킹은 아직 넘기지 않는다

`definition.md` §3 벤치마킹은 현재 패키지로 옮기지 않는다. 상위기획 내부 자료로만 둔다.
넘기기로 결정하면 네 곳을 함께 고쳐야 한다 — `prd.template.md`의 절, 위 매핑표, `scripts/check_wireframe_input.py`의 `REQUIRED_SECTIONS`, `tests/fixture-wf-*`의 `prd.md`. 절 목록이 하드코딩이라 한 곳만 고치면 테스트가 깨진다.

## 절대 빠뜨리면 안 되는 다섯

다음 하네스가 이것 없이는 화면을 못 그린다. 하나라도 없으면 STEP 8을 다시 한다.

1. **출력 매체** (`constraints.md` §1) — Figma인지 HTML인지. 없으면 스킬이 임의로 고른다
2. **기준 너비** (`constraints.md` §1) — 없으면 375pt가 기본값이라고 명시라도 한다
3. **화면별 State** (`ia.md` §3) — Empty·Error·Partial이 없으면 Default 화면만 그려진다
4. **더미 콘텐츠 필수 케이스** (`constraints.md` §8) — 없으면 "홍길동1, 홍길동2"가 들어간다
5. **가정 로그** (`constraints.md` §9) — 없으면 미결이 확정으로 둔갑한다

## 온보딩(STEP 4) 처리

`wireframe` 스킬의 입력 항목에는 온보딩 칸이 따로 없다. 그렇다고 버리면 "첫 진입 화면을 무엇으로 그릴지"가 사라진다. 두 곳으로 나눠 넣는다.

- `user-flow.md` §5 — ONB 경로 전체 (진입 상태, 필수 단계, 첫 가치 화면, 완료 조건)
- `ia.md` §2·§3 — 온보딩 때문에 추가된 화면(가입·시작 설정 등)도 다른 화면과 똑같이 목록과 블록에 넣는다

온보딩 경로가 여럿이고 첫 화면이 서로 다르면, `README.md`의 "화면 범위에 대한 참고"에 그 사실을 적는다.

## 검증

```bash
python scripts/check_wireframe_input.py {프로젝트명}/01-planning {wireframe_input_dir}
```

검사 항목은 다섯이다.

1. 파일 5종이 모두 있는가
2. 템플릿의 절 제목이 모두 살아 있는가 (임의 삭제 금지)
3. 상위기획의 `REQ`·`SCR`·`ROLE`·`ONB`가 패키지에서 하나도 누락되지 않았는가
4. 상위기획에 없는 ID를 패키지가 새로 만들지 않았는가
5. `RISK-01`~`RISK-12`가 `constraints.md`에 전부 있고, 채우지 않은 템플릿 자리표시자(`SCR-NN`, `{프로젝트명}`, `<!-- -->`)가 남아 있지 않은가

실패하면 해당 파일을 고치고 다시 돌린다. 3번이 실패했는데 상위기획 쪽이 틀린 것이라면 STEP 8이 아니라 그 스텝으로 되돌아간다.

스크립트를 못 돌리는 환경이면 위 다섯을 손으로 확인하고, 수동 확인이었음을 `_handoff.md` 8절에 적는다.

## 자체 점검

- [ ] 패키지 5개 파일이 `{wireframe_input_dir}/`에 있는가
- [ ] 템플릿의 HTML 주석(`<!-- -->`)을 전부 지웠는가
- [ ] `{프로젝트명}` 같은 자리표시자가 남아 있지 않은가
- [ ] `prd.md`만 읽고 도메인을 모르는 사람이 무슨 서비스인지 이해할 수 있는가
- [ ] `user-flow.md` §1의 핵심 경로가 `진입 → 입력 → 처리 → 결과 → 다음 행동` 5단을 지키는가
- [ ] `ia.md` §2의 모든 화면에 목적이 한 문장으로 적혀 있는가
- [ ] `constraints.md` §1의 출력 매체와 기준 너비가 확정값 또는 명시된 기본값인가
- [ ] `constraints.md` §9 가정 로그가 전 산출물의 `TBD:`를 하나도 빠뜨리지 않았는가
- [ ] 패키지 5개 파일 밖의 문서를 읽지 않고도 `wireframe` 스킬 1단계를 시작할 수 있는가
