#!/usr/bin/env bash
# codex-critic.sh — C단계 미적·게슈탈트 판정을 Codex(별도 프로세스·별도 모델)에 위임한다.
#
# 왜 별도 프로세스인가: design-critic이 Claude 서브에이전트이면 "Claude가 만든 화면을 Claude가 검증"하는
# 구조가 되어 같은 모델의 판단 편향(자기 승인)을 벗어나지 못한다. Codex CLI를 별도 프로세스로 실행하면
# 생성(메인 Claude Code 세션)과 검증(별도 Codex 세션·별도 모델·별도 컨텍스트)이 완전히 분리된다.
#
# 사용법:
#   codex-critic.sh <brief.md 경로> <PRD 경로> <신규 화면 PNG 1개 이상> -- <소스 패턴 PNG 1개 이상>
#
# 예:
#   codex-critic.sh design/pettime/brief.md \
#     docs/pettime-PRD.md \
#     design/pettime/refs/screens-v3.png \
#     -- \
#     design/_rehearsal/refs/s1-lets-start.png design/_rehearsal/refs/s2-home.png
#
# 출력: SKILL.md C단계·report.md가 기대하는 고정 포맷 텍스트를 stdout으로 낸다.
# 종료 코드: 0 = PASS 파싱 성공, 1 = FAIL 파싱 성공, 2 = 실행 실패(재시도 대상 아님, 사람에게 에스컬레이션)

set -euo pipefail

BRIEF="$1"; shift
PRD="$1"; shift
NEW_IMAGES=()
while [[ "$1" != "--" ]]; do NEW_IMAGES+=("$1"); shift; done
shift # skip --
SRC_IMAGES=("$@")

if [[ ! -f "$BRIEF" ]]; then
  echo "ERROR: brief.md not found: $BRIEF" >&2
  exit 2
fi
if [[ ! -f "$PRD" ]]; then
  echo "ERROR: PRD not found: $PRD" >&2
  exit 2
fi
if [[ ${#NEW_IMAGES[@]} -eq 0 || ${#SRC_IMAGES[@]} -eq 0 ]]; then
  echo "ERROR: need at least one new-screen image and one source-pattern image" >&2
  exit 2
fi

PATTERN_SPEC=$(awk '/^## F\. 패턴 스펙/,/^## [A-Z0-9]\. /' "$BRIEF" | sed '$d')
if [[ -z "$PATTERN_SPEC" ]]; then
  PATTERN_SPEC="(brief.md에서 '## F. 패턴 스펙' 섹션을 찾지 못함 — brief.md 전체를 참고하라)"
fi

PRD_CONTENT=$(cat "$PRD")

PROMPT=$(cat <<EOF
너는 평가자다. 이 화면들을 만든 사람이 아니다. 판정과 원인 진단만 낸다. 코드나 파일을 고치지 않는다.

입력:
- 첨부 이미지 중 앞쪽 ${#NEW_IMAGES[@]}장은 "신규 화면"(이번에 새로 만든 서비스 화면), 뒤쪽 ${#SRC_IMAGES[@]}장은 "소스 패턴"(디자인 언어의 출처 화면)이다. 이미지 순서로 구분하라.
- 패턴 스펙(brief.md 발췌):
${PATTERN_SPEC}
- PRD 원문 전체:
${PRD_CONTENT}

절차:
1. PRD를 먼저 읽고 핵심 유저스토리·기능 요구사항·PRD가 명시한 엣지케이스를 파악한다.
2. 소스 화면을 전부 본다. 패턴 스펙 7항목(색/타이포/형태/간격/레이아웃 아키타입/장식/카피 톤)이 실제 소스 화면과 맞는지 확인하고, 다르면 "스펙 불일치"로 적는다.
3. 신규 화면을 하나씩 소스 화면과 나란히 놓고 본다. 동시에 신규 화면들만 가지고 PRD의 각 유저스토리를 처음부터 끝까지 실제로 수행할 수 있는지 시뮬레이션한다.
4. 마지막으로, 이 화면 세트를 "2000만원을 주고 외주로 맡긴 클라이언트" 입장에서 통째로 다시 본다. 위 1~3에서 이미 확인한 사실(패턴 정합성 여부, 플로우 완성 여부)을 이 관점의 판단 재료로 쓰되, 그것과 별개로 "이 정도 품질이면 이 값을 받을 자격이 있는가"를 독립적으로 판단한다 — 패턴·플로우가 기술적으로 PASS여도 마무리가 조잡하면 이 항목은 FAIL일 수 있다.

판정 항목 — 4개 모두 하드 게이트:

하드 1. 패턴 정합성 — "같은 회사가 만든 다른 서비스"로 보이는가. 근거는 반드시 구체 속성으로 적는다(주색 면적, 카드 라운드·그림자, 상단바 높이감, 리스트 셀 구조, 일러스트 스타일, 하단 네비 형태). 소스 도메인 단어가 신규 화면에 남아 있으면 즉시 실패.
하드 2. 시각적 위계 — 3초 안에 "무엇을 하라는 화면인지" 읽히는가. 첫 시선이 가는 요소와 CTA가 일치하는가.
하드 3. PRD 핵심 플로우 커버리지 — PRD의 핵심 유저스토리 각각에 대해, 지금 보여준 화면들만으로 "시작부터 끝까지 이 작업을 완료할 수 있는가"를 유저스토리별로 PASS/FAIL 판정한다. 화면이 몇 장 안 보여도 좋다 — 없는 화면을 만들어달라는 게 아니라, "보여준 것 안에서 이 플로우가 완결되는가"만 본다. PRD가 명시한 엣지케이스(예: 중복 소속, 늦은 회신, 겹치는 일정)가 화면 어딘가에서 실제로 처리된 근거가 있는지도 유저스토리 판정과 함께 적는다. 유저스토리 하나라도 화면상으로 완결이 안 보이면 이 항목 전체가 FAIL이다.
하드 4. 상업 퀄리티(클라이언트 관점) — 페르소나: 이 화면 세트를 2000만원을 주고 외주 제작사에 맡긴 클라이언트. "이대로 최종 인도물로 받아들이겠는가"를 PASS/FAIL로 판정한다. FAIL이면 구체적 결함을 최소 3가지 든다(예: "카드 그림자가 화면마다 강도가 달라 손 안 댄 티가 난다", "빈 상태 화면의 CTA 문구가 다른 화면들과 톤이 다르다", "리스트 셀 우측 여백이 화면별로 2~3px씩 어긋난다"). 근거는 스크린샷에서 실제로 보이는 것만 들고, 추측이나 일반론("더 세련되게" 같은 말)은 결함으로 인정하지 않는다. 결함이 정말 없으면 PASS와 그 근거(왜 이 정도면 값을 한다고 보는지)를 적는다.

리포트 5항목(각 PASS/WARN + 한 줄 근거): 색온도·조명 일관성 / 여백 리듬 / 정보 밀도 / 클리셰·AI슬롭(그라데이션 남용, 의미 없는 블롭, 과한 이모지, 동일 카드 반복, 아이콘·이미지 자리표시자 잔존) / 엣지케이스(빈 상태) 완성도.

실패 시 진단(하나만 고른다. 하드 게이트가 여러 개 FAIL이면 가장 근본적인 원인 하나를 고른다):
- 국소: 속성 하나만 바꾸면 통과. 그 속성과 값을 적는다. (하드 4 상업 퀄리티 FAIL의 전형적 원인 — 그림자 강도, 여백 오차 같은 마감 디테일.)
- 방향: 구조(IA, 컴포넌트 선택)가 문제. 어느 화면의 어느 섹션인지 적는다. (하드 3 플로우 커버리지 FAIL의 전형적 원인 — 화면 자체가 필요한 정보/액션을 담을 구조가 아닌 경우.)
- 반복: 이전 시도와 같은 이유로 실패했을 가능성. 요구사항 해석 문제일 수 있음을 적는다.

출력 형식(이것만 반환하라. 다른 텍스트를 앞뒤에 붙이지 마라):
## 판정: PASS | FAIL
### 하드
- 패턴 정합성: PASS/FAIL — 근거
- 위계: PASS/FAIL — 근거
- PRD 플로우 커버리지: PASS/FAIL — 유저스토리별 판정 + 엣지케이스 처리 근거
- 상업 퀄리티(클라이언트 관점): PASS/FAIL — 근거(FAIL이면 구체 결함 3가지 이상)
### 리포트
- 색온도: … / 여백: … / 밀도: … / 슬롭: … / 엣지케이스: …
### 진단: 국소 | 방향 | 반복 | 해당없음
- 화면/섹션/속성: …
- 권장 조치 한 줄: …
EOF
)

IMG_ARGS=()
for f in "${NEW_IMAGES[@]}" "${SRC_IMAGES[@]}"; do
  IMG_ARGS+=(-i "$f")
done

OUTPUT=$(codex exec "${IMG_ARGS[@]}" --sandbox read-only --skip-git-repo-check "$PROMPT" 2>&1)

# codex exec 출력에서 마지막 "codex" 블록(모델 응답)만 추출한다.
# 형식: 헤더들 다음 "codex\n<응답>\ntokens used\n<n>\n<응답 반복>" 순서로 나온다.
RESPONSE=$(echo "$OUTPUT" | awk '/^codex$/{c++; if(c==1){found=1; next}} found && /^tokens used$/{exit} found{print}')

if [[ -z "$RESPONSE" ]]; then
  echo "ERROR: Codex 응답 파싱 실패. 원본 출력:" >&2
  echo "$OUTPUT" >&2
  exit 2
fi

echo "$RESPONSE"

if echo "$RESPONSE" | grep -q "^## 판정: PASS"; then
  exit 0
elif echo "$RESPONSE" | grep -q "^## 판정: FAIL"; then
  exit 1
else
  echo "WARNING: 판정 라인을 찾지 못함 — 형식 위반. 사람이 직접 원문을 확인하라." >&2
  exit 2
fi
