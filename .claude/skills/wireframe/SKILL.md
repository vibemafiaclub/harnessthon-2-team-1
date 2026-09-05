---
name: wireframe
description: PRD, User Flow, IA를 입력받아 MVP 수준의 Mid-fi 와이어프레임을 만든다. "와이어프레임 만들어줘", "화면 구조 잡아줘", "PRD를 화면으로 바꿔줘", "이 플로우 화면별로 그려줘" 같은 요청에 사용한다. 새 기능을 기획하지 않고, 주어진 기획을 정보 위계·UI Pattern·Layout·Action·State로 변환한다.
---

# wireframe

상위기획팀이 넘긴 PRD, User Flow, IA를 화면 구조로 바꾸는 스킬이다.
결과물은 Mid-fi 와이어프레임과 화면별 설계 스펙이다. 기능을 새로 기획하지 않는다.

판단 기준 전문은 [reference/principles.md](reference/principles.md), MVP 범위 판단은 [reference/mvp-checklist.md](reference/mvp-checklist.md)를 따른다. 여기서는 그 기준을 실행 순서로 풀어 쓴다.

## 입력 확인

시작하기 전에 아래 항목이 있는지 확인한다.

| 항목 | 없을 때 |
| --- | --- |
| PRD | 사용자에게 요청한다. PRD 없이는 진행하지 않는다. |
| User Flow | PRD에서 추출하고 "이렇게 가정했습니다"로 명시한다. |
| IA | PRD와 User Flow에서 추출하고 가정으로 명시한다. |
| 제약사항 (플랫폼, 디바이스, 개발 리소스) | 모바일 웹, 375pt 너비를 기본값으로 두고 명시한다. |
| 출력 매체 (Figma / HTML) | Figma 파일이 열려 있거나 URL이 주어지면 Figma, 아니면 HTML. |

확정되지 않은 정보는 침묵하지 않고 가정 로그에 적는다. 가정 로그는 스펙 문서 맨 위에 둔다.

## 작업 순서

화면을 하나씩 그리기 전에 전체 구조부터 잡는다. 순서는 아래와 같다.

### 1단계. 범위 확정

- PRD의 기능을 Core / Support / Later / Remove로 나눈다. 와이어프레임에는 Core와 필요한 Support만 넣는다.
- User Flow에서 핵심 경로 하나를 고른다. `진입 → 입력 → 처리 → 결과 → 다음 행동` 구조로 적는다.
- IA를 화면 목록으로 바꾼다. 화면마다 목적을 한 문장으로 쓴다. 목적을 한 문장으로 쓸 수 없는 화면은 삭제하거나 합친다.
- 이 단계 결과를 사용자에게 먼저 보여준다. 화면 목록이 틀리면 뒤 작업이 전부 틀어진다.

### 2단계. 화면별 설계

각 화면을 [templates/screen-spec.md](templates/screen-spec.md) 양식으로 채운다. 아래 순서를 지킨다. 순서를 건너뛰고 Component부터 고르지 않는다.

1. **목적**: 이 화면에서 사용자가 달성해야 하는 목표
2. **정보 추출**: 목표 달성에 필요한 정보만 나열
3. **정보 위계**: Primary / Secondary / Supporting으로 나누고, 사용자가 확인하는 순서대로 정렬
4. **Primary Action**: 화면의 목적을 달성하는 행동 하나. Secondary, Tertiary는 그 다음
5. **UI Pattern**: principles.md 4장의 표에서 고른다. 가장 단순하고 익숙한 것을 고른다
6. **Section 그룹핑**: 같은 목적의 정보를 한 Section으로 묶고, 행동과 그 행동에 필요한 정보를 가깝게 둔다
7. **State**: Default는 필수. 나머지는 핵심 플로우가 멈추는 경우에만 추가한다
8. **Component 재사용**: Component Inventory부터 본다. 데이터와 행동이 같으면 Component도 같아야 한다
9. **Dummy Content**: PRD의 사용 맥락에 맞는 실제 같은 내용을 넣는다
10. **Interaction**: `User Action → System Response → UI Change → Next` 형식으로 주요 인터랙션을 적는다

### 3단계. Component Inventory

화면 설계와 동시에 [templates/component-inventory.md](templates/component-inventory.md)를 관리한다.

- 새 Component를 만들기 전에 Inventory에 같은 역할이 이미 있는지 본다.
- 한 Component는 한 가지 역할만 맡는다.
- 화면마다 새 패턴을 만들지 않는다. Inventory가 화면 수보다 빠르게 늘어나면 잘못된 신호다.

### 4단계. 렌더링

스펙이 완성된 뒤에 그린다. 스펙 없이 바로 그리지 않는다.

**공통 규칙 (Mid-fi)**

- 색은 회색조만 쓴다. 배경 `#FFFFFF`, 면 `#F2F2F2`, 테두리 `#D9D9D9`, 본문 `#1A1A1A`, 보조 텍스트 `#767676`.
- Primary CTA만 진한 회색 `#1A1A1A` 채움에 흰 글자로 구분한다. Secondary는 테두리만, Tertiary는 텍스트만.
- 폰트는 시스템 sans-serif 하나. 크기는 제목 20, 소제목 16, 본문 14, 캡션 12만 쓴다.
- 간격은 8pt 단위. 화면 좌우 여백 16, Section 간격 24, 항목 간격 8 또는 12.
- 이미지 자리는 대각선이 그어진 회색 박스로 표시한다. 일러스트나 그림자, 애니메이션은 넣지 않는다.
- 각 화면 옆에 Annotation을 붙인다. 번호를 매기고 정보 위계, Primary Action, State 전환 조건을 적는다.

**Figma로 그릴 때**

1. `use_figma`를 부르기 전에 반드시 `figma-use` 스킬을 먼저 로드한다.
2. 새 파일이 필요하면 `figma-create-new-file` 스킬도 같이 로드한다.
3. 페이지 하나에 화면을 가로로 나열한다. 프레임 이름은 `01 홈 / Default`, `01 홈 / Empty`처럼 `번호 화면명 / State`로 짓는다.
4. 모든 프레임과 Section에 Auto Layout을 건다. 절대 좌표로 배치하지 않는다.
5. Component Inventory에 있는 것은 실제 Figma Component로 만들고, 화면에서는 Instance를 쓴다.
6. 레이어 이름은 역할로 짓는다. `Rectangle 12`를 남기지 않는다.
7. 화면 옆에 Annotation용 텍스트 프레임을 하나씩 둔다.
8. 다 그린 뒤 `get_screenshot`으로 한 번 렌더해서 실제 콘텐츠가 들어간 상태에서 Layout이 깨지지 않는지 확인한다.

**HTML로 그릴 때**

1. `artifact-design` 스킬을 로드하고 시작한다.
2. 파일 하나에 모든 화면을 넣는다. 화면마다 375pt 너비 프레임을 만들고 가로로 나열한다.
3. Component Inventory의 각 항목을 CSS 클래스 하나로 대응시킨다. 같은 Component는 같은 클래스를 쓴다.
4. 프레임 아래에 Annotation을 붙인다.
5. Artifact로 게시하고 링크를 전달한다.

### 5단계. 최종 검수

렌더 결과와 스펙을 principles.md 12장의 11개 항목과 대조한다. 하나라도 "아니오"면 해당 화면으로 돌아간다.

특히 아래 셋은 자주 놓친다.

- PRD에 없는 기능이 들어갔는가. 빈 공간을 채우려고 넣은 것은 뺀다.
- CTA 둘 이상이 같은 위계로 경쟁하는가.
- Dummy Content를 실제 길이의 텍스트로 넣었을 때 Layout이 깨지는가.

## 산출물

작업 폴더(기본값 `wireframes/`)에 아래 파일을 남긴다.

```
wireframes/
  spec.md                  # 가정 로그 + 범위 + 화면 목록 + 화면별 스펙
  components.md            # Component Inventory
  wireframe.html           # HTML로 그린 경우
```

Figma로 그린 경우 spec.md 맨 위에 파일 URL과 페이지 이름을 적는다.

## 하지 않는 것

- PRD에 없는 기능을 추가하지 않는다.
- User Flow와 IA를 임의로 바꾸지 않는다. 바꿔야 한다고 판단되면 바꾸지 말고 이유를 적어 사용자에게 알린다.
- 모든 콘텐츠를 Card로 만들지 않는다. Card 안에 Card를 넣지 않는다.
- `제목`, `설명 텍스트`, `사용자 이름` 같은 Placeholder를 쓰지 않는다.
- Brand Color, Typography System, 일러스트, 그림자를 넣지 않는다. 그건 다음 디자인 단계의 일이다.
- 익숙한 UX Pattern을 독창성을 위해 재설계하지 않는다.
- 스펙 없이 바로 그리지 않는다.

## 관련 스킬

- `oss-design-harness`: 이 스킬의 결과물을 High-fi로 발전시킬 때 사용한다. 와이어프레임은 그 하네스의 B단계 입력이 된다.
- `figma-use`, `figma-create-new-file`: Figma로 그릴 때 필수.
- `artifact-design`: HTML로 그릴 때 필수.
