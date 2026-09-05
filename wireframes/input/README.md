# wireframe 스킬 입력 패키지 — 청첩장모임 스케줄러

상위기획 산출물(PRD, definition.md, users.md, ia.yaml, flows.yaml, policy.md, validation.csv, seed-data.json, _handoff.md)을 `wireframe` 스킬이 요구하는 입력 형태로 재구성한 폴더다. ID 체계(REQ, NFR, ROLE, ENT, SCR, ST, FLW, POL, RISK)는 원본과 동일하다.

## 스킬 입력 항목 매핑

| 스킬이 요구하는 항목 | 파일 | 비고 |
|---|---|---|
| PRD | [prd.md](prd.md) | 배경·목표·유저 스토리·역할·스코프·REQ-01~15·NFR·성공 기준·평가 기준 |
| User Flow | [user-flow.md](user-flow.md) | 핵심 경로 2개(예비부부, 초대받은 지인)·상태 전이 ST-01~05·FLW-01~07 |
| IA | [ia.md](ia.md) | 엔티티 ENT-01~07·화면 SCR-01~10·화면별 정보/행동/상태·내비게이션·커버리지 |
| 제약사항 | [constraints.md](constraints.md) §1 | 모바일 웹 375pt, Figma 출력, 데이터 규모 |
| 출력 매체 | [constraints.md](constraints.md) §1 | Figma 신규 파일. 연결이 없으면 HTML |
| 정책·리스크 | [constraints.md](constraints.md) §2~7 | 권한표, POL-01~20, RISK-01~12, 화면별 주의점 |
| Dummy Content | [constraints.md](constraints.md) §8 | 시드 데이터 요약과 5대 필수 케이스 |
| 가정 로그 초안 | [constraints.md](constraints.md) §9 | spec.md 맨 위로 옮긴다 |

## 실행 방법

이 폴더를 참조해 스킬을 호출한다.

```
/wireframe wireframes/input/ 을 입력으로 청첩장모임 스케줄러 와이어프레임을 만들어줘.
출력 매체는 Figma 신규 파일, 산출물은 wireframes/ 에 남겨줘.
```

스킬은 1단계(범위 확정: Core/Support/Later/Remove 분류, 핵심 경로 선택, 화면 목록)를 먼저 보여주고 확인을 받은 뒤 화면별 스펙으로 넘어간다.

## 화면 범위에 대한 참고

화면 11개(SCR-02.1 포함) 전부가 요구사항에 매핑되어 있지만, MVP 와이어프레임은 핵심 경로 위주로 그린다. 분류는 스킬 1단계에서 판단하되 다음을 참고한다.

- 핵심 경로 A(예비부부): SCR-01 → SCR-05 → SCR-06 → SCR-07
- 핵심 경로 B(초대받은 지인): SCR-08 → SCR-09
- 핵심 경로의 전제: SCR-02/02.1(지인이 없으면 모임 편성 불가), SCR-10(배우자 연결이 없으면 통합 조망 불가)
- SCR-03 그룹 관리는 SCR-02.1에서 새 그룹 즉시 생성이 가능하므로 Support 후보
- SCR-04 모임 목록은 REQ-12(상태 구분)의 주 화면이지만 SCR-01 홈이 상태별 건수를 이미 보여준다

## 미결 사항 (클라이언트 확인 필요)

화면 구조에 영향을 주는 것만 추렸다. 전체 목록은 prd.md §6 보류 항목 참고.

| 항목 | 영향 화면 |
|---|---|
| 회신 마감 후 무응답 처리 기본값 | SCR-06 |
| 초대받은 지인의 전역 식별 기준(전화번호) | SCR-08 구조 전체 |
| 초대받은 지인의 신원 확인 수준 | SCR-08, SCR-09 진입 |
| 같은 모임 내 다른 참가자의 회신 열람 허용 여부 | SCR-09 |
| 배우자 대신 확정·취소하는 경우의 세부 UX | SCR-06, SCR-10 |
| 알림 채널 | 화면 내 알림 문구 |
