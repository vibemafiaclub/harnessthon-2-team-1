# 와이어프레임: <YYYYMMDD>-<slug>

> `wireframe` 스킬 산출물. Figma MCP 에이전트(`figma-generate-design`, `figma-use`)가 이 파일을 읽고 프레임을 만든다. 설계 근거는 [spec.md](spec.md), Component 정의는 [components.md](components.md)에 있다. 맨 아래 "Figma 핸드오프" 절부터 읽으면 만들 것의 전체 목록이 나온다.

## 0. 표기법

이 절은 양식을 그대로 복사한다. 변환 에이전트가 트리를 읽는 규칙이다.

**노드 한 줄**

```
<종류> "<레이어 이름 또는 텍스트>" <속성=값 ...> [@번호]
```

들여쓰기 두 칸이 부모-자식이다. 형제는 위에서 아래 순서로 놓인다. `@번호`는 프레임 아래 Annotation 표의 번호다.

| 종류 | 뜻 | Figma로 옮기면 | 필수 속성 |
| --- | --- | --- | --- |
| `frame` | 최상위 프레임. 화면 하나 × State 하나 | 페이지 위 Frame, Auto Layout 세로 | `w=375`, `h=hug`, `bg=bg` |
| `col` | 세로 Auto Layout 컨테이너 | Frame, layoutMode VERTICAL | `w`, `h` |
| `row` | 가로 Auto Layout 컨테이너 | Frame, layoutMode HORIZONTAL | `w`, `h` |
| `text` | 텍스트. 따옴표 안이 실제 내용 | Text | `style` |
| `icon` | Material Symbols Outlined 아이콘. 따옴표 안이 Material 이름 | 아이콘 라이브러리 인스턴스 또는 벡터 | `size` |
| `image` | 이미지 자리. 대각선 회색 박스 | Rectangle, `surface` 채움 + 대각선 | `w`, `h` |
| `divider` | 1px 가로선 | Line 또는 h=1 Rectangle, `line` 색 | 없음 |
| `comp` | components.md에 정의된 Component의 인스턴스. 따옴표 안이 Component 이름 | Component Instance | 없음. override만 적는다 |

**속성**

| 속성 | 값 | 기본값 | 설명 |
| --- | --- | --- | --- |
| `w`, `h` | `fill` / `hug` / 숫자 | 컨테이너 `w=fill h=hug`, 텍스트 `w=fill h=hug` | 숫자는 pt |
| `pad` | `16` / `12,16` / `8,16,12,16` | `0` | 전체 / 세로,가로 / 위,오른쪽,아래,왼쪽 |
| `gap` | 숫자 | `0` | 자식 사이 간격 |
| `justify` | `start` / `center` / `end` / `between` | `start` | 주축 정렬. `between`은 양끝 배치 |
| `align` | `start` / `center` / `end` | `start` | 교차축 정렬 |
| `bg` | `bg` / `surface` / `ink` | 없음(투명) | 채움 |
| `border` | `line` / `ink` | 없음 | 1px 테두리 |
| `radius` | 숫자 | `0` | 모서리. 버튼과 카드는 4 |
| `style` | `title` / `subtitle` / `body` / `caption` | 텍스트 필수 | 20/600, 16/600, 14/400, 12/400 |
| `color` | `ink` / `muted` / `bg` | `ink` | 텍스트와 아이콘 색 |
| `weight` | `600` | 스타일 기본값 | body나 caption을 굵게 할 때만 |
| `size` | `24` / `20` | 아이콘 필수 | 20은 텍스트 앞 인라인만 |
| `label` | 문자열 | 없음 | 단독 아이콘의 의미. 단독 사용 불가 아이콘은 반드시 옆에 `text`를 둔다 |
| `variant`, `state` | Inventory의 Variant / State 이름 | `Default` | `comp`에만 |
| `<슬롯>=` | 문자열 | 정의값 | `comp`의 텍스트 override. 슬롯 이름은 components.md 정의의 `slot:` 이름 |
| `sticky` | `bottom` / `top` | 없음 | 스크롤과 무관하게 고정. Figma에서는 프레임 끝에 두고 이름에 표시 |

**토큰**

| 토큰 | 값 | 용도 |
| --- | --- | --- |
| `bg` | #FFFFFF | 화면 배경, Primary CTA 글자 |
| `surface` | #F2F2F2 | 면, 입력창, 이미지 자리 |
| `line` | #D9D9D9 | 테두리, 구분선 |
| `ink` | #1A1A1A | 본문, 아이콘, Primary CTA 채움 |
| `muted` | #767676 | 보조 텍스트, 비활성 |
| 폰트 | 시스템 sans-serif | Figma에서는 Pretendard, 없으면 Inter |
| 간격 | 4, 8, 12, 16, 24 | 화면 좌우 16, Section 사이 24, 항목 사이 8 또는 12 |
| 높이 | 버튼 48, 상단 바 56, 터치 최소 44 | |

## 1. 프레임 목록

| 프레임 | 화면 | State | 기준 프레임 | 비고 |
| --- | --- | --- | --- | --- |
| `06 모임 상세 / Default` | SCR-06 | Default (확정대기) | 전체 트리 | |
| `06 모임 상세 / Partial` | SCR-06 | 회신중 | Default 차이 | |

## 2. 프레임: 06 모임 상세 / Default

```
frame "06 모임 상세 / Default" w=375 h=hug bg=bg
  row "TopBar" w=fill h=56 pad=0,8 align=center gap=8
    icon "arrow_back" size=24 label="뒤로 가기"
    text "지수네 청첩장 모임" style=subtitle w=fill
    icon "more_vert" size=24 label="더보기 메뉴"
  col "Body" w=fill h=hug pad=0,16,24,16 gap=24
    col "StatusSection" w=fill h=hug gap=8 @1
      comp "StatusBadge" variant=Filled label="확정대기"
      text "회신 마감 2일 지남 · 미응답 3명" style=body
      comp "TextButton" label="마감 연장" @2
    col "DateOptionList" w=fill h=hug gap=8 @3
      text "날짜 후보" style=subtitle
      comp "DateOption" state=Selected date="10월 12일 (토) 12:00" count="참석 7 · 불참 2"
      row "OverlapWarning" w=fill h=hug pad=8,12 gap=8 bg=surface radius=4 align=start @4
        icon "warning" size=20 color=muted
        text "같은 시간에 '민호네 모임'이 있어요. 확정하면 두 모임이 겹칩니다." style=caption color=muted w=fill
    col "ParticipantSection" w=fill h=hug gap=8 @5
      row "SectionHeader" w=fill h=hug justify=between align=center
        text "참가자 9명" style=subtitle
        text "미응답 3" style=caption color=muted
      comp "ParticipantRow" name="김민수" reply="참석"
      comp "ParticipantRow" name="박서연" reply="불참"
      comp "ParticipantRow" name="이준호" reply="미응답" state=Pending action="제외"
  col "CtaDock" w=fill h=hug pad=12,16,16,16 gap=8 bg=bg sticky=bottom @6
    divider
    comp "PrimaryButton" label="10월 12일 (토) 12:00로 확정"
    comp "TextButton" label="모임 취소"
```

### Annotation

| 번호 | 대상 노드 | 설명 |
| --- | --- | --- |
| 1 | StatusSection | 상태 배지. 마감 도달로 시스템이 회신중에서 확정대기로 바꾼 상태다. 사용자 행동 없이 바뀌므로 배지와 ②가 그 사실을 알린다. |
| 2 | TextButton "마감 연장" | Secondary Action. 마감 정보 옆에 둔다. 자동 제외는 없다 (POL-02). |
| 3 | DateOptionList | Primary 정보. 후보별 집계가 확정 판단의 근거라 참가자 목록보다 위. 후보가 하나라 미리 선택돼 있다. |
| 4 | OverlapWarning | 해당 후보 바로 아래. 확정을 막지 않고 탭 시 확인 다이얼로그로 한 번 더 묻는다 (POL-03, REQ-11). |
| 5 | ParticipantSection | 확정대기에서만 미응답자 행에 "제외"가 보인다. 제외 즉시 집계가 갱신된다. |
| 6 | CtaDock | Primary Action 하나. 선택한 후보 일시가 문구에 들어간다. 모임 취소는 텍스트 버튼으로 위계를 낮춘다. 확정 후 ST-03. |

## 3. 프레임: 06 모임 상세 / Partial

기준: `06 모임 상세 / Default`. 아래 노드만 다르다.

| 대상 노드 | Default | 이 State |
| --- | --- | --- |
| StatusBadge | `variant=Filled label="확정대기"` | `variant=Outline label="회신중"` |
| StatusSection > text | "회신 마감 2일 지남 · 미응답 3명" | "회신 마감까지 3일 · 회신 6/9" |
| TextButton "마감 연장" | 있음 | 없음 |
| ParticipantRow (미응답) | `state=Pending action="제외"` | `state=Pending` (제외 없음) |
| PrimaryButton | `label="10월 12일 (토) 12:00로 확정"` | `state=Disabled label="마감 후 확정할 수 있어요"` |

### Annotation

| 번호 | 대상 노드 | 설명 |
| --- | --- | --- |
| 1 | PrimaryButton | 마감 전에는 확정할 수 없다. Disabled 이유를 버튼 문구로 알린다. |

## 4. Figma 핸드오프

변환 에이전트는 이 절의 순서대로 만든다.

**만드는 순서**

1. 토큰(0절)을 색 변수와 텍스트 스타일로 만든다. 이미 있으면 재사용한다.
2. Component(아래 표)를 components.md의 정의 트리대로 만든다. Variant와 State는 Component Set으로 묶는다.
3. Default 프레임을 트리 순서대로 만든다. 프레임은 가로로 나열하고 사이 간격 80.
4. 차이 표만 있는 State 프레임은 Default 프레임을 복제한 뒤 차이 표를 적용한다.
5. Annotation 표는 프레임 오른쪽에 번호 목록 텍스트로 붙인다.

**프레임**

| 순서 | 프레임 | 기준 |
| --- | --- | --- |
| 1 | `06 모임 상세 / Default` | 전체 트리 |
| 2 | `06 모임 상세 / Partial` | 1 복제 + 차이 |

**Component** (정의는 components.md)

| Component | Variant | State | 텍스트 슬롯 |
| --- | --- | --- | --- |
| PrimaryButton | | Default, Disabled | label |
| TextButton | | Default | label |
| StatusBadge | Filled, Outline | | label |
| DateOption | | Default, Selected | date, count |
| ParticipantRow | | Default, Pending | name, reply, action |

**아이콘** (Material Symbols Outlined. 라이브러리에 없으면 icons.md의 path로 벡터를 만든다)

| Material 이름 | 의미 | 쓰인 프레임 |
| --- | --- | --- |
| arrow_back | 뒤로 가기 | 전체 |
| more_vert | 더보기 메뉴 | 전체 |
| warning | 일정 겹침 주의 | 06 Default, Partial |

**이미지**: 없음. (있으면 `image` 노드 수와 크기를 적는다. 외부 URL은 쓰지 않는다.)

**폰트**: 시스템 sans-serif. Figma에서는 Pretendard, 없으면 Inter. 크기와 굵기는 0절 토큰대로.
