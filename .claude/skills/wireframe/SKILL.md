---
name: wireframe
description: PRD, User Flow, IA를 입력받아 MVP 수준의 Mid-fi 와이어프레임을 Markdown으로 만든다. "와이어프레임 만들어줘", "화면 구조 잡아줘", "PRD를 화면으로 바꿔줘", "이 플로우 화면별로 그려줘" 같은 요청에 사용한다. 새 기능을 기획하지 않고, 주어진 기획을 정보 위계·UI Pattern·Layout·Action·State로 변환한다. 산출물 wireframe.md는 Figma MCP로 디자인 시안을 만드는 에이전트의 입력이 된다.
---

# wireframe

상위기획팀이 넘긴 PRD, User Flow, IA를 화면 구조로 바꾸는 스킬이다.
결과물은 Markdown으로 적은 Mid-fi 와이어프레임과 화면별 설계 스펙이다. 기능을 새로 기획하지 않는다.

이 스킬은 그림을 그리지 않는다. 화면을 Figma Auto Layout에 그대로 옮길 수 있는 **레이아웃 트리**로 적는다. 그 파일(`wireframe.md`)을 Figma MCP 에이전트(`figma-generate-design`, `figma-use`)가 읽어 디자인 시안을 만든다. 그래서 산출물은 사람이 읽기 쉬운 것보다 변환 에이전트가 오해 없이 읽는 것을 우선한다.

판단 기준 전문은 [reference/principles.md](reference/principles.md), MVP 범위 판단은 [reference/mvp-checklist.md](reference/mvp-checklist.md), 아이콘은 [reference/icons.md](reference/icons.md)를 따른다. 여기서는 그 기준을 실행 순서로 풀어 쓴다.

## 입력 확인

시작하기 전에 아래 항목이 있는지 확인한다.

| 항목 | 없을 때 |
| --- | --- |
| PRD | 사용자에게 요청한다. PRD 없이는 진행하지 않는다. |
| User Flow | PRD에서 추출하고 "이렇게 가정했습니다"로 명시한다. |
| IA | PRD와 User Flow에서 추출하고 가정으로 명시한다. |
| 제약사항 (플랫폼, 디바이스, 개발 리소스) | 모바일 웹, 375pt 너비를 기본값으로 두고 명시한다. |
| 출력 매체 | Markdown으로 고정한다. HTML이나 이미지를 만들지 않고 Artifact도 게시하지 않는다. 제약사항이 다른 매체를 요구해도 이 스킬은 Markdown만 만든다. Figma 변환은 후속 에이전트의 일이다. |
| 실행 이름 | 범위를 나타내는 짧은 영문 slug를 정한다. 예: `all-screens`, `scr06-smoke`. 저장 폴더 이름에 쓴다. |
| 이전 평가 (`review.md`) | 있으면 재실행이다. 개선 항목부터 읽고, 필수 항목은 전부 반영한다. |

확정되지 않은 정보는 침묵하지 않고 가정 로그에 적는다. 가정 로그는 스펙 문서 맨 위에 둔다.

## 작업 순서

화면을 하나씩 적기 전에 전체 구조부터 잡는다. 순서는 아래와 같다.

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
   - 아이콘도 Component다. icons.md 표에서 Material 이름으로 고르고, 스펙에는 `뒤로 가기(arrow_back)`처럼 의미와 이름을 같이 적는다. 표에 없는 아이콘은 표에 먼저 추가한다
9. **Dummy Content**: PRD의 사용 맥락에 맞는 실제 같은 내용을 넣는다
10. **Interaction**: `User Action → System Response → UI Change → Next` 형식으로 주요 인터랙션을 적는다

### 3단계. Component Inventory

화면 설계와 동시에 [templates/component-inventory.md](templates/component-inventory.md)를 관리한다.

- 새 Component를 만들기 전에 Inventory에 같은 역할이 이미 있는지 본다.
- 한 Component는 한 가지 역할만 맡는다.
- 화면마다 새 패턴을 만들지 않는다. Inventory가 화면 수보다 빠르게 늘어나면 잘못된 신호다.
- 쓴 아이콘은 Inventory의 아이콘 표에 Material 이름, 의미, 쓰인 화면을 적는다. 같은 의미에 다른 아이콘이 두 개 있으면 하나로 합친다.
- Inventory의 각 Component는 "Component 정의" 절에 레이아웃 트리를 **한 번만** 적는다. 화면에서는 인스턴스 한 줄로 참조한다. Figma 에이전트가 이 정의로 Component를 만들고 화면에는 인스턴스를 놓는다.

### 4단계. 와이어프레임 작성

스펙이 완성된 뒤에 적는다. 스펙 없이 바로 적지 않는다. 양식과 표기법은 [templates/wireframe.md](templates/wireframe.md)에 있다. 표기법을 임의로 바꾸거나 늘리지 않는다. 표기로 적을 수 없는 것은 그 줄 끝에 `# 메모`로 남긴다.

**공통 규칙 (Mid-fi)**

- 색은 토큰 다섯 개만 쓴다. `bg` #FFFFFF, `surface` #F2F2F2, `line` #D9D9D9, `ink` #1A1A1A, `muted` #767676. hex를 직접 적지 않는다.
- Primary CTA만 `ink` 채움에 `bg` 글자로 구분한다. Secondary는 테두리만, Tertiary는 텍스트만.
- 텍스트 스타일은 `title` 20/600, `subtitle` 16/600, `body` 14/400, `caption` 12/400 넷만 쓴다.
- 간격은 8pt 단위. 화면 좌우 여백 16, Section 간격 24, 항목 간격 8 또는 12. 버튼 높이 48, 터치 영역 최소 44.
- 이미지 자리는 `image` 노드로 크기만 적는다. 일러스트나 그림자, 애니메이션은 넣지 않는다.
- 아이콘은 Material Symbols Outlined만 쓴다. `‹`, `×`, `☰`, `→` 같은 유니코드 글리프나 이모지로 대신하지 않는다. 라벨 없이 두는 아이콘은 icons.md에서 단독 사용이 허용된 것뿐이고, 나머지는 텍스트 라벨과 나란히 둔다. 크기는 24, 텍스트 앞 인라인만 20.
- 프레임마다 Annotation을 붙인다. 트리의 줄 끝에 `@1`처럼 번호를 달고, 프레임 아래 표에 정보 위계, Primary Action, State 전환 조건을 적는다.

**wireframe.md 작성 규칙**

1. 파일 하나에 모든 프레임을 넣는다. 프레임은 화면과 State의 조합 하나다. 이름은 `01 홈 / Default`, `01 홈 / Empty`처럼 `번호 화면명 / State`로 짓는다. Figma에서 최상위 프레임 이름이 된다.
2. Default State는 레이아웃 트리 전체를 적는다. 다른 State는 Default를 기준으로 달라지는 노드만 "차이" 표에 적는다. 절반 넘게 달라지면 트리 전체를 적는다.
3. 트리의 컨테이너는 전부 `col` 또는 `row`다. 절대 좌표를 쓰지 않는다. 노드마다 크기(`w`, `h`)를 `fill`, `hug`, 숫자 중 하나로 적는다.
4. Inventory에 있는 Component는 `comp` 한 줄로 참조하고 내부를 다시 적지 않는다. 텍스트나 State가 다르면 그 줄에 override로 적는다.
5. 레이어 이름은 역할을 나타내는 영문 PascalCase로 짓는다. `TopBar`, `DateOptionList`, `CtaDock`. `Frame 12`, `Group 3` 같은 이름은 쓰지 않는다.
6. 텍스트는 실제 Dummy Content를 그대로 적는다. 여러 줄이면 `\n`으로 잇는다.
7. 파일 맨 아래 "Figma 핸드오프" 절에 프레임 목록, 만들 Component와 Variant, 쓴 아이콘, 폰트 대체 규칙, 만드는 순서를 표로 정리한다. 변환 에이전트는 이 절부터 읽는다.
8. 파일은 처음부터 6단계의 저장 경로에 쓴다. 임시 경로에 쓰고 옮기지 않는다.

### 5단계. 최종 검수

wireframe.md와 스펙을 principles.md 12장의 12개 항목과 대조한다. 하나라도 "아니오"면 해당 화면으로 돌아간다.

특히 아래 다섯은 자주 놓친다.

- PRD에 없는 기능이 들어갔는가. 빈 공간을 채우려고 넣은 것은 뺀다.
- CTA 둘 이상이 같은 위계로 경쟁하는가.
- Dummy Content를 실제 길이의 텍스트로 넣었을 때 Layout이 깨지는가. 트리에서 `w=fill`인 텍스트가 한 줄을 넘길 때 아래 노드가 밀려도 되는지 본다.
- 아이콘만 보고 의미를 알 수 없는 곳이 있는가. 트리에서 `icon` 줄을 전부 찾아 `label=`이 없는 것이 단독 사용 허용 목록에 있는지 본다.
- 변환 에이전트가 물어봐야 할 것이 남았는가. 트리를 위에서 아래로 읽으며 크기가 빠진 노드, Inventory에 없는 `comp`, 토큰 밖의 색과 크기, `# 메모`로 미룬 판단을 찾는다. 하나라도 있으면 채우거나 가정 로그로 올린다.

### 6단계. 저장

검수를 통과한 산출물을 레포에 남긴다. 실행 한 번이 폴더 하나다. 이전 실행을 덮어쓰지 않는다.

1. `wireframes/output/<YYYYMMDD>-<slug>/` 폴더를 만든다. 날짜는 실행일, slug는 입력 확인에서 정한 실행 이름이다. 같은 날 같은 slug로 다시 돌리면 `-2`, `-3`을 붙인다.
2. 폴더 안에 `spec.md`, `components.md`, `wireframe.md`, `README.md`를 둔다. README는 [templates/run-readme.md](templates/run-readme.md) 양식을 따른다. 입력 폴더와 커밋 해시, 적은 프레임 목록, Figma 변환 상태를 적는다.
3. `wireframes/output/README.md` 인덱스 표에 이 실행을 한 줄 추가한다. 열은 실행 폴더, 날짜, 범위, 링크, 비고다. 링크 열에는 Figma 변환 전이면 `wireframe.md` 상대 경로를, 변환 후에는 Figma 파일 링크를 적는다. 인덱스가 없으면 만든다.
4. 커밋은 사용자가 요청할 때만 한다. 메시지는 `docs(wireframe): <slug> 산출물 저장` 형식을 쓴다.

## 산출물

```
wireframes/
  input/                          # 상위기획 입력 (PRD, User Flow, IA, 제약사항)
  output/
    README.md                     # 실행 인덱스. 실행마다 한 줄
    <YYYYMMDD>-<slug>/
      README.md                   # 실행 요약. 입력 버전, 범위, Figma 변환 상태
      spec.md                     # 가정 로그 + 범위 + 화면 목록 + 화면별 스펙
      components.md               # Component Inventory + Component 정의 트리 + 아이콘 표
      wireframe.md                # 프레임별 레이아웃 트리 + Annotation + Figma 핸드오프
```

최종 보고에는 저장 폴더 경로와 프레임 수를 적고, Figma 변환 명령 한 줄을 덧붙인다.

```
wireframes/output/<폴더>/wireframe.md 를 읽고 Figma 핸드오프 절의 순서대로 <Figma 파일 링크>에 프레임을 만들어줘.
```

## 하지 않는 것

- PRD에 없는 기능을 추가하지 않는다.
- User Flow와 IA를 임의로 바꾸지 않는다. 바꿔야 한다고 판단되면 바꾸지 말고 이유를 적어 사용자에게 알린다.
- HTML, SVG, 이미지, Artifact를 만들지 않는다. 산출물은 Markdown뿐이다.
- Figma를 직접 건드리지 않는다. 변환은 후속 에이전트가 wireframe.md를 읽고 한다.
- 모든 콘텐츠를 Card로 만들지 않는다. Card 안에 Card를 넣지 않는다.
- `제목`, `설명 텍스트`, `사용자 이름` 같은 Placeholder를 쓰지 않는다.
- Brand Color, Typography System, 일러스트, 그림자를 넣지 않는다. 그건 다음 디자인 단계의 일이다.
- Material 밖의 아이콘을 만들거나, 유니코드 글리프와 이모지를 아이콘으로 쓰지 않는다.
- 익숙한 UX Pattern을 독창성을 위해 재설계하지 않는다.
- 스펙 없이 바로 적지 않는다.

## 관련 스킬

- `wireframe-review`: 이 스킬의 실행 폴더를 체크리스트로 평가한다. 개선 항목이 다음 실행의 입력이 된다.
- `figma-generate-design`, `figma-use`: wireframe.md를 읽어 Figma에 프레임을 만드는 후속 단계. 이 스킬 안에서 호출하지 않는다.
- `oss-design-harness`: Figma 시안을 High-fi로 발전시킬 때 사용한다. 와이어프레임은 그 하네스의 B단계 입력이 된다.
