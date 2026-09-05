# figma-log.md — 03-figma-builder 실행 로그

> **폰트 대체:** `SF Pro Display` / `SF Pro Text` 없음 → `design.md` §Note on Font Substitutes에 따라 **Inter**로 대체.
> display 크기 letter-spacing 추가 -0.01em(예: hero-display -0.28 → -0.84px, display-md -0.374 → -0.714px), body line-height 1.47 → 1.44.
> weight 매핑: 300 Light / 400 Regular / 600 Semi Bold / 700 Bold. 500 미사용.
> (파일에 `SF Pro` 단일 패밀리는 존재하나 Display/Text 분리 패밀리가 아니므로 정책대로 Inter 채택.)

- fileKey `dyqBJHi5EN92veBmDgLjx8` · 기준 노드 `14:60` = **SECTION "Section 1"** (Page 1 안, 화면 배치 기준점으로는 쓰지 않음 — `📱 Screens` 페이지에 배치)
- 파일에 이 프로젝트와 무관한 기존 자산 존재(컬렉션 `Calculator`, `Wedding Scheduler Tokens`, Pretendard `typography/*` 스타일 12개). **건드리지 않음.** 이 프로젝트 자산은 컬렉션 `design.md` + 스타일 접두사 `design.md/`로 분리.

## Foundations

실행일 2026-09-05. 상태: **이미 생성되어 있어 재생성하지 않음** (정의 파일 모드 A 1단계). 인벤토리·자체 검증·스크린샷만 수행.

### 페이지

| 페이지           | 노드 ID                                                      |
| ---------------- | ------------------------------------------------------------ |
| `🎨 Foundations` | `18:102` (루트 프레임 `foundations / components` = `18:159`) |
| `📱 Screens`     | `18:103` (비어 있음)                                         |

### 변수 컬렉션 `design.md` — `VariableCollectionId:18:104`, 모드 `Light` (`18:0`), 변수 37개

| 그룹        | 변수 (ID 접미)                                                                                                                                                                                                                                                                                                                                                                                     | scopes                                                                    |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| colors (21) | primary 18:105 · primary-focus 106 · primary-on-dark 107 · on-primary 108 · canvas 109 · canvas-parchment 110 · surface-pearl 111 · surface-tile-1 112 · surface-tile-2 113 · surface-tile-3 114 · surface-black 115 · surface-chip-translucent 116 · ink 117 · body 118 · body-on-dark 119 · on-dark 120 · body-muted 121 · ink-muted-80 122 · ink-muted-48 123 · divider-soft 124 · hairline 125 | 배경 `FRAME_FILL,SHAPE_FILL` / 텍스트 `TEXT_FILL` / 테두리 `STROKE_COLOR` |
| spacing (9) | xxs 126(4) · xs 127(8) · sm 128(12) · md 129(17) · lg 130(24) · xl 131(32) · xxl 132(48) · section 133(80) · section-mobile 134(48)                                                                                                                                                                                                                                                                | `GAP`                                                                     |
| rounded (7) | none 135(0) · xs 136(5) · sm 137(8) · md 138(11) · lg 139(18) · pill 140(9999) · full 141(9999)                                                                                                                                                                                                                                                                                                    | `CORNER_RADIUS`                                                           |

(전체 ID 형식: `VariableID:18:1xx`)

### 텍스트 스타일 (접두사 `design.md/typography/`, Inter, 16개)

| 토큰           | 스타일 ID                                     | 값                             |
| -------------- | --------------------------------------------- | ------------------------------ |
| hero-display   | `S:4c70a333e543df15f1dd1c43c0da61ffc289f9fb,` | 56 / Semi Bold / 107% / -0.84  |
| display-lg     | `S:476afa3acf72d6251e070cdf69be9cedd1979acf,` | 40 / Semi Bold / 110% / -0.4   |
| display-md     | `S:1fda48f9e88df47100ea111bf5d96240258acad9,` | 34 / Semi Bold / 147% / -0.714 |
| lead           | `S:8fbad9b718679b8ec212a386701da63fe1de7058,` | 28 / Regular / 114% / -0.084   |
| lead-airy      | `S:324bc9470a357f588be6b87f3df613b49baa9a0f,` | 24 / Light / 150% / -0.24      |
| tagline        | `S:e79e7f0e468045ea8140fd5e028e3d2bc189d484,` | 21 / Semi Bold / 119% / 0.021  |
| body-strong    | `S:a54d516da550a52dc43a2081523dd1572e8266a8,` | 17 / Semi Bold / 124% / -0.374 |
| body           | `S:79536eceaaf7a02f64abf4ac7e56759558695f78,` | 17 / Regular / 144% / -0.374   |
| dense-link     | `S:4b7339cce2f8feb5d849d91d1900daf4d2ca0066,` | 17 / Regular / 241% / 0        |
| caption        | `S:3991828a56ee54aafdbd504dd021249396956bc5,` | 14 / Regular / 143% / -0.224   |
| caption-strong | `S:447f869242f638fa5dff34019f7b6467096abe1f,` | 14 / Semi Bold / 129% / -0.224 |
| button-large   | `S:5dbe2618c8948fd928151f3790ab8bcabc9c5978,` | 18 / Light / 100% / 0          |
| button-utility | `S:d0545367b3d764ebde6dc49da535f2ab8f80a2da,` | 14 / Regular / 129% / -0.224   |
| fine-print     | `S:828a609eea6a76bbf151a122eaa349c645134058,` | 12 / Regular / 100% / -0.12    |
| micro-legal    | `S:63c76072174adbf4a76e998f6c242f404107a23a,` | 10 / Regular / 130% / -0.08    |
| nav-link       | `S:4ad8287158b2e7527c09775d9ea734d343eed4b3,` | 12 / Regular / 100% / -0.12    |

### 이펙트 스타일

| 이름                    | ID                                            | 값                                 |
| ----------------------- | --------------------------------------------- | ---------------------------------- |
| `effect/product-shadow` | `S:edb1993919aaea42a6539bd7bf20b0b255cbf0fe,` | drop rgba(0,0,0,0.22) 3px 5px 30px |

### 컴포넌트 (`🎨 Foundations` > `foundations / components`, 총 36 COMPONENT)

| 이름                  | 종류      | 노드 ID  | key                                        | variants (이름 → 노드 ID)                                                                                                                                        |
| --------------------- | --------- | -------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| button-primary        | SET       | `20:119` | `25aa9b3ebaf7251095e503806156f3f42c1a3917` | State=default,Size=default `20:111` · State=active,Size=default `20:113` · State=default,Size=compact `20:115` · State=active,Size=compact `20:117`              |
| button-secondary-pill | SET       | `20:126` | `19227016f422f846a2b72a525c1d47e7b5f5666d` | Size=default `20:122` · Size=compact `20:124`                                                                                                                    |
| button-dark-utility   | COMPONENT | `20:129` | `dee44d59d1cfdd154af991ec4b557e83b0a3a50a` | —                                                                                                                                                                |
| button-icon-circular  | SET       | `20:236` | `f0cc3a41b25ddaab83e39ecf4480549dc52e8b11` | Size=44 `20:230` · Size=32 `20:233`                                                                                                                              |
| text-link             | SET       | `20:243` | `a63270fe516ec5de125a16f91b13d13d72c4914d` | Size=body `20:239` · Size=caption `20:241`                                                                                                                       |
| status-chip           | SET       | `20:434` | `cf4121be63f2d19da293f556fd2aba2c9421a194` | State=default `20:430` · State=selected `20:432`                                                                                                                 |
| list-row              | SET       | `22:91`  | `ea858f56f168dc209db779d7ef3bf4c68ec7ab1c` | Trailing=caption `22:76` · Trailing=chevron `22:81` · Trailing=none `22:87`                                                                                      |
| input                 | SET       | `22:98`  | `e0f7901ddbee1bf407d7402fb25437843fad6ffa` | State=empty `22:94` · State=filled `22:96`                                                                                                                       |
| card                  | COMPONENT | `22:101` | `0f1cf5a4eee1bdfe063fa4483918533c0a76fba1` | —                                                                                                                                                                |
| mobile-header         | SET       | `22:498` | `a4db1d4f8bdb7eb1df2377035fa7ead76e16fc8a` | Left=title,Right=cta `22:468` · Left=title,Right=none `22:475` · Left=back,Right=cta `22:480` · Left=back,Right=none `22:490`                                    |
| mobile-tab-bar / tab  | SET       | `25:172` | `95ccc4763624d2fe07017b5fafd4ad01e793a9c2` | State=active × Icon=calendar `25:136` / list.bullet `25:141` / person.2 `25:148` · State=inactive × calendar `25:154` / list.bullet `25:159` / person.2 `25:166` |
| mobile-tab-bar        | SET       | `25:236` | `0b597577d221bb4d8f0fcc8314aaf514f54bfa63` | Active=calendar `25:173` · Active=meetings `25:194` · Active=contacts `25:215`                                                                                   |
| mobile-sticky-cta     | SET       | `25:500` | `750c356a765bb15815bcf7257f88aa68942b977d` | Left=summary `25:487` · Left=link `25:493`                                                                                                                       |
| section-dark          | COMPONENT | `25:503` | `8a4bb3c087ed43972e610157d465045f29de4797` | —                                                                                                                                                                |
| empty-state           | COMPONENT | `28:473` | `c6fb84cbdef2a985d66a73054caa328ebac488f2` | —                                                                                                                                                                |

각 컴포넌트 `description`에 design.md 키·토큰 근거 기록됨. 로컬 컴포넌트이므로 화면 조립 시 `getNodeByIdAsync(id).createInstance()` 사용(같은 파일이라 `importComponentByKeyAsync` 불필요).

### 자체 검증 (2026-09-05)

| 항목                                         | 결과 |
| -------------------------------------------- | ---- |
| 자동 이름(`Frame N` / `Rectangle N` 등) 노드 | 0    |
| 솔리드 fill 중 변수 미바인딩                 | 0    |
| 솔리드 stroke 중 변수 미바인딩               | 0    |
| 텍스트 노드 중 텍스트 스타일 미적용          | 0    |
| Inter 외 폰트 사용 텍스트                    | 0    |

### 스크린샷

`work/screenshots/foundations.png` (노드 `18:159`, 864×4095)

### 스크린샷 주의 (리뷰어용)

`get_screenshot` 결과에서 한글 텍스트가 간헐적으로 비어 보임(`list-row` chevron/none 변형 title·meta, `empty-state` title/body, `button-primary` label). 노드의 `characters`·fill 바인딩·텍스트 스타일은 정상 렌더된 변형과 동일하게 확인됨(`22:83`,`22:89`,`28:474`,`28:475`). Inter에 한글 글리프가 없어 폴백 폰트가 익스포트 시점에 로드되지 않는 렌더 레이스로 판단 — 같은 노드를 두 번 찍었을 때 비는 텍스트가 매번 달랐음. **데이터 결함 아님.** 화면 리뷰 시 텍스트 공백은 재스크린샷으로 확인할 것.

### 아이콘 교체 필요

`button-icon-circular`, `mobile-tab-bar / tab`(calendar / list.bullet / person.2), `list-row Trailing=chevron`의 아이콘은 SF Symbols 스타일 단색 플레이스홀더. 최종 납품 전 실제 아이콘으로 교체 필요.

## calendar-overview

실행일 2026-09-05. 모드 B 첫 생성. 페이지 `📱 Screens` (`18:103`). **주의:** 동일 화면을 만드는 다른 세션과 충돌 → 사용자 결정 (B)로 이 세션이 소유. 상대 잔해(`calendar-overview` 37:580, `calendar-overview / calendar-cell` 37:622) 삭제 후 처음부터 재생성. 참조 `Hi Fi- Mockups`(15:2019/15:2020)는 건드리지 않음.

### 프레임

| 프레임                     | 노드 ID  | 크기       | 위치              | 비고                                      |
| -------------------------- | -------- | ---------- | ----------------- | ----------------------------------------- |
| `calendar-overview`        | `41:652` | 390 × 1038 | x 60093, y -27302 | 세로 HUG(스크롤 화면, 본문 minHeight 662) |
| `calendar-overview--empty` | `42:615` | 390 × 844  | x 60563, y -27302 | 헤더·필터·탭바 동일, 본문 = `empty-state` |

링크: https://www.figma.com/design/dyqBJHi5EN92veBmDgLjx8/design?node-id=41-652 · https://www.figma.com/design/dyqBJHi5EN92veBmDgLjx8/design?node-id=42-615

### 블록 → 노드

| 블록  | 노드                                                                    | ID                 | 내용                                                                                                                                                                                                                           |
| ----- | ----------------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 헤더  | `calendar-overview / header` (mobile-header Left=title,Right=cta)       | `41:653`           | "우리 일정" / cta "새 모임"                                                                                                                                                                                                    |
| 1·2   | `calendar-overview / filters`                                           | `41:661`           | status-chip ×4 (전체 selected) + caption "결혼식 12월 12일 (토) · D-23" 우정렬                                                                                                                                                 |
| 3     | `calendar-overview / summary / undated-row` (list-row Trailing=chevron) | `41:672`           | "날짜 미정 모임 5건" / "마감 임박 입사 동기 · 마감 22시간", fill `colors/canvas-parchment`                                                                                                                                     |
| 4     | `calendar-overview / calendar / month-nav`                              | `41:985`           | 좌 tagline "2026년 11월" / 우 controls: button-icon-circular 32 ×2 (`next` = `41:994`, detach 후 좌우 반전)                                                                                                                    |
| 5     | `calendar-overview / calendar / weekdays`                               | `41:997`           | caption muted ×7, 7열 FILL                                                                                                                                                                                                     |
| 6     | `calendar-overview / calendar / grid`                                   | `41:1005`          | 5행 × 7셀 (30일 + 빈 셀 5). 행 사이 1px `colors/hairline`. 오늘 19 `colors/primary`, 지난 날짜 `ink-muted-48`, 선택 28 = parchment 채움 + 2px `primary-focus` + `rounded/sm`. 셀 텍스트 7/8/14/21/22/29 "1건", 28 "2건 · 겹침" |
| 7     | `calendar-overview / selected-day / head`                               | `42:579`           | 다크 바 `colors/surface-tile-1` + `rounded/sm`: tagline "11월 28일 (토)" `body-on-dark` / caption "2건 · 겹침" `body-muted`                                                                                                    |
| 8     | `calendar-overview / selected-day / card / m05`, `/ m04`                | `42:582`, `42:592` | 카드 문법(1px hairline, `rounded/lg`, 패딩 `spacing/md`): 시간·인원 caption muted → 제목 body-strong → status-chip 소유자 + 장소 caption → chevron. time 오름차순 (18:30 대학 후배 → 19:00 동네 친구)                          |
| 9     | `calendar-overview / selected-day / overlap-notice`                     | `42:602`           | "같은 저녁에 2건이에요. 각 모임에서 '날짜 다시 잡기'를 할 수 있어요."                                                                                                                                                          |
| 탭바  | `calendar-overview / tab-bar` (mobile-tab-bar Active=calendar)          | `41:678`           | 달력 활성                                                                                                                                                                                                                      |
| empty | `calendar-overview / empty-state` (in `42:615`)                         | `42:778`           | "첫 모임을 만들어 보세요" / "지인을 묶어 날짜 후보를 보내면, 확정된 모임이 이 달력에 표시돼요." / cta "새 모임 만들기"                                                                                                         |

블록 6→7 간격 32px = body gap `spacing/xs`(8) + selected-day paddingTop `spacing/lg`(24).

### 사용 컴포넌트

mobile-header `22:468` · status-chip `20:430`/`20:432` · list-row `22:81` · button-icon-circular Size=32 `20:233` · mobile-tab-bar Active=calendar `25:173` · empty-state `28:473`.

### 조합 컴포넌트 (부록 C 권한 내, 토큰만 사용)

- **달력 그리드**: 7열 FILL 셀(세로 auto-layout, 패딩 `spacing/xxs`, minHeight 44, caption-strong 숫자 + caption 셀 텍스트), 행 하단 1px `colors/hairline`.
- **선택 날짜 다크 바**: `colors/surface-tile-1` 배경, `rounded/sm`, 패딩 `spacing/sm`×`spacing/md`, 텍스트 `body-on-dark`/`body-muted`. (`section-dark`의 48px 패딩은 과해 카드 규모로 축소.)
- **모임 카드**: `list-row`에 chip을 넣을 수 없어 `card` 스펙(1px hairline, `rounded/lg`, 패딩 17)으로 조합 + `status-chip` 인스턴스 + `list-row Trailing=chevron`의 chevron 프레임 clone.

### 참조 반영 (`15:2020` `Screen-1 (Agenda)`, 사용자 지시)

- 가져옴: 월 헤딩 좌정렬 + 이전/다음 컨트롤 우측 그룹 / 선택 셀 = 배경 채움 + 테두리 + 둥근 모서리 / 선택 날짜를 전폭 다크 배너로 / 선택일 모임을 카드 목록(시간 → 제목 → 장소)으로.
- 가져오지 않음(design.md 충돌): Lato·Almarai 폰트, 청록·파랑·주황 점(모임 색 구분 금지), 카드 좌측 컬러 바, 검정 라운드 패널, 플로팅 `+` FAB(IA 고정: 헤더 "새 모임" + 탭바 유지). 주 스트립 대신 월 그리드 유지(겹침 탐색이 PRD 핵심).
- 참조는 design.md와 근본적으로 다른 시각 언어(다른 팔레트·폰트 시스템) → 시각은 design.md 준수.

### 자체 검증

| 항목                        | default `41:652` | empty `42:615` |
| --------------------------- | ---------------- | -------------- |
| 자동 이름 노드              | 0                | 0              |
| 솔리드 fill 변수 미바인딩   | 0                | 0              |
| 솔리드 stroke 변수 미바인딩 | 0                | 0              |
| 텍스트 스타일 미적용        | 0                | 0              |
| Inter 외 폰트               | 0                | 0              |

### 스크린샷

`work/screenshots/calendar-overview.png` (390×1038). 헤더 제목·cta·카운트다운·요약 행·안내문의 한글이 비어 보이는 것은 Foundations 로그의 렌더 레이스(Inter 한글 글리프 폴백)와 동일 — `characters`는 정상. 리뷰 시 재스크린샷 요망.

### 아이콘 교체 필요

`month-nav / next` (`41:994`)는 `button-icon-circular` 인스턴스를 detach 후 chevron.left를 좌우 반전한 프레임 — 실제 chevron.right 아이콘으로 교체 필요. prev/tab-bar/chevron은 Foundations 플레이스홀더 그대로.

### 변경 이력

- **2026-09-05 (리뷰 meeting-create #1 A5/A8, 다른 세션 동의 후)**
  - A8 `status-chip` 변형 `20:430`·`20:432`: `minHeight` 32 + 세로 CENTER (패딩 4×12 유지, 높이 28→32). 세트 `20:434` description에 이력 추가. 공유 컴포넌트라 `calendar-overview` 등 모든 chip 인스턴스 높이 자동 반영.
  - A5 조합 컴포넌트 **`list-row-selectable`** 신설 (기존 컴포넌트 수정 없음, 추가만): 섹션 프레임 `foundations / list-row-selectable` `49:1652`(라벨 `49:1653`) > 세트 `49:1654`, key `341e781c25e3978bfb7383242d90baa943941b5f`, 변형 `Selected=false` `49:1628` · `Selected=true` `49:1639`. 스펙: 390 폭, pl/pr `spacing/lg`, pt/pb `spacing/sm`, gap `spacing/md`, minHeight 44, bg `colors/canvas`(true: `colors/canvas-parchment`), 하단 1px `colors/hairline`; lead = title `body-strong` `colors/ink` + meta WRAP[`status-chip` 슬롯 chip-1/chip-2 + caption `caption` `colors/ink-muted-48`]; 우측 24px 아이콘(false: circle `ink-muted-48` 1.5px / true: checkmark.circle.fill `ink` + check `canvas`). 프로퍼티: `title#49:0` TEXT, `caption#49:3` TEXT, `Show caption#49:6` BOOL, `Show chip-2#49:9` BOOL, `Selected` VARIANT. 중첩 chip 라벨은 chip-1/chip-2 인스턴스의 `label#20:12`로 오버라이드. 아이콘 교체 필요(SF Symbols).

## meeting-create

실행일 2026-09-05. 모드 B 첫 생성 (기존 동명 노드 없음). `📱 Screens`(`18:103`), `calendar-overview` 오른쪽 +80.

### 프레임

| 프레임                  | 노드 ID  | 크기       | 위치 (x, y)   | 링크                                                                      |
| ----------------------- | -------- | ---------- | ------------- | ------------------------------------------------------------------------- |
| `meeting-create`        | `42:603` | 390 × 1202 | 60563, -27302 | https://www.figma.com/design/dyqBJHi5EN92veBmDgLjx8/design?node-id=42-603 |
| `meeting-create--empty` | `43:991` | 390 × 696  | 61465, -27302 | https://www.figma.com/design/dyqBJHi5EN92veBmDgLjx8/design?node-id=43-991 |

세로 HUG(스크롤 화면), 배경 `colors/canvas` 바인딩. 주요 컨테이너: header `42:604` · content `42:614` · members `42:1125` · rows `42:1142` · sticky-cta `43:985`.

### 사용 컴포넌트 (Foundations 인스턴스)

| 블록              | 컴포넌트 (변형 노드)                                  | 오버라이드                                                            |
| ----------------- | ----------------------------------------------------- | --------------------------------------------------------------------- |
| header            | `mobile-header` Left=back,Right=none `22:490`         | 내부 `title` 텍스트 visible=false (와이어: 뒤로가기만, 제목 없음)     |
| 2 모임 이름       | `input` State=filled `22:96`                          | value "옆 팀 동료"                                                    |
| 3 소유자          | `status-chip` selected `20:432` / default `20:430` ×3 | "신부"(selected) "신랑" "공동"                                        |
| 5 검색            | `input` State=empty `22:94`                           | value "이름으로 찾기"                                                 |
| 6 그룹 필터       | `status-chip` ×5 (직장 동료 selected)                 | 가로 스크롤 = FILL 폭 + clipsContent (5번째 "가족" 잘림은 의도)       |
| 8 지인 행 메타 칩 | `status-chip` default ×8                              | 그룹 이름                                                             |
| sticky            | `mobile-sticky-cta` Left=summary `25:487`             | summary "2명 선택", 중첩 `button-primary` label "다음: 날짜 후보"     |
| empty 본문        | `empty-state` `28:473`                                | "고를 지인이 없어요" / "먼저 지인을 등록해 주세요." / cta "지인 추가" |

텍스트 스타일: 제목 `display-md`, 섹션 헤드 `tagline`, 행 제목 `body-strong`, 라벨·카운트·메타 `caption`. 색: 제목/행 제목 `colors/ink`, 라벨·메타·카운트·미선택 원 `colors/ink-muted-48`(`colors/body-muted`는 0.8 회색이라 흰 배경에서 부적합해 미사용).

### 조합 컴포넌트 — 선택 아이콘 행 (`meeting-create / members / rows / {pid}`)

`list-row` 인스턴스는 meta가 단일 텍스트 prop이라 칩+caption 조합 불가 → `list-row` 스펙(A-4: 배경 canvas, 하단 1px `colors/hairline`, 세로 패딩 `spacing/sm`, minHeight 44)을 auto-layout 프레임으로 재현. 구조: `lead`(title body-strong + `meta` WRAP[chip…, caption]) + 우측 24px 아이콘. 선택 행(p12 `43:646`, p13 `43:666`)은 배경 `colors/canvas-parchment` + `icon-checkmark.circle.fill`(ellipse fill ink + check vector stroke `colors/canvas`), 미선택은 `icon-circle`(ellipse stroke ink-muted-48 1.5px). 행 순서·메타는 와이어 그대로(p03 칩 2개 · p14 "따로 만나기" · p13 caption 없음). 하이라이트는 content 좌우 패딩 24 안쪽만 칠해짐(풀블리드 아님) — 리뷰어 판단 요망.

블록 9 경고 caption·both·separate-warning·error·search-empty 상태는 와이어 규칙대로 생성하지 않음(default 숨김 / empty만 별도 프레임).

### 자체 검증 (2026-09-05, 두 프레임 모두)

| 항목                                              | meeting-create | --empty |
| ------------------------------------------------- | -------------- | ------- |
| 자동 이름(`Frame N`/`Rectangle N`/…) 노드         | 0              | 0       |
| 솔리드 fill 중 변수 미바인딩 (인스턴스 내부 제외) | 0              | 0       |
| 솔리드 stroke 중 변수 미바인딩                    | 0              | 0       |
| 텍스트 노드 중 텍스트 스타일 미적용               | 0              | 0       |
| Inter 외 폰트                                     | 0              | 0       |

### 스크린샷

`work/screenshots/meeting-create.png` (390×1202) · `work/screenshots/meeting-create--empty.png` (390×696).
렌더 메모: 첫 생성된 행 제목 4개(p03·p12·p10·p13)가 `characters`·스타일 정상인데도 반복 렌더에서 비어 보였음(Foundations 로그의 한글 폴백 레이스와 동일 증상). 같은 속성으로 텍스트 노드를 재생성(`44:670`~`44:673`)하니 렌더됨 — 최종 스크린샷은 7행 모두 표시.

### 아이콘 교체 필요

행 우측 `icon-checkmark.circle.fill` / `icon-circle`은 ellipse + SVG 체크 플레이스홀더 — SF Symbols `checkmark.circle.fill` / `circle`로 교체 필요. 검색 input에 돋보기 아이콘 없음(Foundations `input` 컴포넌트에 아이콘 슬롯 없음). 헤더 chevron.left는 Foundations 플레이스홀더 그대로.

## meeting-dates

실행일 2026-09-05. 모드 B 첫 생성 (기존 동명 노드 없음). `📱 Screens`(`18:103`), 생성 직전 페이지 재스캔 후 최우측 노드 오른쪽 +80.

### 프레임

| 프레임                 | 노드 ID   | 크기      | 위치 (x, y)   | 링크                                                                       |
| ---------------------- | --------- | --------- | ------------- | -------------------------------------------------------------------------- |
| `meeting-dates`        | `45:678`  | 390 × 900 | 61935, -27302 | https://www.figma.com/design/dyqBJHi5EN92veBmDgLjx8/design?node-id=45-678  |
| `meeting-dates--empty` | `45:1199` | 390 × 844 | 62405, -27302 | https://www.figma.com/design/dyqBJHi5EN92veBmDgLjx8/design?node-id=45-1199 |

default는 콘텐츠(후보 3개 + 마감 + 안내 2줄)가 844를 넘어 세로 HUG(900). empty는 844 고정 + content FILL. 배경 `colors/canvas` 바인딩. 주요 컨테이너: header `45:679` · content `45:687` · candidates `45:691` (head `45:692`, rows `45:695`) · deadline `45:749` · sticky-cta `45:765`.

### 블록 → 노드 (default)

| 블록   | 노드                                                          | ID                                  | 내용                                                                                                         |
| ------ | ------------------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 헤더   | `meeting-dates / header` (mobile-header Left=back,Right=none) | `45:679`                            | 내부 `title` visible=false (뒤로가기만)                                                                      |
| 1      | `meeting-dates / title-block`                                 | `45:688` (title `45:1471`)          | display-md "날짜 후보" / caption muted "대학 동기 · 7명"                                                     |
| 2      | `meeting-dates / candidates / head`                           | `45:692`                            | tagline "후보" / caption muted "3/5" (SPACE_BETWEEN)                                                         |
| 3      | `meeting-dates / candidates / rows / c1·c2·c3`                | `45:696` · `45:702` · `45:707`      | 조합 list-row(아래) + `text-link` Size=caption "삭제". c1·c3 메타 caption `colors/ink`                       |
| 4      | `meeting-dates / candidates / add`                            | `45:713`                            | button-secondary-pill Size=default, FILL 폭, "+ 후보 추가"                                                   |
| 5      | `meeting-dates / deadline / title`                            | in `45:749`                         | tagline "회신 마감", 섹션 paddingTop `spacing/xl`                                                            |
| 6      | `meeting-dates / deadline / presets / chip-*`                 | `45:752` `45:754` `45:756` `45:758` | status-chip "24시간" "3일" "7일" default / "직접" selected                                                   |
| 6 입력 | `meeting-dates / deadline / custom-input`                     | `45:760`                            | input State=filled "11월 18일 (수) 23:59"                                                                    |
| 7      | `meeting-dates / deadline / hint`                             | `45:762`                            | caption `ink-muted-48`                                                                                       |
| 8      | `meeting-dates / share-hint`                                  | `45:764`                            | caption `ink-muted-48`, content 마지막                                                                       |
| 스티키 | `meeting-dates / sticky-cta` (Left=summary)                   | `45:765` (cta `I45:765;25:490`)     | "후보 3개 · 마감 11/18" / button-primary "링크 보내기"                                                       |
| empty  | `meeting-dates--empty / candidates / empty-caption`           | `45:1257`                           | rows 대신 caption muted "아직 후보가 없어요. 1개만 넣어도 보낼 수 있어요." · count "0/5" · 스티키 "후보 0개" |

4a(adding) · urgent · error · resend 상태는 와이어 규칙대로 생성하지 않음(default + empty만).

### 사용 컴포넌트 (Foundations 인스턴스)

mobile-header `22:490` · text-link Size=caption `20:241` · button-secondary-pill Size=default `20:122` · status-chip `20:430`/`20:432` · input State=filled `22:96` · mobile-sticky-cta Left=summary `25:487` (중첩 button-primary `20:111`).

### 조합 컴포넌트 — 후보 행 (`meeting-dates / candidates / rows / {cid}`)

`meeting-create`의 선택 아이콘 행과 같은 방식: `list-row` 인스턴스에는 우측에 `text-link`를 넣을 수 없어 A-4 list-row 스펙을 auto-layout 프레임으로 재현 — 배경 `colors/canvas`, 하단 1px `colors/hairline`, 세로 패딩 `spacing/sm`, gap `spacing/md`, minHeight 44, `lead`(title body-strong `colors/ink` + meta caption `colors/ink` — 겹침 경고에 경고색·아이콘 없음) + 우측 `text-link` "삭제". c2는 overlapWarning null → meta 없음.

### 자체 검증 (2026-09-05, 두 프레임 모두)

| 항목                                              | meeting-dates | --empty |
| ------------------------------------------------- | ------------- | ------- |
| 자동 이름(`Frame N`/`Rectangle N`/…) 노드         | 0             | 0       |
| 솔리드 fill 중 변수 미바인딩 (인스턴스 내부 제외) | 0             | 0       |
| 솔리드 stroke 중 변수 미바인딩                    | 0             | 0       |
| 텍스트 노드 중 텍스트 스타일 미적용               | 0             | 0       |
| Inter 외 폰트                                     | 0             | 0       |

### 스크린샷

`work/screenshots/meeting-dates.png` (390×900) · `work/screenshots/meeting-dates--empty.png` (390×844).
렌더 메모: 첫 생성한 display-md 제목 "날짜 후보"가 `characters` 정상인데도 비어 렌더됨(Foundations 로그의 한글 폴백 레이스와 동일). 같은 속성으로 텍스트 노드 재생성(`45:1471`, `45:1472`) 후 렌더 확인.

### MCP 메모

헤더 인스턴스 내부 `title`을 `getNodeByIdAsync('I45:679;22:497')` 핸들로 `visible=false` 하면 `The node with id "45:686" does not exist` 오류(2회). `findAllWithCriteria`로 얻은 핸들로는 성공 — 다음 화면에서 참고.

### 아이콘 교체 필요

헤더 chevron.left는 Foundations 플레이스홀더 그대로. 이 화면에 새 아이콘 없음.

### FIX-LOCAL #1 (2026-09-05, `work/reviews/calendar-overview.md` 수정 목록 6항목)

| #   | 항목                                   | 처리                                                                                                                                                                                                                                                                                                                                                                                                                                          | 결과 노드                                                                                                                                                                                                |
| --- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `month-nav / prev` 32→44               | `swapComponent` → `button-icon-circular` Size=44 (`20:230`)                                                                                                                                                                                                                                                                                                                                                                                   | `41:988` (44×44)                                                                                                                                                                                         |
| 2   | `month-nav / next` 32→44               | Size=44 인스턴스 생성 → `detachInstance` → chevron 좌우 반전. 구 `41:994` 삭제                                                                                                                                                                                                                                                                                                                                                                | `45:675` (44×44). month-nav 행 44, CENTER 정렬 유지                                                                                                                                                      |
| 3   | cell-28 텍스트                         | "2건 · 겹침" → **"겹침"** (건수는 head/count에 유지)                                                                                                                                                                                                                                                                                                                                                                                          | `41:1093`. 그리드 5행 모두 46                                                                                                                                                                            |
| 4   | calendar 블록 paddingTop               | `spacing/lg`(24) 바인딩 → 요약 행↔월 헤딩 8+24 = 32                                                                                                                                                                                                                                                                                                                                                                                           | `41:984`                                                                                                                                                                                                 |
| 5   | A5 로컬 컴포넌트화                     | **`calendar-overview / calendar-cell`** variant set `45:790` (State=default `45:775` / past `45:779` / today `45:783` / selected `45:787` / empty `45:789`, 홀더 `45:771`) → 그리드 셀 35개 전부 인스턴스로 교체. **`calendar-overview / meeting-card`** `45:1177` (홀더 `45:1167`) → 카드 2개 인스턴스 `45:1179`(m05) / `45:1189`(m04). 교체 중 empty 변형이 createFrame 기본 100px·행 counter-axis 고정으로 행이 66이 됐던 것을 46으로 복구 | 재사용률 (인스턴스 ÷ 인스턴스+프레임): 리뷰 산식 그대로 0.18 → **0.57** (51/90). 인스턴스 내부 프레임 17개를 빼면 **0.70** (51/73). 남은 자체 프레임 22개는 body·섹션·행·status-bar 등 레이아웃 컨테이너 |
| 6   | A7 `calendar-overview--no-meeting-day` | default 복제 → 셀 28 default 변형("겹침" 유지), 셀 19 selected 변형 + 숫자 `colors/primary`, head "11월 19일 (목)" + count 공백, 카드·안내 제거 → caption `ink-muted-48` "이 날 확정된 모임이 없어요"                                                                                                                                                                                                                                         | `45:1258` (390×844, x 61465). `--empty` 오른쪽                                                                                                                                                           |

리뷰 지적 로그 오기 정정: 헤더 `41:653` → `15:4101`, 탭바 `41:678` → `15:4069` (둘 다 `41:652` 안의 자식임을 확인 후 위 표 정정).

#### 사용자 지시: 상태바·네비 보완 (3개 상태 프레임 공통)

- **상태바** `calendar-overview / status-bar` (default `45:715` / empty `45:732` / no-meeting-day는 복제본): 프레임 최상단 절대 위치 오버레이 390×47 (헤더 컴포넌트 미수정). 좌 `time` "9:41" `typography/caption-strong` `colors/ink`, 패딩 좌우 `spacing/lg`. 우 `icons`(gap `spacing/xs`): `signal`/`wifi`/`battery` SVG 단색 벡터, fill·stroke `colors/ink` 바인딩. **아이콘 교체 필요**(플레이스홀더).
- **홈 인디케이터** `calendar-overview / tab-bar / home-indicator` (default `45:731` / empty `45:748` / no-meeting-day 복제본): 134×5 사각형, `rounded/pill`, `colors/on-dark`, 절대 위치 하단 8px·가로 중앙(constraints CENTER/MAX). 탭바 컴포넌트 미수정.
- **헤더 점검**: 제목 "우리 일정" `colors/ink` x=24, CTA "새 모임" `colors/on-primary` 우측 여백 24 — 정상.
- **탭바 점검**: "달력" `colors/on-dark`(활성) / "모임"·"지인" `colors/ink-muted-48`, 아이콘 벡터 9개 — 정상.
- 3개 프레임(`41:652`, `42:615`, `45:1258`) 모두 동일 상태바·헤더·탭바·홈 인디케이터.

#### 자체 검증 (FIX-LOCAL #1 후)

| 항목                        | default `41:652` | empty `42:615` | no-meeting-day `45:1258` | 컴포넌트 홀더 2개 |
| --------------------------- | ---------------- | -------------- | ------------------------ | ----------------- |
| 자동 이름                   | 0                | 0              | 0                        | 0                 |
| 솔리드 fill/stroke 미바인딩 | 0/0              | 0/0            | 0/0                      | 0/0               |
| 텍스트 스타일 미적용        | 0                | 0              | 0                        | 0                 |
| Inter 외 폰트               | 0                | 0              | 0                        | 0                 |
| 높이                        | 1054 (HUG)       | 844            | 844                      | —                 |

스크린샷: `work/screenshots/calendar-overview.fix-1.png` (390×1054). 한글 글리프 공백은 기존 렌더 레이스 — `characters` 정상.

### FIX-LOCAL #1 적용 (2026-09-05)

리뷰 `work/reviews/meeting-create.md` 수정 목록 전부 적용 (A5·A8은 다른 세션 동의 후 진행).

| 항목           | 적용 내용                                                                                                                                                                                                                                                   | 변경 노드                                                                                                                                      |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| C3·C6 풀블리드 | `content` pl/pr 0 + CENTER, title/name/owner FIXED 342, `members` FILL+CENTER, `head` FILL + pl/pr `spacing/lg`, `search` FIXED 342, `group-filter` FILL 390 + pl/pr `spacing/lg` + clipsContent(칩이 화면 가장자리에서 잘림), `rows` FILL 390. 새 프레임 0 | `42:614` `42:1111` `42:1112` `42:1116` `42:1125` `42:1126` `42:1129` `42:1131` `42:1142` / --empty `43:1000` `43:1001` `43:1002` `43:1006`     |
| C4             | 7행 caption "'직장 팀'에 편성됨"으로 축약 → p03 행 2줄(h 81), wrap 없음                                                                                                                                                                                     | (행 교체로 인스턴스 prop `caption#49:3`에 반영)                                                                                                |
| A8             | Foundations `status-chip` minHeight 32 (Foundations 변경 이력 참조) — 이 화면 chip 인스턴스 자동 반영                                                                                                                                                       | `20:430` `20:432`                                                                                                                              |
| A5             | `list-row-selectable` 신설 후 raw 행 → 인스턴스 교체. 래퍼 프레임 추가 없음                                                                                                                                                                                 | default `49:1655` `49:1666` `49:1679` `49:1690` `49:1703` `49:1714` `49:1725` (raw `43:635`~`43:976` 삭제). 상태 프레임 4개 행도 동일 인스턴스 |
| A7             | 상태 프레임 4개 = `42:603` clone 후 차이만 수정, 레이어 접두사 각 프레임 id                                                                                                                                                                                 | 아래 표                                                                                                                                        |

| 새 프레임                          | 노드 ID   | 크기     | 차이                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `meeting-create--separate-warning` | `49:1164` | 390×1271 | p14 조은비 Selected=true(`49:1813`), head/sticky "3명 선택", 블록 9 caption `colors/ink` `49:2122` (rows 아래·sticky 위)                                                                                                                                                                                                                         |
| `meeting-create--both`             | `49:1280` | 390×971  | 소유자 "공동" selected, 이름 "상견례", group-filter 9칩("전체" selected + "대학 동기·신부"… "러닝 크루·신랑 · 모임 없음" 등, 추가 칩 `49:2127`~`49:2133`), 행 4개 p22 한정우·p23 이미경·p40 김영호·p41 박순자 (`49:1835` `49:1846` `49:1859` `49:1870`, 첫 칩 sideLabel + "가족", 전부 선택, 편성 caption 없음 = 지금 편성 중인 m09), "4명 선택" |
| `meeting-create--error`            | `49:1396` | 390×1242 | 이름 input State=empty "예: 대학 동기"(`49:1402`) + caption `colors/ink` "모임 이름을 입력해 주세요" `49:2160`                                                                                                                                                                                                                                   |
| `meeting-create--search-empty`     | `49:1512` | 390×679  | 검색 input State=filled "박"(`49:1529`), rows → caption `ink-muted-48` "'박'에 해당하는 지인이 없어요" `49:2162`                                                                                                                                                                                                                                 |

배치: `43:991` 오른쪽, 재스캔 시점 최우측 +80 순차 (x 62875 / 63345 / 63815 / 64285). 다른 세션 프레임(`meeting-dates*`, `meeting-detail`, `calendar-overview*`)은 읽기만 함.

자체 검증 (6프레임 모두): 자동 이름 0 / 미바인딩 fill·stroke 0 / 스타일 미적용 텍스트 0 / Inter 외 0. 인스턴스 비율(인스턴스 ÷ (인스턴스 + raw 프레임)): default 0.70 · separate-warning 0.70 · both 0.71 · error 0.70 · empty 0.64 · search-empty 0.60 (empty·search-empty는 행 0개라 분모의 레이아웃 컨테이너 비중이 커짐 — 리뷰어 판단 요망).

스크린샷 갱신: `work/screenshots/meeting-create.png`(1214) · `--empty.png`(700) · `--separate-warning.png`(1271) · `--both.png`(971) · `--error.png`(1242) · `--search-empty.png`(679). 렌더 메모: default의 이름 input 값·검색 placeholder, --both의 "새 모임" 제목이 익스포트에서 비어 보임 — `characters` 정상(한글 폴백 렌더 레이스, Foundations 로그 참조). 리뷰 시 재스크린샷 요망.

### FIX-LOCAL #2 (2026-09-05, 리뷰 2회차 수정 목록 2항목 + 사용자 지시 1건)

| #   | 항목                                                                               | 처리                                                                                                                                                                                                                                                                 | 결과                                                              |
| --- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 1   | A4 status-bar `paddingTop 14`                                                      | 3개 프레임 status-bar(`45:715` / `45:732` / `45:1334`) paddingTop·Bottom 0, 높이 47 고정 컨테이너 + `counterAxisAlignItems=CENTER`로 세로 위치 결정                                                                                                                  | 자체 프레임 비토큰 padding/gap 0 (3프레임)                        |
| 2   | A5 고아 마스터                                                                     | `calendar-overview / calendar-cell`(`45:790`)·`meeting-card`(`45:1177`)가 parent 없음 확인 → `📱 Screens`에 **`calendar-overview / _components`** `50:1302` (x 65225, y -27302, 최우측+80) 생성 후 `appendChild`로 이동. variant set 자체 padding/gap 16 → 24로 정정 | default 프레임 인스턴스 37개 연결 유지 확인                       |
| +   | 사용자 지시(부록 A-1 `{component.status-bar}` / `{component.home-indicator}` 추가) | 홈 인디케이터 레이어명 `calendar-overview / tab-bar / home-indicator` → **`calendar-overview / home-indicator`** (`45:731` / `45:748` / `45:1350`), 위치·속성 그대로. 상태바 이름 `calendar-overview / status-bar` 유지                                              | 색 확인: 상태바 time `colors/ink`, 홈 인디케이터 `colors/on-dark` |

참고: default 프레임 높이 1054 → 1066은 다른 세션의 Foundations `status-chip` minHeight 28→32 반영(칩 행 +4, 카드 칩 2개 +8). 칩 오버라이드 없음.

#### 자체 검증 (FIX-LOCAL #2 후)

| 항목                                 | `41:652`   | `42:615` | `45:1258` | `_components` `50:1302` |
| ------------------------------------ | ---------- | -------- | --------- | ----------------------- |
| 자동 이름                            | 0          | 0        | 0         | 0                       |
| 솔리드 fill/stroke 미바인딩          | 0/0        | 0/0      | 0/0       | 0/0                     |
| 텍스트 스타일 미적용 / Inter 외 폰트 | 0/0        | 0/0      | 0/0       | 0/0                     |
| 자체 프레임 비토큰 padding·gap       | 0          | 0        | 0         | 0 (16→24 정정 후)       |
| 높이                                 | 1066 (HUG) | 844      | 844       | 289                     |

스크린샷: `work/screenshots/calendar-overview.fix-2.png` (390×1066).

## meeting-detail

실행일 2026-09-05. 모드 B 첫 생성 (기존 동명 노드 없음). `📱 Screens`(`18:103`), 생성 직전 페이지 재스캔 후 최우측(`meeting-create--search-empty` 64285+390) 오른쪽 +80. 와이어 `## 상태` "03은 default 1개만" → `--empty` 등 상태 프레임 없음.

### 프레임

| 프레임           | 노드 ID   | 크기       | 위치 (x, y)   | 링크                                                                       |
| ---------------- | --------- | ---------- | ------------- | -------------------------------------------------------------------------- |
| `meeting-detail` | `49:1736` | 390 × 1450 | 64755, -27302 | https://www.figma.com/design/dyqBJHi5EN92veBmDgLjx8/design?node-id=49-1736 |

세로 HUG(스크롤 화면), 배경 `colors/canvas` 바인딩, 프레임·content `counterAxisAlignItems` CENTER, content pl/pr 0(풀블리드) + 각 블록이 자체 pl/pr `spacing/lg`. 첫 844 안에 블록 1~~3(제목 y99~~241 · summary 241~~422 · 미회신자 422~~550) 포함. 주요 컨테이너: header `49:1737` · content `49:1745` · sticky-cta `50:1293` · status-bar `50:1303` · home-indicator `50:1319`.

### 블록 → 노드

| 블록   | 노드                                                           | ID                                         | 내용                                                                                                                                                                                                                                                                                                                                                                                  |
| ------ | -------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 상태바 | `meeting-detail / status-bar` (절대 위치 390×47, 헤더 위)      | `50:1303`                                  | 좌 "9:41" caption-strong `colors/ink` / 우 `icons` signal·wifi·battery SVG 단색 벡터(fill·stroke `colors/ink`) — 부록 A-1 `{component.status-bar}`                                                                                                                                                                                                                                    |
| 헤더   | `meeting-detail / header` (mobile-header Left=back,Right=none) | `49:1737`                                  | 내부 `title` visible=false (뒤로가기만)                                                                                                                                                                                                                                                                                                                                               |
| 1      | `meeting-detail / title-block`                                 | `49:1746` (title `49:1747`)                | display-md "대학 동기" / meta: status-chip "신부" `49:1749` + "확정 대기" `49:1751` + caption muted "7명" `49:1753`. 패딩 `spacing/lg` 4방향, gap `spacing/sm`                                                                                                                                                                                                                        |
| 2      | `meeting-detail / summary` (section-dark)                      | `49:1997`                                  | props headline "회신 6/7" / body "마감 지남 · 11월 18일 (수) 23:59" / caption "가장 많이 가능한 후보 11월 29일 (일) 저녁 · 6명". 390 풀블리드, 블록 1·3과 간격 0                                                                                                                                                                                                                      |
| 3      | `meeting-detail / unreplied`                                   | `49:2001` (head `49:2002`, row `49:2005`)  | head tagline "아직 답이 없어요" + caption muted "1명" SPACE_BETWEEN / 조합 행 p11: title "오준호" + meta "대학 동기 · 복학 동기" + `button-secondary-pill` compact "리마인드" `49:2009`                                                                                                                                                                                               |
| 4      | `meeting-detail / candidates`                                  | `49:2092` (rows `49:2094`)                 | tagline "후보별 회신" / `list-row Trailing=caption` ×3: c1 `49:2095` · c2 `49:2100`(meta null → `meta` visible=false) · c3 `49:2105`(title 뒤 " · 가장 많음" 범위에 caption-strong). trailing "가능 3 · 불가 3" / "가능 3 · 불가 3" / "가능 6 · 불가 0". 겹침 caption c1·c3. paddingTop `spacing/xl`                                                                                  |
| 5      | `meeting-detail / members`                                     | `50:1250` (head `50:1251`, rows `50:1256`) | head tagline "구성원 7명" + `text-link` Size=caption "구성원 변경" `50:1253` / 범례 caption muted `50:1633` / `list-row Trailing=caption` ×7 — p11 `50:1257`(meta "미회신", "· · ·") 먼저, 이후 p01 `50:1262` p02 `50:1267` p04 `50:1272` p05 `50:1277`(memo) p06 `50:1282` p07 `50:1287`. trailing 텍스트 스타일 `body`로 오버라이드(기호 판독), meta 없는 행은 `meta` visible=false |
| 6      | `meeting-detail / note`                                        | `50:1634`                                  | caption muted "메모 · 민아는 직장 팀 모임에 넣기로 함" (members 블록 마지막, paddingBottom `spacing/lg`)                                                                                                                                                                                                                                                                              |
| 스티키 | `meeting-detail / sticky-cta` (mobile-sticky-cta Left=link)    | `50:1293`                                  | 중첩 `text-link` "마감 연장" / 중첩 `button-primary` "확정하기" (ready 상태)                                                                                                                                                                                                                                                                                                          |
| 홈     | `meeting-detail / home-indicator` (절대 위치, 하단 8px 중앙)   | `50:1319`                                  | 134×5, `rounded/pill`, `colors/ink` — 부록 A-1 `{component.home-indicator}`                                                                                                                                                                                                                                                                                                           |

### 사용 컴포넌트 (Foundations 인스턴스, 총 20)

mobile-header `22:490` · status-chip default `20:430` ×2 · section-dark `25:503` · button-secondary-pill Size=compact `20:124` · list-row Trailing=caption `22:76` ×10 · text-link Size=caption `20:241` · mobile-sticky-cta Left=link `25:493` (중첩 text-link `20:239` + button-primary `20:111`).

### 조합 컴포넌트 (부록 C 권한 내)

- **미회신자 행** (`unreplied / row / p11`, 1개): `list-row`에 우측 pill을 넣을 수 없어 A-4 list-row 스펙(배경 `colors/canvas`, 하단 1px `colors/hairline`, 세로 패딩 `spacing/sm`, gap `spacing/md`, minHeight 44)을 auto-layout으로 재현 + `button-secondary-pill` compact. 1개뿐이라 컴포넌트 승격 안 함(meeting-dates와 동일 방식).
- 그 외 행 10개는 전부 `list-row` 인스턴스 (meeting-create 리뷰 A5 반영).
- **기호 행**: `replyMarks` 문자열을 trailing prop에 넣고 텍스트 스타일만 `body`로 오버라이드. 와이어의 "기호 간 `spacing/sm`"은 텍스트 prop 안이라 공백 문자로 대체(letterSpacing 오버라이드는 스타일 detach를 유발해 사용 안 함).

### 자체 검증 (2026-09-05)

| 항목                                                | meeting-detail `49:1736`                                                                                                                                      |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 자동 이름(`Frame N`/`Rectangle N`/`Vector N`…) 노드 | 0                                                                                                                                                             |
| 솔리드 fill 중 변수 미바인딩 (visible 기준)         | 0                                                                                                                                                             |
| 솔리드 stroke 중 변수 미바인딩                      | 0                                                                                                                                                             |
| 텍스트 노드 중 텍스트 스타일 미적용(범위 포함)      | 0                                                                                                                                                             |
| Inter 외 폰트                                       | 0                                                                                                                                                             |
| 재사용률 (인스턴스 ÷ 인스턴스+프레임)               | 20 ÷ (20+33) = 0.38 — 프레임 33개 중 인스턴스 내부·SVG 아이콘 래퍼·레이아웃 컨테이너(fill/stroke 없음). 자체 그린 fill/stroke 보유 프레임은 미회신자 행 1개뿐 |
| 높이                                                | 1450 (HUG)                                                                                                                                                    |

### 스크린샷

`work/screenshots/meeting-detail.png` (390×1450). 첫 렌더에서 범례·메모 caption 한글이 비어 보여 같은 속성으로 텍스트 노드 재생성(`50:1633`, `50:1634`) 후 재촬영 — 전부 표시됨.

### MCP 메모

7행 인스턴스 루프에서 `setProperties` 직후 같은 스크립트 안에서 얻은 `findAllWithCriteria` 핸들로 `.name` 읽기 시 `The node with id "…" does not exist` 1회(스크립트 롤백됨). 인스턴스 생성·`setProperties`를 먼저 전부 끝내고 두 번째 루프에서 `findOne`으로 새 핸들을 잡으니 성공.

### 아이콘 교체 필요

`status-bar / icons / signal·wifi·battery` SVG 플레이스홀더, 헤더 chevron.left는 Foundations 플레이스홀더 그대로.

### status-bar / home-indicator 적용 (2026-09-05, design.md A-1 추가분)

6개 프레임 전부에 헤더 인스턴스 수정 없이 프레임 직속 절대 위치 블록으로 추가 (`calendar-overview / status-bar` 구조와 동일).

- `{id} / status-bar`: 390×47, (0,0), HORIZONTAL SPACE_BETWEEN, pl/pr `spacing/lg`, 좌 `time` "9:41" `caption-strong` `colors/ink`, 우 `icons`(gap `spacing/xs`) = `signal`·`wifi`·`battery` SVG 벡터, fill/stroke `colors/ink` 바인딩(배터리 외곽·꼭지는 변수 + opacity 0.35/0.4).
- `{id} / home-indicator`: 134×5 RECTANGLE, x 128 / y = 높이-13 (safe-bottom 안), radius `rounded/pill`, fill `colors/ink`, constraints CENTER/MAX.

| 프레임 | status-bar | home-indicator |
| --- | --- | --- |
| `meeting-create` `42:603` | `50:1599` | `50:1615` |
| `--empty` `43:991` | `50:1616` | `50:1632` |
| `--separate-warning` `49:1164` | `50:1635` | `50:1651` |
| `--both` `49:1280` | `50:1652` | `50:1668` |
| `--error` `49:1396` | `50:1681` | `50:1697` |
| `--search-empty` `49:1512` | `50:1698` | `50:1714` |

자체 검증 재실행(6프레임): 자동 이름 0 / 미바인딩 fill·stroke 0 / 스타일 미적용 텍스트 0 / Inter 외 0. 스크린샷 6장 재갱신(`work/screenshots/meeting-create*.png`). 상태바 아이콘은 단색 플레이스홀더 — SF Symbols 교체 필요. 렌더 메모: 익스포트에서 "새 모임" 제목 등 한글이 간헐적으로 비어 보임(characters 정상, 폴백 렌더 레이스) — 리뷰 시 재스크린샷.
