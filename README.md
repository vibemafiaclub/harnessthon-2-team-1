# oss-design-harness

**Figma 디자인 패턴(또는 디자인 시스템 문서) + PRD → 같은 디자인 언어의 새 서비스 화면을 Figma에 생성하고, 구조·시각 검증까지 마치는 하네스.**

VIBE MAFIA CLUB 하네스톤 2회차(2026-09-05)를 계기로 만든 오픈소스 프로젝트입니다.

## 이 하네스가 하는 일

**입력**: (Figma 패턴 파일 URL **또는** 디자인 시스템 문서, 예: `docs/design.md`) + PRD(미확정 항목 포함 가능) + 출력 Figma 파일 URL
**출력**: 출력 파일 새 페이지에 생성된 화면 세트(`Library`·`Screens/<project>`·`Presentation`) + `projects/<project>/` 산출물(brief/decisions/report) + (선택) 클릭 가능한 웹 데모 Artifact 링크

운전자는 **디자인 비전문가**라고 가정합니다. 하네스는 그림(스크린샷·클릭 가능한 로우파이)으로 보여주고, 모든 질문에 추천 기본값을 붙이고, "그냥 알아서"라고 답해도 끝까지 결과물을 냅니다.

## 프레임워크 — 판단 구조

디자이너가 일하는 **순서**를 그대로 흉내내지 않습니다. 각 단계가 실제로 하려던 일(**판단 기준**)만 뽑아서, 에이전트가 잘하는 방식(병렬 생성, 다각도 교차 비평, 프로세스 분리 검증)으로 다시 구현합니다.

| 단계 | 시점 | 하는 일 |
|---|---|---|
| **P. PRD 인테이크** | 만들기 전 | PRD를 화면·기능·엔티티·미확정 항목으로 분해. 미확정은 확정/가정/열림으로 분류, 열림만 질문(최대 5개). |
| **F. 패턴 추출 / 문서 승계** | 만들기 전 | Figma 패턴이면 `pattern-extractor` 서브에이전트가 유형 진단 + 디자인 언어 9항목을 추출. 디자인 시스템 문서가 이미 있으면 재추출 없이 그대로 승계. |
| **0. 요구사항 정렬** (조건부) | 패턴/문서가 없거나 못 덮을 때 | 레퍼런스 보드 또는 클릭 가능한 로우파이를 보여주고 좋다/싫다+이유로 암묵 기준을 역추출. 라벨형 질문 금지. |
| **B. 발산·수렴** | 정답이 여러 개일 때 | 이미 정해진 축(색·타이포·형태·장식·카피 톤)은 잠그고, IA와 기능↔컴포넌트 매핑 2축만 후보 2개씩. 도메인 전이 표 작성. |
| **G. 생성** | 만드는 중 | 인스턴스로 1차 조립(=이 하네스의 와이어프레임) → 스크린샷 검토 → 마감(활성 탭·빈 상태·장식 절제) → 프레젠테이션 페이지. |
| **A. 구조적 사실 검증** | 만든 후 | 컴포넌트 재사용률·토큰 준수·도메인 단어 잔존 3개 하드 게이트 + 리포트 3개. |
| **C. 미적·게슈탈트 판단** | 만든 후 | **Codex CLI**(별도 프로세스·별도 모델)가 소스·PRD 원문과 함께 보고 4개 하드 게이트를 판정: 패턴 정합성, 시각적 위계, **PRD 핵심 플로우 커버리지**(유저스토리별로 이 화면들만으로 완결되는지), **상업 퀄리티**(2000만원 외주 클라이언트가 인도물로 받아들일지, 냉정하게). Codex 미가용 시에만 `design-critic` 서브에이전트로 폴백. 실패 시 국소/방향/반복 진단 → 즉시 조치 → 재검사로 이어지는 자동 재시도 루프(상한 2회, 초과 시 사람 에스컬레이션). |
| **W. 웹 배포** (선택) | CP4 통과 후 | 확정된 화면을 HTML/CSS로 이식해 Artifact로 publish — 클릭 가능한 웹 데모 링크를 Figma 링크와 함께 제공. |

사람 체크포인트 4곳(요구사항 되읽기 → 시안 보드 → 와이어프레임 검토 → 최종 확인)에서만 멈춥니다. 최종 판단은 항상 사람이 내립니다.

## 왜 검증을 Codex로 분리하는가

이 하네스로 화면을 만드는 것은 Claude Code(메인 세션)입니다. C단계 판정을 Claude 서브에이전트로 하면 "만든 모델이 자기 결과를 검증"하는 구조가 되어 같은 모델 특유의 판단 편향을 벗어나지 못합니다. `scripts/codex-critic.sh`가 Codex CLI를 별도 프로세스로 호출해, 화면을 만드는 과정을 전혀 모르는 다른 모델이 결과물만 보고 판정하게 합니다.

## 서브에이전트 3개

| 에이전트 | 역할 | 쓰기 권한 |
|---|---|---|
| `pattern-extractor` | 소스 Figma 패턴의 F1(유형 진단)·F2(디자인 언어 9항목 추출) | 없음(읽기 전용) |
| `ref-scout` | 외부 레퍼런스(App Store/Play, Mobbin 등) 조사·캡처 | 이미지 파일만 |
| `design-critic` | C단계 판정의 **폴백**(Codex CLI 미가용 시에만) | 없음(판정만) |

## 구조

```
CLAUDE.md                                          # 운전자 전제·체크포인트·서브에이전트 정책·Figma 규칙·시간 예산
.claude/skills/oss-design-harness/SKILL.md         # 하네스 본체 — P/F/0/B/G/A/C 절차 + CP 4곳
.claude/skills/oss-design-harness/templates/       # brief.md, decisions.md, report.md, reference-board.html
.claude/skills/oss-design-harness/references/figma-snippets.md   # 검증된 use_figma 코드 스니펫
.claude/skills/oss-design-harness/scripts/codex-critic.sh        # C단계 정식 검증 — Codex CLI 호출
.claude/agents/pattern-extractor.md                # F1·F2 서브에이전트 (신규 Figma 패턴 조사)
.claude/agents/ref-scout.md                        # 외부 레퍼런스 조사·캡처 서브에이전트
.claude/agents/design-critic.md                    # C단계 평가 서브에이전트 (Codex 폴백)
docs/concept.md                                    # 컨셉 스펙 전문 (배경·경쟁 포지셔닝·논리 검증 과정)
docs/design.md                                     # (예시) 디자인 시스템 문서 — F단계 문서 승계 경로의 입력
projects/<project>/                                # 실행 산출물 (brief, decisions, report, refs/, board.html)
```

## 사용법

1. (Figma 패턴 파일 또는 디자인 시스템 문서) + PRD + 출력 Figma 파일을 준비한다. 이 레포를 프로젝트 루트로 Claude Code를 실행한다.
2. 아래처럼 시작한다.
   ```
   이 Figma 패턴으로 PRD 화면 만들어줘. 패턴: <URL>, PRD: <경로 또는 본문>, 출력: <URL>
   ```
   또는 디자인 시스템 문서가 이미 있으면:
   ```
   docs/design.md 참고해서 PRD 화면 만들어줘. PRD: <경로>, 출력: <URL>
   ```
3. 체크포인트 4곳에서 답한다. 모르면 "추천대로"라고 답하면 된다.
4. 결과는 출력 파일의 `Library`, `Screens/<project>`, `Presentation` 페이지와 `projects/<project>/`에 남는다.

## 라이선스

MIT — [LICENSE](./LICENSE)
