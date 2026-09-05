---
name: planning-harness
description: PRD·RFP·구두 브리프를 받아 에이전시 납품 수준의 상위 기획 산출물(정의서·역할·IA·플로우·온보딩·정책·검증표·시드데이터)과 다음 하네스로 넘길 와이어프레임 입력 패키지를 생성하는 하네스. 사용자가 "기획해줘", "IA 짜줘", "화면 설계 전에 구조 잡아줘", "요구사항 정리해줘", "이 PRD로 기획 시작해줘", "온보딩 경로 잡아줘" 등을 요청하면 이 스킬을 사용한다. 도메인 무관 범용 구조이며, 화면설계서(스토리보드) 직전까지를 범위로 한다. 결과물은 ID 기반 구조화 문서 9종과, 그것을 `wireframe` 스킬 입력 형식(prd·user-flow·ia·constraints)으로 재구성한 패키지다.
---

# 상위 기획 하네스

PRD/RFP/브리프 → **화면설계서 직전까지**의 기획 산출물을 만든다.
레이아웃·컴포넌트·컬러·타이포는 이 하네스의 범위가 **아니다**. 여기서는 "무엇을, 누가, 어떤 순서로, 어떤 규칙 아래" 까지만 확정한다.

## 범위 경계

| 이 하네스가 한다 | 하지 않는다 (다음 하네스) |
|---|---|
| 벤치마킹·레퍼런스 조사 (ui bowl) | 컬러·타이포·레이아웃 디테일 |
| 문제·스코프 정의 | 화면 레이아웃 |
| 역할·권한 | 컴포넌트 설계 |
| 정보구조·엔티티·화면목록 | 컬러·타이포·디자인 시스템 |
| 유저 플로우·상태 전이 | Figma 파일 생성 |
| 온보딩 경로 (첫 진입 → 첫 가치) | 코치마크·툴팁·튜토리얼 문구 |
| 정책(예외·권한·데이터) | 퍼블리싱·개발 |
| 커버리지 검증 | 클라이언트 제출용 PPT·PDF 렌더링 |
| 다음 하네스용 입력 패키지 변환 | 와이어프레임·화면 렌더링 자체 |

## 입력

1. `config/project-profile.yaml` — 없으면 `config/project-profile.template.yaml`을 복사해 사용자와 함께 채운다.
2. 원본 요구자료 (PRD·RFP·회의록·구두 브리프). 형식 무관.

입력이 부실해 임의로 지어내야 할 상황이면 **즉시 멈추고** `references/interview.md`를 읽어 질문한다. 추측으로 채우지 않는다.

## 공통 실행 규칙

- **ID를 반드시 부여한다.** 규칙은 `references/id-convention.md`를 STEP 1 시작 전에 1회 읽는다. 이후 모든 산출물은 산문 대신 ID로 상호참조한다.
- **한 스텝에 한 참조 파일만 읽는다.** 스텝 진입 시 해당 `references/stepN-*.md`를 읽고, 끝나면 다음 스텝 파일을 읽는다. 미리 몰아서 읽지 않는다.
- **템플릿을 복사해서 채운다.** `templates/`의 뼈대를 벗어나 임의로 섹션을 추가·삭제하지 않는다. 스키마가 스크립트 검증 기준이기 때문이다.
- **모르는 것은 `TBD:` 로 남긴다.** 예: `TBD: 결제 수단 범위 — 클라이언트 확인 필요`. 지어낸 확정 문장보다 명시된 미결이 낫다. 모든 `TBD:`는 `_handoff.md`에 모아 보고한다.
- **출력 언어는 한국어.** ID·필드명·파일명만 영문.

## 실행 순서

각 스텝은 앞 스텝 산출물이 존재해야 시작한다. 건너뛰지 않는다.

| STEP | 읽을 파일 | 산출물 |
|---|---|---|
| 0 | `config/project-profile.template.yaml` | `project-profile.yaml` |
| 1 | `references/step1-definition.md` | `definition.md`(벤치마킹 포함), `users.md` |
| 2 | `references/step2-ia.md` | `ia.yaml` |
| 3 | `references/step3-flows.md` | `flows.yaml` |
| 4 | `references/step4-onboarding.md` | `onboarding.yaml` |
| 5 | `references/step5-policy.md` | `policy.md` |
| 6 | `references/step6-validation.md` | `validation.csv` |
| 7 | `references/step7-seed.md` | `seed-data.json`, `_handoff.md` |
| 8 | `references/step8-wireframe-input.md` | `{wireframe_input_dir}/` 패키지 5종 |

출력 위치: `{프로젝트명}/01-planning/` (STEP 8 패키지만 `project-profile.yaml`의 `output.wireframe_input_dir`, 기본 `wireframes/input/`)

STEP 4(온보딩)는 화면(STEP 2)과 플로우(STEP 3)를 첫 진입 순서로 꿰는 스텝이다. 여기서 "온보딩 첫 단계가 참조할 화면이 없다"가 발견되면 STEP 2로 돌아가 화면을 추가하고 다시 온다.

STEP 8(와이어프레임 입력 패키지)은 STEP 1~7이 만든 9종을 다음 하네스인 `wireframe` 스킬이 읽는 형식으로 **변환**하는 스텝이다. 새 정보를 만들지 않고 ID도 다시 매기지 않는다. 다음 단계가 화면 설계가 아니면 건너뛸 수 있다.

## STEP 6 검증 루프 (필수)

STEP 6은 통과할 때까지 반복한다. LLM 자체 판단만으로 "문제없음"이라고 결론내지 않는다.

```bash
python scripts/validate_ids.py   {프로젝트명}/01-planning
python scripts/check_coverage.py {프로젝트명}/01-planning
```

- `validate_ids.py` 실패 → 깨진 참조가 있는 스텝으로 되돌아가 수정
- `check_coverage.py` 실패 → 미커버 요구사항은 STEP 2(화면 추가)·STEP 3(플로우 추가)으로, 온보딩 경로 누락·필수 단계 근거 없음은 STEP 4로 되돌아감
- 스크립트 실행 환경이 없으면 `references/step6-validation.md`의 수동 체크리스트를 대신 수행하되, 수동 수행했음을 `_handoff.md`에 명시한다

되돌아가 수정한 뒤에는 **STEP 6을 처음부터 다시 돌린다.** 부분 재검증은 하지 않는다.

## STEP 8 패키지 검사 (필수)

```bash
python scripts/check_wireframe_input.py {프로젝트명}/01-planning {wireframe_input_dir}
```

- 파일 5종 존재, 절 제목 보존, `REQ`·`ROLE`·`SCR`·`ONB` 누락 없음, 신규 ID 생성 없음, `RISK-01`~`12` 전부 존재, 자리표시자 잔존 없음을 본다
- 누락 ID가 상위기획 쪽 오류라면 STEP 8이 아니라 해당 스텝으로 되돌아간다
- 실행 환경이 없으면 `references/step8-wireframe-input.md`의 자체 점검을 손으로 수행하고, 수동이었음을 `_handoff.md`에 적는다

## 품질 기준선

산출물의 밀도·문장 수준이 헷갈리면 `examples/wedding-scheduler/`를 참고한다.
이 예시보다 얕으면 납품 수준이 아니다.

## 완료 보고

작업 종료 시 사용자에게 다음을 요약한다.

1. 생성된 파일 목록과 경로
2. 화면 수·플로우 수·엔티티 수·온보딩 경로 수
3. 벤치마킹으로 조사한 서비스 수와 출처 (미수행이면 사유)
4. `references/risk-patterns.md` 12패턴 중 이 프로젝트에 해당한 것과 대응 화면
5. 역할별 온보딩 경로(`ONB-`)와 각 경로의 첫 가치 화면, 필수 단계 수
6. 남은 `TBD:` 전체 목록 (클라이언트 확인 필요 사항)
7. STEP 8 패키지 경로와 `check_wireframe_input.py` 결과
8. 다음 하네스 호출 문장 (패키지 `README.md`의 "실행 방법" 그대로)
9. 다음 하네스로 넘어갈 때의 주의점
