# Review — meeting-create (#1회차)

판정: **FIX-LOCAL**
프레임: `42:603` (default) · `43:991` (--empty) / 스크린샷: `work/screenshots/meeting-create.review-1.png`, `work/screenshots/meeting-create--empty.review-1.png`

이전 리뷰 없음 → FIX-LOCAL 1회차. REDIRECT-B 이력 0.

## A 결과

측정 스크립트: `use_figma` 읽기 2회, 두 프레임 전체 순회 (default 115 노드 / empty 35 노드).

| #   | 측정값                                                                                                                                                                                                                                                                                                                                                                   | 합격                |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| A1  | 미바인딩 솔리드 fill 0 / stroke 0 (두 프레임). `43:655`, `43:674` `icon / check`에 visible=false 흰 fill 1개 — 비가시라 제외                                                                                                                                                                                                                                             | 통과                |
| A2  | 텍스트 스타일 미적용 0 (default 39 · empty 12). display-md 1개(제목), hero-display/display-lg/lead 0                                                                                                                                                                                                                                                                     | 통과                |
| A3  | Medium 0                                                                                                                                                                                                                                                                                                                                                                 | 통과                |
| A4  | 화면 레벨 auto-layout gap/padding 토큰 외 **0**. 토큰 외 값은 전부 Foundations 컴포넌트 내부: `input` pl/pr 20 (design.md §search-input "12px × 20px"), `button-primary` 11×22 (§button-primary). 본문 > SKILL 우선순위로 허용                                                                                                                                           | 통과 (주석)         |
| A5  | default: 인스턴스 20 ÷ (20 + 컴포넌트 없이 그린 프레임 38) = **0.34**. 순수 레이아웃 컨테이너(fill·stroke 없음) 제외해도 20 ÷ 36 = 0.56. 원인: 지인 행 7개(`43:635` `43:646` `43:657` `43:666` `43:958` `43:967` `43:976`)가 각각 row+lead+meta+icon(+check) 4~5개 프레임의 raw 조립. empty: 7 ÷ 11 = 0.64                                                               | **실패** (< 0.7)    |
| A6  | 자동 이름 0                                                                                                                                                                                                                                                                                                                                                              | 통과                |
| A7  | 와이어 `## 상태` 6개: default ○ / **both ✕** / **separate-warning ✕** / **error ✕** / **search-empty ✕** / empty ○. `both`는 상견례(`edgeCases.bothSides`), `separate-warning`은 1:1(`oneOnOne`) 엣지케이스가 **유일하게 노출되는 상태** — `_index.md` 배치표가 이 화면 블록 3·9에 걸어 둔 케이스가 어느 프레임에도 없다                                                 | **실패** (4개 누락) |
| A8  | 탭 가능 인스턴스 중 높이 < 44: `status-chip` **h=28** (chip 허용선 32 미달). default 8개 — owner `42:1119` `42:1121` `42:1123`, group-filter `42:1132` `42:1134` `42:1136` `42:1138` `42:1140`. empty 3개 — `43:1009` `43:1011` `43:1013`. (행 메타 칩 8개는 라벨이라 제외.) 원인은 Foundations `status-chip` 세트 `20:434`(4×12 패딩 + caption 20 = 28)                 | **실패** (11개)     |
| A9  | effect 보유 노드 4개 = header `42:604` `43:992`, sticky-cta `43:985` `43:1021`. 전부 `BACKGROUND_BLUR` 20, 그림자 0. design.md §Elevation "Backdrop blur … Sub-nav and floating sticky bar" + A-4 `mobile-header`/`mobile-sticky-cta` "parchment 80% + blur" 명시 → 허용. 관찰만: 두 컴포넌트 fill opacity 1(80% 아님) — Foundations 소관, 게이트 3 통과분이라 판정 보류 | 통과 (주석)         |
| A10 | 와이어 스택 1·2·3·4·5·6·8 (7 없음, 9는 default 숨김) = 7행 ↔ 실제 `content` 4블록(title/name/owner/members) + `members` 4블록(head/search/group-filter/rows) = 7. header·sticky 존재. 누락 0                                                                                                                                                                             | 통과                |

## C 결과

| #   | 관찰                                                                                                                                                                                                                                                                                                                                                                                             | 기준 (design.md)                                                                                                                                                                           | 판정                       |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| C1  | 표면 white(canvas) + parchment(header·sticky·선택 행·empty-state)뿐. dark 섹션 0. 액센트 blue 1종                                                                                                                                                                                                                                                                                                | §Colors Surface 3종 / A-4 section-dark "1화면 1개 이하"                                                                                                                                    | 통과                       |
| C2  | display-md "새 모임" 1개. 파란 pill: default 1개(sticky), empty 2개("지인 추가" + sticky "다음: 날짜 후보"). 3초 판독: 제목 → "구성원" 목록으로 한 줄기. 관찰만: empty에서 0명 선택인데 "다음: 날짜 후보"가 "지인 추가"와 같은 무게로 남아 두 pill이 경합 — 와이어 error 규칙("버튼 비활성 시각 없음")대로라 판정 보류                                                                           | C2 "파란 pill CTA 1~2개" / A-2 display-md 1개                                                                                                                                              | 통과 (관찰 1)              |
| C3  | (1) 위 블록(제목·이름·소유자, gap 17) ↔ 구성원 섹션 pt 32 — 위가 아래보다 빽빽하지 않음. (2) **빌더 판단 요청 — 선택 행 parchment 하이라이트가 24px 안쪽(342폭)만 칠해짐**: 스크린샷에서 선택 행 좌우에 흰 거터 24px가 남아 "행 배경 전환"이 아니라 "안쪽에 놓인 회색 블록"으로 읽힌다. 같은 화면의 empty-state(`43:1015`)는 390 풀블리드라 두 문법이 한 파일에 공존                             | §Overview "full-bleed tile sections … the color change itself acting as the section divider" / Don't "tiles are rectangular and edge-to-edge" — 표면색 전환은 가장자리까지, 내용만 24 인셋 | **실패 → FIX-LOCAL** (2)   |
| C4  | 행 7개 중 6개는 제목 + 메타 1줄 = 2줄. **p03 박민아(`43:635`)는 제목 + 칩 2개 + caption이 3줄(h 101)** — meta 폭 301에 칩 83+8+83+8+caption 132 = 314로 13px 넘쳐 wrap. chip/행 최대 2(허용선). 숫자 요약 "2명 선택" 2개                                                                                                                                                                         | C4 "리스트 행은 제목 + 메타 2줄까지" / "한 행에 chip 2개 초과 금지"                                                                                                                        | **실패 → FIX-LOCAL** (p03) |
| C5  | 칩은 hairline 테두리 + 텍스트, 선택은 2px primary-focus 테두리만. 그림자·그라디언트·이모지·보라·카드 안 카드 0. 체크 아이콘 ink 단색                                                                                                                                                                                                                                                             | C5 목록 / A-4 status-chip "색으로 상태 구분 금지"                                                                                                                                          | 통과                       |
| C6  | (1) empty 헤더 = default와 같은 변형(Left=back, Right=none), 블록 1~3 동일 유지, 문구 "고를 지인이 없어요 / 먼저 지인을 등록해 주세요." 도메인 맥락 ○. (2) **group-filter 5번째 칩 "가족"이 24px 마진선에서 "가"로 잘림**(`42:1140`, x 319 + w 50 > 342). 빌더는 "가로 스크롤 의도"라 했으나 마진 안쪽에서 잘리면 스크롤 어포던스가 아니라 크롭 결함으로 읽힌다. 긴 이름 데이터는 이 화면에 없음 | C6 "잘리거나 겹치는가" / A-1 side-margin 24                                                                                                                                                | **실패 → FIX-LOCAL** (2)   |

빌더 판단 요청 회신:

- **조합 list-row (A5)**: 조합 자체는 부록 C·`_index.md` 공통 항목("선택 아이콘 행")으로 허용. 문제는 조합을 **컴포넌트로 승격하지 않고 raw 프레임 7벌**로 찍은 것 — 그래서 A5가 0.34. 컴포넌트화하면 통과 가능(아래 수정 1).
- **parchment 하이라이트 인셋 (C3)**: 실패. 표면색 전환은 풀블리드, 내용만 24 인셋(수정 2).

## 수정 목록 (FIX-LOCAL 시)

- [ ] **A5** `foundations / components`(`18:159`)에 조합 컴포넌트 `list-row-selectable` 신설(변형 `Selected=false/true`; 내부: title body-strong + meta WRAP[status-chip 인스턴스 슬롯, caption] + 우측 24px 아이콘; 배경 canvas/parchment 바인딩, 하단 1px hairline, pt/pb `spacing/sm`, **pl/pr `spacing/lg`**, minHeight 44). `members / rows`(`42:1142`)의 raw 행 7개를 인스턴스 7개로 교체, `figma-log.md` 조합 컴포넌트 표에 기록. 예상 A5 = 19 ÷ (19 + 8) = 0.70 — **래퍼 프레임을 추가하면 0.68로 다시 실패하므로 새 컨테이너 금지**. (근거 design.md 부록 C "조합 컴포넌트 … figma-log에 기록", SKILL A5)
- [ ] **C3·C6** 풀블리드 재배치(새 프레임 0개로): `content`(`42:614`) pl/pr 24 → 0, `counterAxisAlignItems` CENTER; `title` `42:1111`·`name` `42:1112`·`owner` `42:1116` 폭 FIXED 342; `members`(`42:1125`) FILL 390 + CENTER 정렬; `head`(`42:1126`) FILL + pl/pr `spacing/lg`; `search`(`42:1129`) FIXED 342; `group-filter`(`42:1131`) FILL 390 + pl/pr `spacing/lg` + clipsContent(칩이 **화면 가장자리에서** 잘리도록); `rows`(`42:1142`) FILL 390, 각 행 인스턴스가 pl/pr 24를 자체 보유. `--empty`(`43:1000`~)도 동일 구조. (근거 design.md §Overview full-bleed / A-1 side-margin 24)
- [ ] **C4** `43:635` p03 meta 넘침 13px: 메타 caption을 7행 전부 "'직장 팀'에 편성됨"으로 축약(`43:643` `43:652` `43:663` `43:964` `43:982`; 폭 약 100 → 83+8+83+8+100 = 282 ≤ 301). 부록 C 마이크로카피 권한 내. 축약 후에도 wrap이면 caption을 칩 앞으로 옮기지 말고 보고. (근거 SKILL C4 "제목 + 메타 2줄까지")
- [ ] **A8** Foundations `status-chip` `20:430`·`20:432`: `minHeight` 32 + 세로 CENTER (패딩 4×12는 A-4 그대로 유지). 이 화면 인스턴스 11개가 자동 반영. **공유 컴포넌트라 `calendar-overview` 칩 높이도 28→32로 바뀜** — 오케스트레이터에 알릴 것(다른 세션 노드는 직접 수정 금지). (근거 SKILL A8 "chip 32 허용", A-5)
- [ ] **A7** 상태 프레임 4개를 `43:991` 오른쪽에 추가 (와이어 `## 상태` 그대로):
  - `meeting-create--separate-warning`: p14 조은비 + p12·p13 선택, 블록 9 caption `colors/ink` "조은비 님은 따로 만나기로 표시돼 있어요. 이대로 진행할 수 있어요." (rows 바로 아래, sticky 위), sticky "3명 선택" — **1:1 엣지케이스 노출 프레임(우선)**
  - `meeting-create--both`: 소유자 "공동" selected, group-filter "전체"+그룹 8개("직장 동료·신부" 형식), 행 메타 첫 칩 sideLabel, p22·p23·p40·p41 예시 — **상견례 엣지케이스 노출 프레임(우선)**
  - `meeting-create--error`: 블록 2 아래 caption "모임 이름을 입력해 주세요" (또는 블록 9 자리 "구성원을 1명 이상 골라 주세요")
  - `meeting-create--search-empty`: rows → caption `ink-muted-48` "'박'에 해당하는 지인이 없어요"
    (근거 SKILL A7 "전부 존재", `_index.md` 까다로운 상황 배치표 meeting-create 3·9)

## 재발산 사유 (REDIRECT-B 시)

해당 없음. 실패 항목은 전부 속성·컴포넌트 승격·프레임 추가로 닫힌다 — 블록 구성·순서·단위는 와이어와 일치(A10 누락 0).

## 관찰만 (판정 보류, 다음 회차 참고)

- `mobile-header`/`mobile-sticky-cta` fill opacity 1 — A-4 "parchment 80%"와 불일치. Foundations 소관.
- empty 상태에서 파란 pill 2개("지인 추가" + "다음: 날짜 후보") 경합. 와이어 규칙 범위라 판정 안 함.
- 검색 input 돋보기 아이콘 없음(빌더 로그와 동일). 아이콘 교체 목록 항목.
