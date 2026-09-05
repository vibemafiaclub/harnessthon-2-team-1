# Review — calendar-overview (#1회차)

판정: FIX-LOCAL
프레임: `41:652` (default) · `42:615` (`--empty`) / 스크린샷: `work/screenshots/calendar-overview.review-1.png`, `work/screenshots/calendar-overview--empty.review-1.png` (2026-09-05 리뷰 시점 재촬영)

이전 리뷰 없음 → FIX-LOCAL 1회차. 판정 기준: `.claude/skills/oss-design-harness/SKILL.md` A1~~A10 / C1~~C6, 기준값 `design.md` + `work/brief.md` §4.
참조 `15:2020`에서 온 레이아웃(카드 문법, 다크 날짜 바, 월 헤딩 좌정렬)은 사용자 지시에 따라 design.md 부록 A와 충돌하지 않는 한 실패 사유로 삼지 않았다.

## A 결과 (노드 속성, default `41:652` / empty `42:615`)

| #   | 측정값                                                                                                                                                                                                                                                                         | 합격                |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| A1  | 솔리드 fill 미바인딩 0 / 0 · stroke 미바인딩 0 / 0                                                                                                                                                                                                                             | ✅                  |
| A2  | 텍스트 스타일 미적용 0 / 0. hero-display·display-lg·lead 사용 0                                                                                                                                                                                                                | ✅                  |
| A3  | Medium(500) 0 / 0                                                                                                                                                                                                                                                              | ✅                  |
| A4  | 토큰 외 gap/padding: 화면 레벨 0. 인스턴스 내부에서 `button-primary` compact 좌우 15, `empty-state` cta 11×22 검출 — design.md §Layout "Button padding: 8–11px vertical, 15–22px horizontal" 명시값이므로 위반 아님. 좌우 마진 24 (`41:660` pl/pr 24)                          | ✅                  |
| A5  | 인스턴스 14 ÷ (14 + 비인스턴스 프레임 62) = **0.18**. 비인스턴스 프레임 중 달력 그리드 41개(행 5 + 셀 35 + grid), 모임 카드 8개가 전부 손으로 그린 프레임. 그리드를 제외해도 0.40                                                                                              | ❌ (기준 ≥ 0.7)     |
| A6  | 자동 이름 0 / 0                                                                                                                                                                                                                                                                | ✅                  |
| A7  | 와이어 `## 상태` 4개 중 default ✅, empty ✅(`42:615`), **no-meeting-day ❌**, filtered ❌. no-meeting-day는 선택일의 빈 상태(문구 확정)라 필수로 본다. filtered는 데이터만 바뀌는 변형이라 SKILL.md A7("empty 필수, selected/error 해당 시") 기준으로 판정 보류               | ❌ (no-meeting-day) |
| A8  | 탭 가능 인스턴스 높이 < 44: `month-nav / prev` `41:988` 32, `month-nav / next` `41:994` 32(detach 프레임). design.md 부록 A-4는 `button-icon-circular` 32 축소를 **헤더 뒤로가기에만** 허용, 본문 §Touch Targets "exactly 44×44". 와이어가 32를 적었으나 design.md 본문이 우선 | ❌ (2)              |
|     | 참고(화면 책임 아님): 헤더 cta `button-primary` compact 36, `status-chip` 28 (8×15 / 4×12 패딩 + 텍스트 높이의 산술 결과 — 부록 A-4 스펙 그대로). Foundations 레벨 사안으로 오케스트레이터에 보고만                                                                            | 관찰                |
| A9  | effect 있는 노드: `mobile-header` 인스턴스의 `BACKGROUND_BLUR` 1개 (design.md §Elevation "Backdrop blur" 스펙, 그림자 아님). 그림자 0                                                                                                                                          | ✅                  |
| A10 | 와이어 스택 9행 → 실제 블록: filters(1·2) / summary(3) / calendar(4·5·6) / selected-day(7·8·9). 누락 0. 블록 8은 list-row 대신 card 조합(참조 반영·figma-log 기록) — 허용. 카드 정렬 time 오름차순 ✅ (18:30 → 19:00)                                                          | ✅                  |

## C 결과 (스크린샷 재촬영 기준)

| #   | 관찰                                                                                                                                                                                                                                                                                                                                                                                                                              | 기준                                                                                                                 | 판정                                        |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| C1  | 표면은 white(본문·카드) / parchment(헤더·요약 행) / near-black(선택일 바 `surface-tile-1`, 탭바 black)뿐. 원형 아이콘 버튼의 회색은 `surface-chip-translucent`. dark 섹션 1개                                                                                                                                                                                                                                                     | §Colors Surface 목록 / A-4 section-dark "1화면 1개 이하"                                                             | ✅                                          |
| C2  | 첫 3초에 읽히는 것은 다크 바 "11월 28일 (토)". 파란 pill CTA 1개("새 모임"). display-md 0개, tagline 헤드 3개(헤더 제목·월·선택일). 헤더 제목이 tagline인 것은 와이어·A-4 mobile-header 스펙. 다크 바가 달력(조망)보다 먼저 읽히는 점은 brief 판단기준 1("조망이 상세보다 먼저")과 긴장이 있으나, 참조 반영·A-4 허용 범위                                                                                                         | §Do "Reserve pill for primary CTA" / A-2 대제목 1개 / brief §3-1                                                     | ✅ (다크 바 우선 읽힘은 관찰만, 판정 보류)  |
| C3  | (a) 위쪽 밀도: 칩 → 카운트다운 → parchment 요약 행 → "2026년 11월" 헤딩이 각 8px 간격으로 붙어 있고, 달력 → 선택일 사이는 32px. 섹션 간 간격이 같은 급으로 느껴지지 않고 위가 아래보다 빽빽하다. (b) 셀 28 "2건 · 겹침"이 41px 셀에서 2줄로 꺾여 row-4만 66px(다른 행 46) — 그리드 행 리듬이 깨짐. 24px 마진 침범은 없음                                                                                                          | SKILL C3 "위쪽이 아래보다 빽빽하지 않은가 / 섹션 간 간격 같은 급" · A-3 섹션 간 32 · 와이어 블록 6 "텍스트 '겹침'만" | ❌ (a)(b) 모두 속성 하나로 해결 → FIX-LOCAL |
| C4  | 리스트(카드) 행 3줄(시간·인원 / 제목 / 칩+장소) — 와이어 "제목 + 메타 2줄"에서 메타가 위아래로 나뉜 형태이나 정보량은 제목+메타 2요소. 행당 chip 1개. 숫자 요약 D-23 / 5건 / 22시간 / 2건 = 4개                                                                                                                                                                                                                                   | SKILL C4                                                                                                             | ✅ (카드 3줄 구성은 참조 반영 범위, 관찰만) |
| C5  | 색 구분 chip 없음(소유자는 텍스트), 카드 그림자 없음(1px hairline만), 그라디언트·이모지·보라 계열 없음, 카드 안 카드 없음, 일러스트 없음. radius: 다크 바·선택 셀 sm(8), 카드 lg(18), 칩·CTA pill — §Don't "radii grammars" 안                                                                                                                                                                                                    | §Don't 전부                                                                                                          | ✅                                          |
| C6  | `--empty`는 default와 같은 헤더·필터·탭바. 문구 "첫 모임을 만들어 보세요 / 지인을 묶어 날짜 후보를 보내면, 확정된 모임이 이 달력에 표시돼요 / 새 모임 만들기" — 도메인 맥락. 긴 장소명 "연남동 소이연남" 잘림·겹침 없음. 카운트다운·요약 행의 한글이 스크린샷에서 비어 보이나 `characters`는 정상("결혼식 12월 12일 (토) · D-23", "날짜 미정 모임 5건", "마감 임박 입사 동기 · 마감 22시간") → Inter 한글 글리프 폴백 렌더 레이스 | SKILL C6                                                                                                             | ✅ (글리프 공백은 관찰만, 판정 보류)        |

## 수정 목록 (FIX-LOCAL, 6항목)

- [ ] `41:988` `month-nav / prev` → `button-icon-circular` **Size=44** 변형(`20:230`)으로 스왑 (근거 design.md §Touch Targets "exactly 44×44", 부록 A-4 32 허용은 헤더 뒤로가기만)
- [ ] `41:994` `month-nav / next` → Size=44(`20:230`) 인스턴스에서 다시 만들고 chevron 좌우 반전, 44×44 (근거 동일). `month-nav` 행 높이 32→44로 늘어나므로 `41:985` 정렬 확인
- [ ] `41:1093` `cell-28 / text` "2건 · 겹침" → **"겹침"** 1줄 (근거 와이어 블록 6 "텍스트 '겹침'만", 부록 C 마이크로카피 권한). 적용 후 row-4 높이가 다른 행과 같은 46인지 확인. 건수는 `42:581` head/count "2건 · 겹침"에 이미 있음
- [ ] `41:984` `calendar` 블록 `paddingTop` = `spacing/lg`(24) 바인딩 → 요약 행과 월 헤딩 사이 8+24 = 32로 선택일 블록 앞 32와 같은 급 (근거 A-3 "섹션 간 32", SKILL C3)
- [ ] A5: 달력 셀 `41:1005` 하위 35개와 모임 카드 `42:582`/`42:592`를 **로컬 컴포넌트화** — `calendar-overview / calendar-cell`(State=default/today/past/selected 또는 최소 default+selected) 1개 + 인스턴스 35, `calendar-overview / meeting-card` 1개 + 인스턴스 2. 예상 재사용률 (14+37) ÷ (51+약 17) ≈ 0.75 (근거 SKILL A5 ≥ 0.7, 부록 C "조합 컴포넌트는 토큰만 사용하고 figma-log에 기록")
- [ ] A7: `calendar-overview--no-meeting-day` 프레임 추가 (`42:615` 오른쪽). default 복제 후 선택 셀 19(오늘) / head "11월 19일 (목)" + count 빈칸 / 블록 8·9 → caption `ink-muted-48` "이 날 확정된 모임이 없어요" 1줄 (근거 와이어 `## 상태` no-meeting-day, SKILL A7)

보류(수정 불요): `filtered` 상태 프레임, 카드 3줄 구성, 다크 바 우선 읽힘, Foundations 유래 높이(compact CTA 36 / chip 28).

## 오케스트레이터 참고 (이 화면 판정에 미반영)

- Foundations: `button-primary` compact(36) · `status-chip`(28)은 부록 A-4 패딩 스펙의 산술 결과라 44 터치 타깃에 못 미친다. 화면마다 반복될 사안 — 게이트 3 승인 자산이므로 사람 결정 필요(예: 시각 크기 유지 + 44 히트 영역 래핑).
- figma-log의 헤더·탭바 노드 ID(`41:653`, `41:678`)는 실제 `15:4101`, `15:4069`로 다르다. 파일 내용은 정상, 로그 오기.

---

# Review — calendar-overview (#2회차)

판정: FIX-LOCAL (2회차 — 3회째 실패 시 REDIRECT-B 승격)
프레임: `41:652` (default, 390×1066) · `42:615` (`--empty`) · `45:1258` (`--no-meeting-day`, 신규) / 스크린샷: `work/screenshots/calendar-overview.review-2.png`, `calendar-overview--empty.review-2.png`, `calendar-overview--no-meeting-day.review-2.png` (리뷰 시점 재촬영)

1회차 수정 목록 6항목 처리 확인: prev/next 44×44 ✅ · cell-28 "겹침" 1줄, 그리드 5행 모두 46 ✅ · calendar paddingTop 24 ✅ · no-meeting-day 프레임 ✅ · 로컬 컴포넌트화 ⚠️(아래 A5). 사용자 지시 항목(상태바·홈 인디케이터)은 존재를 실패로 보지 않고 토큰·네이밍·44 규칙만 적용.

## A 결과 (default / empty / no-meeting-day)

| #   | 측정값                                                                                                                                                                                                                                                                                                                                                                                             | 합격      |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| A1  | fill 미바인딩 0/0/0 · stroke 미바인딩 0/0/0 (상태바 벡터·홈 인디케이터 포함)                                                                                                                                                                                                                                                                                                                       | ✅        |
| A2  | 텍스트 스타일 미적용 0/0/0                                                                                                                                                                                                                                                                                                                                                                         | ✅        |
| A3  | Medium 0/0/0                                                                                                                                                                                                                                                                                                                                                                                       | ✅        |
| A4  | 화면 레벨 토큰 외 값: **`status-bar` paddingTop 14** — `45:715` / `45:732` / `45:1334` 3개. (인스턴스 내부 버튼 패딩 15·11·22는 1회차와 같이 design.md §Layout 명시값)                                                                                                                                                                                                                             | ❌ (3)    |
| A5  | **산식(명시):** 인스턴스 ÷ (인스턴스 + 인스턴스 밖 자체 프레임 중 **직접 그린 것** = 스트로크·솔리드 fill·벡터/도형 자식이 있는 프레임). 순수 auto-layout 래퍼(body·섹션·행·controls 등)와 Foundations 인스턴스 내부 프레임은 "컴포넌트 없이 그린 프레임"이 아니므로 분모에서 뺀다. default: 51 ÷ (51 + 8) = **0.86** (03 산식 51/73 = 0.70도 통과). 03이 뺀 것과 같은 취지.                       | ✅ (수치) |
|     | **단, 로컬 컴포넌트 2개가 캔버스에 없다.** `calendar-overview / calendar-cell` `45:790`(SET)·`meeting-card` `45:1177` 모두 `parent: null`, 홀더 `45:771`·`45:1167` 존재하지 않음. `📱 Screens`·`🎨 Foundations` 어느 페이지에서도 COMPONENT/SET 검색 결과 0. 인스턴스 37개는 고아 마스터를 참조 중(렌더는 되나 마스터를 찾거나 편집할 수 없음). A5의 취지(재사용·유지보수)가 실체 없이 충족된 상태 | ❌ (구조) |
| A6  | 자동 이름 0/0/0. 상태바 `calendar-overview / status-bar / {time,icons,signal,wifi,battery}`, 홈 인디케이터 `calendar-overview / tab-bar / home-indicator` 규칙 준수                                                                                                                                                                                                                                | ✅        |
| A7  | default ✅ · empty ✅ · no-meeting-day ✅(`45:1258`: 셀 19 selected + primary, head "11월 19일 (목)", 카드·안내 대신 caption). filtered: 1회차와 같이 판정 보류                                                                                                                                                                                                                                    | ✅        |
| A8  | month-nav prev `41:988` 44 / next `45:675` 44 ✅. status-chip 32(Foundations 변경 반영) ✅. calendar-cell 인스턴스 46 ✅, meeting-card 115 ✅. 남은 것: 헤더 `button-primary` compact 36 — Foundations 사안(1회차 참고 항목), 화면 책임 아님                                                                                                                                                       | ✅        |
| A9  | `mobile-header` BACKGROUND_BLUR만. 그림자 0. 상태바·홈 인디케이터 effect 없음                                                                                                                                                                                                                                                                                                                      | ✅        |
| A10 | filters / summary / calendar / selected-day 4블록 = 와이어 9행 전부. 상태바·홈 인디케이터는 절대 위치 오버레이라 스택에 영향 없음                                                                                                                                                                                                                                                                  | ✅        |

## C 결과

| #   | 관찰                                                                                                                                                                                                                                                                 | 기준           | 판정                  |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------------- |
| C1  | 표면 white / parchment / near-black 그대로. dark 섹션 1개(선택일 바). 상태바는 parchment 헤더 위에 ink 단색, 홈 인디케이터는 black 탭바 위 on-dark                                                                                                                   | §Colors / A-4  | ✅                    |
| C2  | 파란 pill CTA 1개. 첫 읽힘은 다크 바 → 달력 순(1회차와 동일, 보류 유지). no-meeting-day도 동일 위계                                                                                                                                                                  | SKILL C2       | ✅                    |
| C3  | 요약 행 ↔ "2026년 11월" 32px, 달력 ↔ 다크 바 32px — 섹션 간격 같은 급. 그리드 5행 균등(46), 셀 28 "겹침" 1줄. 24px 마진 침범 없음. 1회차 (a)(b) 해소                                                                                                                 | SKILL C3 / A-3 | ✅                    |
| C4  | 변화 없음(카드 3줄 구성 관찰만, 숫자 요약 4개)                                                                                                                                                                                                                       | SKILL C4       | ✅                    |
| C5  | 변화 없음. 상태바 아이콘은 단색 ink 벡터(이모지·컬러 아님)                                                                                                                                                                                                           | §Don't         | ✅                    |
| C6  | `--empty`·`--no-meeting-day` 모두 default와 같은 상태바·헤더·필터·탭바. no-meeting-day 문구 "이 날 확정된 모임이 없어요" 도메인 맥락. `--empty`의 카운트다운 한글이 이번에도 비어 보이나 `42:624` characters "결혼식 12월 12일 (토) · D-23" 정상 → 렌더 레이스, 보류 | SKILL C6       | ✅ (글리프 공백 보류) |

## 수정 목록 (FIX-LOCAL #2, 2항목)

- [ ] **로컬 컴포넌트 2개를 캔버스에 복원.** `45:790` `calendar-overview / calendar-cell`(SET)과 `45:1177` `calendar-overview / meeting-card`를 `📱 Screens` 페이지의 홀더 프레임(예: `calendar-overview / components`, 화면 프레임 오른쪽)에 다시 넣는다. `getNodeByIdAsync`로 잡히면 `holder.appendChild(node)`; 안 되면 같은 이름·변형으로 재생성 후 인스턴스 37개(`41:1005` 하위 35 + `45:1179`·`45:1189`, no-meeting-day 복제본 포함)를 `swapComponent`. 완료 후 `page.findAllWithCriteria({types:['COMPONENT','COMPONENT_SET']})`에 2개가 잡혀야 한다. figma-log의 홀더 ID(`45:771`, `45:1167`)도 정정 (근거 SKILL A5 취지, 부록 C "조합 컴포넌트는 figma-log에 기록" — 기록된 노드가 실재해야 함)
- [ ] `45:715` / `45:732` / `45:1334` `status-bar` paddingTop 14 → 토큰값. 높이 47 고정 + `counterAxisAlignItems: CENTER`이므로 pt/pb 0으로 두거나, 노치 아래 정렬이 필요하면 `spacing/sm`(12) 또는 `spacing/md`(17) 바인딩 (근거 SKILL A4 "토큰 밖 0")

보류(수정 불요): filtered 상태, 카드 3줄 구성, 다크 바 우선 읽힘, Foundations compact CTA 36, 상태바 아이콘 플레이스홀더(로그에 교체 필요로 기록됨).

---

# Review — calendar-overview (#3회차)

판정: **PASS**
프레임: `41:652` (default, 390×1066) · `42:615` (`--empty`) · `45:1258` (`--no-meeting-day`) · 홀더 `50:1302` (`calendar-overview / _components`) / 스크린샷: `work/screenshots/calendar-overview.review-3.png`, `calendar-overview--empty.review-3.png`, `calendar-overview--no-meeting-day.review-3.png` (리뷰 시점 재촬영)

2회차 수정 목록 2항목 처리 확인: status-bar pt/pb 0 + 47 고정 + CENTER ✅ · 고아 마스터 2개가 `📱 Screens` > `calendar-overview / _components` `50:1302` 아래 실재(`findAllWithCriteria` 결과: calendar-cell SET + 변형 5 + meeting-card) ✅, 인스턴스 37개 마스터 연결 유지 ✅. 추가: 홈 인디케이터 레이어명 `calendar-overview / home-indicator`(A-1 신규 행 기준) ✅.

## A 결과 (default / empty / no-meeting-day / 홀더)

| #   | 측정값                                                                                                                                                                                 | 합격 |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| A1  | fill 미바인딩 0/0/0/0 · stroke 미바인딩 0/0/0/0. 상태바 time·벡터 `colors/ink`, 홈 인디케이터 `colors/on-dark`(`18:120`) — A-1 신규 행 스펙과 일치                                     | ✅   |
| A2  | 텍스트 스타일 미적용 0/0/0/0                                                                                                                                                           | ✅   |
| A3  | Medium 0/0/0/0                                                                                                                                                                         | ✅   |
| A4  | 자체 프레임 토큰 외 gap/padding 0/0/0/0. status-bar pt 14 → 0 해소. (인스턴스 내부 버튼 패딩 15·11·22는 design.md §Layout 명시값)                                                      | ✅   |
| A5  | 2회차 산식: default 51 ÷ (51 + 직접 그린 자체 프레임 8) = **0.86**; no-meeting-day 47 ÷ (47 + 8) = 0.85; empty 12 ÷ (12 + 3) = 0.80. 마스터 2개 캔버스 실재 확인(2회차 구조 지적 해소) | ✅   |
| A6  | 자동 이름 0/0/0/0. `{screen-id} / status-bar`, `{screen-id} / home-indicator` A-1 규칙 준수                                                                                            | ✅   |
| A7  | default ✅ · empty ✅ · no-meeting-day ✅. filtered 보류(1·2회차 동일)                                                                                                                 | ✅   |
| A8  | month-nav 44/44, status-chip 32, calendar-cell 46, meeting-card 115, 그리드 5행 46 균등. 헤더 compact CTA 36은 Foundations 사안(1회차 참고 항목 유지)                                  | ✅   |
| A9  | `mobile-header` BACKGROUND_BLUR만. 그림자 0                                                                                                                                            | ✅   |
| A10 | 4블록(filters / summary / calendar / selected-day) = 와이어 9행 전부. 상태바·홈 인디케이터는 절대 위치 오버레이                                                                        | ✅   |

## C 결과

| #   | 관찰                                                                                                                                                                      | 기준           | 판정                  |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------------- |
| C1  | 표면 white / parchment / near-black. dark 섹션 1개. 변화 없음                                                                                                             | §Colors / A-4  | ✅                    |
| C2  | 파란 pill CTA 1개. 다크 바 우선 읽힘은 1·2회차와 같이 관찰만                                                                                                              | SKILL C2       | ✅                    |
| C3  | 섹션 간격 32/32 같은 급, 그리드 행 균등, 마진 침범 없음. 상태바 "9:41"·아이콘이 47px 안에서 세로 중앙, 헤더 제목과 겹치지 않음                                            | SKILL C3 / A-3 | ✅                    |
| C4  | 변화 없음                                                                                                                                                                 | SKILL C4       | ✅                    |
| C5  | 변화 없음. 상태바 아이콘 단색 ink                                                                                                                                         | §Don't         | ✅                    |
| C6  | 세 상태 프레임 모두 동일 상태바·헤더·필터·탭바·홈 인디케이터. 문구 도메인 맥락. `--empty` 카운트다운 한글 공백은 `42:624` characters 정상(2회차 확인) → 렌더 레이스, 보류 | SKILL C6       | ✅ (글리프 공백 보류) |

## 남은 참고 (판정 무관, 오케스트레이터·사람용)

- Foundations `button-primary` compact 36px 터치 타깃 — 게이트 3 자산, 사람 결정 대기(1회차 참고 항목).
- 상태바 signal/wifi/battery, month-nav next chevron, 탭바 아이콘은 플레이스홀더 — figma-log에 교체 필요로 기록됨.
- filtered 상태 프레임은 만들지 않음(데이터 변형, SKILL A7 필수 아님).
