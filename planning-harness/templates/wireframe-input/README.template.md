# wireframe 스킬 입력 패키지 — {프로젝트명}

상위기획 산출물(`definition.md`, `users.md`, `ia.yaml`, `flows.yaml`, `onboarding.yaml`, `policy.md`, `validation.csv`, `seed-data.json`, `_handoff.md`)을 `wireframe` 스킬이 요구하는 입력 형태로 재구성한 폴더다. ID 체계(REQ, NFR, ROLE, ENT, SCR, ST, FLW, ONB, POL, RISK)는 원본과 동일하다.

## 스킬 입력 항목 매핑

| 스킬이 요구하는 항목 | 파일 | 비고 |
|---|---|---|
| PRD | [prd.md](prd.md) | 배경·목표·유저 스토리·역할·스코프·REQ·NFR·성공 기준 |
| User Flow | [user-flow.md](user-flow.md) | 핵심 경로·상태 전이(ST)·유저 플로우(FLW)·온보딩 경로(ONB) |
| IA | [ia.md](ia.md) | 엔티티(ENT)·화면(SCR)·화면별 정보/행동/상태·내비게이션·커버리지 |
| 제약사항 | [constraints.md](constraints.md) §1 | 플랫폼·기준 너비·데이터 규모 |
| 출력 매체 | [constraints.md](constraints.md) §1 | |
| 정책·리스크 | [constraints.md](constraints.md) §2~7 | 권한표, POL, RISK, 화면별 주의점 |
| Dummy Content | [constraints.md](constraints.md) §8 | 시드 데이터 요약과 필수 케이스 |
| 가정 로그 초안 | [constraints.md](constraints.md) §9 | `spec.md` 맨 위로 옮긴다 |

## 실행 방법

이 폴더를 참조해 스킬을 호출한다.

```
/wireframe {이 폴더 경로}/ 를 입력으로 {프로젝트명} 와이어프레임을 만들어줘.
출력 매체는 {Figma 신규 파일 / HTML}, 산출물은 {출력 폴더}/ 에 남겨줘.
```

스킬은 1단계(범위 확정: Core/Support/Later/Remove 분류, 핵심 경로 선택, 화면 목록)를 먼저 보여주고 확인을 받은 뒤 화면별 스펙으로 넘어간다.

## 화면 범위에 대한 참고

<!-- 화면 전부가 요구사항에 매핑돼 있어도 MVP 와이어프레임은 핵심 경로 위주로 그린다.
     분류는 스킬 1단계에서 판단하되, 상위기획이 아는 판단 근거를 여기 남긴다. -->

- 핵심 경로 A({역할군}): SCR-NN → SCR-NN → SCR-NN
- 핵심 경로 B({역할군}): SCR-NN → SCR-NN
- 핵심 경로의 전제: <!-- 이게 없으면 핵심 경로가 성립하지 않는 화면 -->
- Support 후보와 그 근거: <!-- 왜 Core가 아닌지 -->

## 미결 사항 (클라이언트 확인 필요)

<!-- 화면 구조에 영향을 주는 것만 추린다. 전체 목록은 prd.md 보류 항목과 constraints.md §9를 가리킨다. -->

| 항목 | 영향 화면 |
|---|---|
