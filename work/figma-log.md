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
