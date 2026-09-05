# oss-design-harness — 오케스트레이터

이 레포는 **PRD → IA/기획 → 와이어프레임 → Figma 모바일 화면 생성 → 리뷰**를 에이전트 4개로 수행하는 디자인 하네스다.
**코드 프로젝트가 아니다.** `package.json`·`src/`·빌드·Storybook이 없다. 홈 디렉토리 `~/CLAUDE.md`의 React/Storybook/`npm run build` 규칙은 이 레포에 적용하지 않는다.
방향은 **기획 → Figma 생성**(`use_figma`로 작업장에 노드를 만든다)이지, Figma → 코드가 아니다.

## 프로젝트 상수

| 키             | 값                                                                              |
| -------------- | ------------------------------------------------------------------------------- |
| Figma 파일     | `https://www.figma.com/design/dyqBJHi5EN92veBmDgLjx8/design?node-id=14-60`      |
| fileKey        | `dyqBJHi5EN92veBmDgLjx8`                                                        |
| 작업 기준 노드 | `14:60` (빈 파일. 03-builder가 첫 실행 시 종류를 확인하고 페이지 구조를 잡는다) |
| 플랫폼         | **모바일 앱 고정** — 프레임 390×844, `design.md` 부록 A                         |
| 디자인 가이드  | `design.md` (읽기 전용. 에이전트는 부록 C 범위만 결정)                          |
| 입력 PRD       | 사용자가 지정. 기본값 `청첩장모임-스케줄러-PRD.md`                              |
| 언어           | 산출물·UI 문구 모두 한국어                                                      |

## 파이프라인

```
PRD ──▶ [01-planner] ──▶ 게이트 1 ──▶ [02-wireframer] ──▶ 게이트 2 ──▶ [03-figma-builder: Foundations] ──▶ 게이트 3
                                                                        │
                                              화면마다 반복 ◀───────────┘
                                              [03-figma-builder: Screen] ──▶ [04-reviewer] ──▶ PASS → 다음 화면
                                                                                            ├─ FIX-LOCAL → 03 (같은 화면 국소 수정, 최대 3회)
                                                                                            ├─ REDIRECT-B → 02 (해당 화면 와이어 재발산) → 게이트
                                                                                            └─ ESCALATE-0 → 사람에게 보고 (01 재실행 여부 결정)
                                              전 화면 완료 ──▶ 최종 보고 (Figma 링크 + work/reviews/ 요약)
```

### 파일 핸드오프 (에이전트끼리 대화로 넘기지 않는다 — 파일로 넘긴다)

| 파일                                                          | 생산자            | 소비자   |
| ------------------------------------------------------------- | ----------------- | -------- |
| `work/brief.md`                                               | 01                | 02, 04   |
| `work/ia.md`                                                  | 01                | 02       |
| `work/decisions.md`                                           | 01, 02 (이어쓰기) | 04, 사람 |
| `work/mock-data.json`                                         | 02                | 03       |
| `work/wireframes/_index.md`, `work/wireframes/{screen-id}.md` | 02                | 03, 04   |
| `work/figma-log.md`                                           | 03 (append)       | 04, 사람 |
| `work/reviews/{screen-id}.md`                                 | 04                | 03, 사람 |

`work/`는 실행 산출물이다. 새 프로젝트를 시작하면 `work/`를 비우거나 `work-{프로젝트명}/`으로 이름을 바꾼다.

## 게이트 규칙 (사람이 디자인 비전문가여도 답할 수 있어야 한다)

모든 게이트는 아래 형식으로만 묻는다. **자유서술을 요구하지 않는다.** `AskUserQuestion`을 쓸 수 있으면 쓴다.

```
[게이트 N: 무엇을 결정하는지 한 줄]

A. (추천) ... — 왜 추천하는지 한 줄
B. ... — A와 무엇이 다른지 한 줄
C. ... — A와 무엇이 다른지 한 줄

모르겠으면 A를 고르세요. 이 결정은 나중에 바꿀 수 있습니다/없습니다.
```

- 게이트 1 (IA): 네비게이션 구조 대안 중 선택 + 화면 목록 확인
- 게이트 2 (와이어프레임): 화면별 ASCII 스케치 확인, 화면 추가/삭제 여부
- 게이트 3 (Foundations): Figma에 생성된 변수·스타일·컴포넌트 스크린샷 확인
- 그 외에는 사람을 부르지 않는다. 리뷰어의 `ESCALATE-0`, 재시도 상한 초과, Figma MCP 오류 3회 연속만 예외.
- 사용자가 "auto" 또는 "게이트 없이"라고 하면 게이트 1~3에서 추천안(A)을 자동 선택하고 `work/decisions.md`에 "자동 선택"으로 기록한다.

## 실행 규칙

1. **Figma MCP 호출은 반드시 서브에이전트(03, 04)에서만** 한다. 오케스트레이터 컨텍스트에 `use_figma`/`get_screenshot` 응답을 들이지 않는다.
2. 각 에이전트는 시작 시 `design.md`와 자기 입력 파일을 읽고, 끝날 때 산출물 파일을 쓴 뒤 **파일 경로 + 5줄 이내 요약**만 보고한다.
3. 03-builder는 **한 번의 호출에 화면 1개**만 만든다. Foundations는 별도 호출.
4. 03-builder는 자기가 이번 실행에서 만든 노드 외에는 수정·삭제하지 않는다. 실패 시 자기 노드를 삭제하고 재생성한다.
5. 04-reviewer는 `work/reviews/{screen-id}.md`에 판정(`PASS` / `FIX-LOCAL` / `REDIRECT-B` / `ESCALATE-0`)과 근거를 남긴다. 같은 화면 `FIX-LOCAL` 3회 → `REDIRECT-B`로 승격. `REDIRECT-B` 2회 → `ESCALATE-0`.
6. 에이전트가 `design.md` 본문과 충돌하는 결정을 해야 하는 상황이면 멈추고 사람에게 보고한다. 부록 C 표 밖의 결정은 하지 않는다.
7. 오케스트레이터는 각 단계 전환 시 사용자에게 **현재 단계 / 다음 단계 / 남은 화면 수**를 한 줄로 알린다.
8. **상태바는 생략 불가.** 03-builder가 만드는 모든 화면 프레임(`--empty` 등 상태 프레임, 모달 포함)은 Foundations `status-bar` 컴포넌트 인스턴스를 첫 자식(`x 0 / y 0`, 390×47)으로 갖는다(`design.md` A-1-1). 자체 프레임·텍스트·벡터로 그리지 않는다. 03은 자체 검증에서, 04는 A11에서 확인하며, 누락된 화면은 리뷰로 보내지 않고 03이 먼저 넣는다. 오케스트레이터는 03에게 화면 지시를 보낼 때 이 규칙을 매번 명시한다.

## 트리거

- "PRD로 시작", "하네스 돌려", "{파일}로 디자인 만들어" → 파이프라인 처음부터
- "{screen-id} 다시" → 03→04 해당 화면만
- "리뷰만" → 04만
- "Foundations만" → 03 Foundations 모드만

## 에이전트

| 에이전트         | 파일                                 | 역할                                                           |
| ---------------- | ------------------------------------ | -------------------------------------------------------------- |
| 01-planner       | `.claude/agents/01-planner.md`       | 0단계 가정·판단기준 + IA/상위기획, 대안 2~3개                  |
| 02-wireframer    | `.claude/agents/02-wireframer.md`    | 화면별 와이어프레임 스펙 + 목데이터                            |
| 03-figma-builder | `.claude/agents/03-figma-builder.md` | Foundations(변수·스타일·컴포넌트) 및 화면을 `use_figma`로 생성 |
| 04-reviewer      | `.claude/agents/04-reviewer.md`      | A(구조 검증) + C(스크린샷 심미 검증) + 라우팅                  |

판단 기준 체크리스트 원본: `.claude/skills/oss-design-harness/SKILL.md`. 04-reviewer는 이 파일을 읽고 검사한다.
