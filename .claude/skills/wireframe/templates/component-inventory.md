# Component Inventory

> `wireframe` 스킬 작업 중 관리하는 목록이다. 새 Component를 만들기 전에 이 표에 같은 역할이 있는지 먼저 본다.

한 Component는 한 가지 역할만 맡는다. 같은 데이터와 같은 행동에는 같은 Component를 쓴다.

| Component | 역할 | 담는 정보 | 쓰이는 화면 | Variant / State |
| --- | --- | --- | --- | --- |
| 예: Meeting Card | 모임 정보 표현 | 모임명, 날짜, 참여 인원 | 01 홈, 03 모임 상세 | Default, Selected |
| 예: Primary Button | 주요 행동 | CTA 문구 | 전체 | Default, Disabled, Loading |

## Component 정의

Inventory의 각 Component를 [wireframe.md](wireframe.md) 0절 표기법으로 한 번만 적는다. 화면에서는 `comp "이름"` 한 줄로 참조한다. 텍스트 슬롯은 `slot:이름`으로 표시하고, 인스턴스에서 `이름="값"`으로 덮어쓴다. Figma 에이전트는 이 트리로 Component를 만들고 State는 Variant로 묶는다.

### PrimaryButton

| State | 달라지는 것 |
| --- | --- |
| Default | 아래 트리 |
| Disabled | `bg=line`, 텍스트 `color=muted` |

```
col "PrimaryButton" w=fill h=48 justify=center align=center radius=4 bg=ink
  text slot:label style=subtitle color=bg
```

### DateOption

| State | 달라지는 것 |
| --- | --- |
| Default | 아래 트리 |
| Selected | `border=ink`, Radio 안에 `ink` 점 |

```
row "DateOption" w=fill h=hug pad=12 gap=12 align=center border=line radius=4 bg=surface
  col "Radio" w=20 h=20 border=ink radius=10
  col "Texts" w=fill h=hug gap=4
    text slot:date style=body weight=600
    text slot:count style=caption color=muted
```

## 아이콘

아이콘은 [reference/icons.md](../reference/icons.md)의 Material Symbols Outlined 표에서만 고른다. 의미 하나에 아이콘 하나다. 같은 의미에 다른 이름이 두 개 보이면 하나로 합친다.

| Material 이름 | 의미 | 쓰이는 화면 | 라벨 |
| --- | --- | --- | --- |
| 예: `arrow_back` | 뒤로 가기 | 02 모임 상세, 03 날짜 선택 | 단독 |
| 예: `share` | 초대 링크 공유 | 02 모임 상세 | "공유" 텍스트와 함께 |

## 추가 기록

Inventory에 새 항목을 넣을 때 아래를 적는다.

| Component | 기존 항목으로 해결할 수 없었던 이유 |
| --- | --- |
|  |  |
