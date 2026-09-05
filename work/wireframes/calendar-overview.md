# calendar-overview — 전체 일정 (홈)

## 목적

신랑·신부 확정 모임을 월 달력에 합쳐 보고 겹친 날짜를 찾는다. 확정 전 모임은 달력 위 요약 행 1줄로 잇는다. PRD §4-5, §4-6.

## 진입 / 이탈

- 진입: 앱 시작(기본 화면) / `{component.mobile-tab-bar}` 탭 1 "달력" / `meeting-confirm` 완료 후 자동 복귀
- 이탈:
  - 헤더 우측 "새 모임" → `meeting-create`
  - 블록 3 요약 행 → `home-meetings` (확정 대기 섹션이 첫 스크롤)
  - 블록 5 달력 셀 탭 → 같은 화면, 블록 7·8이 그 날짜로 바뀜 (상태 `selected`)
  - 블록 8 모임 행 → `meeting-detail` (해당 meetingId)
  - 블록 10 빈 상태 버튼 → `meeting-create`
  - 탭바 "모임" → `home-meetings`, "지인" → `contacts-list`

## 프레임

- 390 × 844. 세로 스크롤 가능 (선택 날짜 모임이 3건 이상이면 늘어남). 그 외에는 한 화면에 들어간다.
- 헤더: `{component.mobile-header}` — 좌: 제목 "우리 일정" (`{typography.tagline}`), 우: `{component.button-primary}` compact "새 모임"
- 하단: `{component.mobile-tab-bar}` — 탭 3개 "달력"(활성, 아이콘 calendar) / "모임"(아이콘 list.bullet) / "지인"(아이콘 person.2)

## 레이아웃 스택 (위→아래)

| #   | 블록           | 컴포넌트 키                                                                                                                          | 내용 (mock-data 경로)                                                                                                                                                                                                                                                                                                                                                                  | 비고                                                                                                                                                                                                                                        |
| --- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | 소유자 필터    | `{component.status-chip}` × 4, 가로 1행                                                                                              | "전체"(selected) / "신부" / "신랑" / "공동" — `derived.sideLabels`                                                                                                                                                                                                                                                                                                                     | 단일 선택. 선택 = 2px `{colors.primary-focus}` 테두리. 필터 값이 블록 5 셀 텍스트와 블록 8 목록에 적용                                                                                                                                      |
| 2   | 결혼식 카운트  | `{typography.caption}` `{colors.ink-muted-48}`                                                                                       | "결혼식 " + `wedding.dateLabel` + " · D-" + `derived.daysToWedding` → "결혼식 12월 12일 (토) · D-23"                                                                                                                                                                                                                                                                                   | 우측 정렬, 블록 1과 같은 행에 넣지 않는다(칩 4개가 폭을 다 씀)                                                                                                                                                                              |
| 3   | 요약 행        | `{component.list-row}` × 1                                                                                                           | 제목(body-strong): "날짜 미정 모임 " + `derived.undatedMeetingIds.length` + "건" → "날짜 미정 모임 5건" / 메타(caption): "마감 임박 " + `meetings[m12].title` + " · " + `meetings[m12].deadlineText` → "마감 임박 입사 동기 · 마감 22시간" / 우: chevron.right                                                                                                                         | 배경 `{colors.canvas-parchment}` (본문과 구분). `undatedMeetingIds.length == 0`이면 블록 통째로 숨김. 마감 임박 = 회신 대기·확정 대기 중 deadline 오름차순 첫 번째                                                                          |
| 4   | 월 내비        | 조합: `{component.button-icon-circular}`(32px) × 2 + `{typography.tagline}`                                                          | 좌 아이콘 chevron.left / 중앙 "2026년 11월" (`derived.calendarMonth`) / 우 아이콘 chevron.right                                                                                                                                                                                                                                                                                        | 좌우 탭 → 같은 화면 이전/다음 달. 결혼식 월(12월) 이후로는 넘어가지 않음                                                                                                                                                                    |
| 5   | 요일 행        | `{typography.caption}` `{colors.ink-muted-48}` × 7                                                                                   | "일" "월" "화" "수" "목" "금" "토"                                                                                                                                                                                                                                                                                                                                                     | 7열 균등. 좌우 마진 `{spacing.lg}` 안에서 (390−48)/7                                                                                                                                                                                        |
| 6   | 달력 그리드    | 조합: 7열 × 5행 셀. 셀 = `{typography.caption-strong}` 날짜 숫자 + `{typography.caption}` 셀 텍스트. 행 사이 1px `{colors.hairline}` | 2026-11-01(일)부터 2026-11-30(월)까지 5행. 셀 텍스트 = `derived.calendar[YYYY-MM-DD].cellText` (없으면 빈칸): 11/7 "1건", 11/8 "1건", 11/14 "1건", 11/21 "1건", 11/22 "1건", 11/28 "2건 · 겹침", 11/29 "1건". 오늘(`derived.today` 11/19) 숫자는 `{colors.primary}`. 선택 셀(11/28)은 셀 전체에 2px `{colors.primary-focus}` 테두리(`{rounded.sm}`) — status-chip selected와 같은 문법 | 셀 높이 = 터치 타깃 44 이상(부록 A-5)에 텍스트 2줄이 들어가는 HUG, 셀 내부 패딩 `{spacing.xxs}`. 지난 날짜 숫자는 `{colors.ink-muted-48}`. 색으로 소유자·겹침 구분 금지 — 텍스트 "겹침"만. 필터가 "신부"면 신부 모임만 세어 cellText 재계산 |
| 7   | 선택 날짜 헤드 | `{typography.tagline}` + `{typography.caption}`                                                                                      | 좌 "11월 28일 (토)" / 우 `derived.calendar["2026-11-28"].cellText` "2건 · 겹침"                                                                                                                                                                                                                                                                                                        | 블록 6과 사이 `{spacing.xl}` 32px                                                                                                                                                                                                           |
| 8   | 선택 날짜 모임 | `{component.list-row}` × N                                                                                                           | `derived.calendar["2026-11-28"].meetingIds` = [m04, m05]. 행마다 — 제목: `meetings[].title` ("동네 친구" / "대학 후배") / 메타: `{component.status-chip}` `sideLabel` ("신부" / "신랑") + caption `memberCount`+"명 · "+`time`+" · "+`place` ("5명 · 19:00 · 연남동 소이연남" / "4명 · 18:30 · 신촌 미분당") / 우: chevron.right                                                       | 정렬: `time` 오름차순. 각 행 → `meeting-detail`                                                                                                                                                                                             |
| 9   | 겹침 안내      | `{typography.caption}` `{colors.ink}`                                                                                                | "같은 저녁에 2건이에요. 각 모임에서 '날짜 다시 잡기'를 할 수 있어요."                                                                                                                                                                                                                                                                                                                  | `derived.calendar[선택일].overlap == true`일 때만. 블록 8 아래                                                                                                                                                                              |

## 상태

- default (= selected 11/28): 위 스택 그대로. 03은 이 상태를 만든다. 실제 앱의 초기 선택일은 `derived.today`이며 이 경우 블록 7 "11월 19일 (목)", 블록 8은 아래 `no-meeting-day`.
- no-meeting-day: 블록 8·9 → `{typography.caption}` `{colors.ink-muted-48}` "이 날 확정된 모임이 없어요" 1줄.
- empty (모임 0개): 블록 3~9를 `{component.empty-state}`로 대체 — 제목 "첫 모임을 만들어 보세요" / 본문 "지인을 묶어 날짜 후보를 보내면, 확정된 모임이 이 달력에 표시돼요." / 버튼 "새 모임 만들기" → `meeting-create`. 블록 1·2는 유지.
- filtered (예: "공동"): 블록 6 셀 텍스트가 공동 모임만 계산 (11/22 "1건"만 남음). 블록 8도 필터 적용. 선택일에 결과 0이면 `no-meeting-day`.

## 엣지케이스 노출

- 겹치는 모임: 블록 6 셀 "2건 · 겹침"(`edgeCases.overlappingMeetings` m04·m05, 11/28) → 블록 7·8에서 두 모임이 소유자 칩과 함께 나란히 → 블록 9 안내.
- 늦은 회신 / 급한 모임: 블록 3 요약 행 "날짜 미정 모임 5건 · 마감 임박 입사 동기 · 마감 22시간"(`edgeCases.urgent` m12) — 확정 전 모임이 달력에 없는 약점(decisions 1-4)을 첫 화면 첫 줄에서 보완.
- 상견례(양가): 블록 1 "공동" 필터, 블록 8 행의 "공동" 칩 (11/22 선택 시 m09).

## ASCII 스케치

```
┌──────────────────────────────┐
│ 우리 일정              [새 모임]│ ← mobile-header (parchment blur)
├──────────────────────────────┤
│ (전체) ( 신부 ) ( 신랑 ) ( 공동 )│ ← status-chip ×4, 전체 selected
│              결혼식 12월 12일 (토) · D-23 │ ← caption muted
│┌────────────────────────────┐│
││ 날짜 미정 모임 5건          › ││ ← list-row (parchment bg)
││ 마감 임박 입사 동기 · 마감 22시간││
│└────────────────────────────┘│
│  (‹)     2026년 11월      (›) │ ← icon-circular 32 + tagline
│  일  월  화  수  목  금  토   │ ← caption muted
│  1   2   3   4   5   6   7   │
│                          1건 │
│  8   9  10  11  12  13  14   │
│ 1건                      1건 │
│ 15  16  17  18  19  20  21   │
│                 (오늘)    1건 │  ← 19 숫자 primary
│ 22  23  24  25  26  27 (28)  │  ← 28 숫자에 2px focus 원
│ 1건                  2건·겹침 │
│ 29  30                       │
│ 1건                          │
│                              │
│ 11월 28일 (토)        2건 · 겹침│ ← tagline + caption
│ 동네 친구                    › │ ← list-row
│ [신부] 5명 · 19:00 · 연남동 소이연남│
│ 대학 후배                    › │ ← list-row
│ [신랑] 4명 · 18:30 · 신촌 미분당 │
│ 같은 저녁에 2건이에요. 각 모임에서│ ← caption
│ '날짜 다시 잡기'를 할 수 있어요. │
├──────────────────────────────┤
│  ●달력      모임      지인    │ ← mobile-tab-bar (black)
└──────────────────────────────┘
```
