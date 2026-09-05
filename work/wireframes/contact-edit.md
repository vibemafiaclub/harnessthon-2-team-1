# contact-edit — 지인 등록·수정

## 목적

이름·연락처·소유자·관계 그룹(복수 선택)·`따로 만나기`를 한 화면에서 등록·수정한다. PRD §4-1 ("한 사람을 여러 그룹에 동시에 소속").

## 진입 / 이탈

- 진입: `contacts-list` 헤더 "추가"(신규 모드) / `contacts-list` 지인 행(수정 모드, 03은 수정 모드 p03으로 만든다) / `contacts-list` 빈 상태 버튼(신규 모드)
- 이탈:
  - 헤더 좌 뒤로가기 → `contacts-list` (변경 폐기)
  - 스티키 CTA "저장" → `contacts-list`
  - 스티키 좌 "저장하고 한 명 더"(신규 모드만) → 같은 화면 신규 모드 (필드 비움, 소유자·그룹 선택은 유지)
  - 블록 7 "이 지인 삭제"(수정 모드만) → `contacts-list`
  - 블록 5 "새 그룹 만들기" → 같은 화면, 블록 5에 `{component.input}` 1줄이 열림 (상태 `new-group`)

## 프레임

- 390 × 콘텐츠 높이 (약 1,000). 세로 스크롤.
- 헤더: `{component.mobile-header}` — 좌: `{component.button-icon-circular}`(32px, chevron.left) / 우: 없음
- 하단: `{component.mobile-sticky-cta}` — 좌: 요약 body "신부 · 그룹 2개" (`sideLabel` + " · 그룹 " + 선택 그룹 수 + "개"), 우: `{component.button-primary}` "저장". 신규 모드는 좌가 `{component.text-link}` "저장하고 한 명 더"로 바뀜 (조합: sticky-cta + text-link)

## 레이아웃 스택 (위→아래)

| #   | 블록        | 컴포넌트 키                                                                  | 내용 (mock-data 경로)                                                                                                                                         | 비고                                                                                                                                                                 |
| --- | ----------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | 화면 제목   | `{typography.display-md}`                                                    | "지인 수정" (신규 모드: "지인 추가")                                                                                                                          |                                                                                                                                                                      |
| 2   | 이름        | `{typography.caption}` 라벨 + `{component.input}`                            | 라벨 "이름" / 값 `people[p03].name` "박민아"                                                                                                                  | 라벨은 `{colors.ink-muted-48}`, 라벨-입력 사이 `{spacing.xs}`. 필드 간 `{spacing.lg}`                                                                                |
| 3   | 연락처      | 라벨 + `{component.input}`                                                   | 라벨 "연락처" / 값 `people[p03].contact` "010-4460-1192"                                                                                                      | 키보드 숫자                                                                                                                                                          |
| 4   | 소유자      | 라벨 + `{component.status-chip}` × 3                                         | 라벨 "누구의 지인인가요" / "신부"(selected) "신랑" "공동"                                                                                                     | 단일 선택. "공동" 선택 시 블록 5에 양측 그룹 8개가 모두 뜸                                                                                                           |
| 5   | 관계 그룹   | 라벨 + `{component.status-chip}` × N (줄바꿈 wrap) + `{component.text-link}` | 라벨 "관계 그룹 · 여러 개 고를 수 있어요" / `groups[side == "bride"]`: "대학 동기"(selected) "직장 동료"(selected) "동네 친구" "가족" / 링크 "새 그룹 만들기" | 복수 선택. 선택 = 2px `{colors.primary-focus}` 테두리. 칩 간 `{spacing.xs}`, 줄 간 `{spacing.xs}`. 선택 0개여도 저장 가능                                            |
| 6   | 관계 메모   | 라벨 + `{component.input}`                                                   | 라벨 "관계 메모" / 값 `people[p03].relation` "대학 동기 · 현재 같은 회사"                                                                                     | 자유 텍스트 1줄. 목록 행 caption으로 그대로 노출됨                                                                                                                   |
| 7   | 따로 만나기 | `{component.list-row}` + 우측 `{component.status-chip}` × 2                  | 제목 "따로 만나기" / 메타 "다른 사람과 같은 모임에 넣으면 알려 드려요" / 우: "아니요"(selected) "네"                                                          | `people[p03].separateOnly == false` → "아니요" selected. p31·p14는 "네". 토글 컴포넌트가 없어 칩 2개 단일 선택으로 조합. 행 하단 hairline 유지                       |
| 8   | 메모        | 라벨 + `{component.input}`                                                   | 라벨 "메모 (나만 보기)" / 값 `people[p03].note` "대학 동기이면서 지금 같은 팀 동료. 어느 모임에 넣을지 애매"                                                  | 2줄까지 늘어나는 입력 (높이 44 → 72)                                                                                                                                 |
| 9   | 삭제        | `{component.text-link}`                                                      | "이 지인 삭제"                                                                                                                                                | 수정 모드만. 중앙 정렬, 위 `{spacing.xl}`. 탭 시 같은 자리에 caption "정말 삭제할까요?" + `{component.button-secondary-pill}` "삭제" 로 바뀜 (상태 `confirm-delete`) |

## 상태

- default (수정 모드, p03): 위 스택
- new (신규 모드): 블록 1 "지인 추가", 모든 입력 placeholder ("이름", "010-", "예: 대학 동기 · 같은 과", "예: 회신이 늦는 편"), 소유자 = 로그인한 사람 쪽 기본 선택("신부"), 그룹 선택 0, 블록 9 없음. 스티키 좌 "저장하고 한 명 더"
- new-group: 블록 5 링크 자리에 `{component.input}` placeholder "그룹 이름" + `{component.button-primary}` compact "추가". 추가 시 새 칩이 selected로 붙음
- both (소유자 "공동"): 블록 5 칩 8개 — 이름 중복은 "직장 동료·신부" / "직장 동료·신랑" / "가족·신부" / "가족·신랑"
- error: 이름 비우고 저장 → 블록 2 아래 caption `{colors.ink}` "이름을 입력해 주세요", 입력 테두리 2px `{colors.primary-focus}`(포커스). 연락처는 선택 항목
- confirm-delete: 블록 9 참조

## 엣지케이스 노출

- 중복 소속: 블록 5 칩 2개 selected (`edgeCases.multiGroupPerson` p03 = [대학 동기][직장 동료])
- 1:1(직장 상사): 블록 7 "따로 만나기" — p31 강민석·p14 조은비는 "네" selected. 이 값이 `meeting-create` 경고와 `contacts-list` 우측 텍스트의 근거
- 상견례(양가 공통 지인): 블록 4 "공동" → p52 정민규처럼 양측 그룹에 동시에 넣을 수 있음
- 긴 텍스트: 블록 2에 p20 이름(16자)이 들어오면 입력 안에서 가로 스크롤, 잘리지 않음

## ASCII 스케치

```
┌──────────────────────────────┐
│ (‹)                          │ ← mobile-header, 뒤로가기만
├──────────────────────────────┤
│ 지인 수정                     │ ← display-md
│                              │
│ 이름                          │ ← caption muted
│ ( 박민아                     ) │ ← input
│ 연락처                        │
│ ( 010-4460-1192              ) │
│ 누구의 지인인가요               │
│ ((신부)) ( 신랑 ) ( 공동 )      │ ← status-chip, 신부 selected
│ 관계 그룹 · 여러 개 고를 수 있어요│
│ ((대학 동기)) ((직장 동료))      │ ← 2개 selected
│ ( 동네 친구 ) ( 가족 )  새 그룹 만들기│ ← text-link
│ 관계 메모                      │
│ ( 대학 동기 · 현재 같은 회사    ) │
│ 따로 만나기       ((아니요)) ( 네 )│ ← list-row + chip ×2
│ 다른 사람과 같은 모임에 넣으면 알려 드려요│
│ 메모 (나만 보기)                │
│ ( 대학 동기이면서 지금 같은 팀 동료.│
│   어느 모임에 넣을지 애매        ) │
│                              │
│          이 지인 삭제           │ ← text-link
├──────────────────────────────┤
│ 신부 · 그룹 2개          [ 저장 ]│ ← mobile-sticky-cta
└──────────────────────────────┘
```
