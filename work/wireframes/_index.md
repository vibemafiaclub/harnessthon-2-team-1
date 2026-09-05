# 와이어프레임 인덱스

> 02-wireframer 산출물. 03·04가 `상태` 열을 갱신한다 (spec-done → built → reviewed-pass). 목데이터: `work/mock-data.json` (부록 B 8개 규칙 검증 통과, 수정 없음. `derived.today` = 2026-11-19 기준).

## 공통 (모든 화면)

- 프레임 390 × 844, safe-top 47 / safe-bottom 34, 좌우 마진 `{spacing.lg}`.
- 탭바 `{component.mobile-tab-bar}` 3탭: "달력"(calendar) / "모임"(list.bullet) / "지인"(person.2). 탭 화면 3개에만. 상세·편집·링크 화면은 `{component.mobile-sticky-cta}` 또는 하단 없음.
- 소유자·상태·겹침은 텍스트 라벨(`{component.status-chip}` / caption)만. 색·아이콘 분기 금지.
- 조합 컴포넌트(03이 `work/figma-log.md`에 기록): 달력 그리드(7열 caption 셀), 선택 아이콘 행(list-row + checkmark.circle), 토글 대체(status-chip 2개 단일 선택), sticky-cta 좌 text-link.

## 화면 목록

| screen-id           | 파일                   | 우선순위 | build-scope | 상태          | 03이 만드는 인스턴스        | 다루는 엣지케이스                                                        |
| ------------------- | ---------------------- | -------- | ----------- | ------------- | --------------------------- | ------------------------------------------------------------------------ |
| `calendar-overview` | `calendar-overview.md` | P0 (홈)  | core        | reviewed-pass | 2026-11, 11/28 선택         | 겹침(m04·m05), 늦은 회신·급한 모임(요약 행 m12), 상견례(공동 필터)       |
| `home-meetings`     | `home-meetings.md`     | P0       | later       | reviewed-pass | 전체 필터, 18행             | 늦은 회신(m01), 급한 모임(m12), 1:1(m07·m16), 상견례(m09), 겹침(m04·m05) |
| `contacts-list`     | `contacts-list.md`     | P0       | later       | built         | 그룹 "대학 동기" 필터, 10행 | 중복 소속(p03), 양가 공통(p52), 1:1(따로 만나기 텍스트), 긴 텍스트(p20)  |
| `contact-edit`      | `contact-edit.md`      | P0       | later       | spec-done     | p03 수정 모드               | 중복 소속(그룹 칩 복수 선택), 1:1(따로 만나기), 양가(공동)               |
| `meeting-create`    | `meeting-create.md`    | P0       | core        | reviewed-pass | m10 편성, 그룹 "직장 동료"  | 중복 소속(p03 편성됨), 1:1(p14 경고), 상견례(공동 상태), 빈 그룹(g06)    |
| `meeting-dates`     | `meeting-dates.md`     | P0       | core        | reviewed-pass | m01 후보 3개, 마감 "직접"   | 겹침 1차 경고(c1·c3), 마감 필수, 급한 모임(urgent 상태 m12)              |
| `meeting-detail`    | `meeting-detail.md`    | P0       | core        | reviewed-pass | m01 확정 대기               | 늦은 회신(p11 미회신·마감 지남·리마인드·연장), 겹침, 상태 5개 CTA        |
| `meeting-confirm`   | `meeting-confirm.md`   | P0       | later       | spec-done     | m01 draft c3                | 겹침 2차 경고, 미회신 제외 확정                                          |
| `guest-response`    | `guest-response.md`    | P0       | core        | reviewed-pass | m02, 응답자 p09             | 급한 모임(마감 첫 스크롤), 늦은 회신(마찰 0), 확정 공유 상태             |

`build-scope` = Figma 생성 범위 (사람 결정 · 2026-09-05, 시간 제약). **core 5개**(`calendar-overview` → `meeting-create` → `meeting-dates` → `meeting-detail` → `guest-response`)를 이 순서로 03이 먼저 만든다. **later 4개**는 스펙은 완성됐으나 후속 배치 — 03은 core 5개가 `reviewed-pass`가 되기 전에 later를 시작하지 않는다. later 화면으로 가는 이탈(예: `meeting-detail` → `meeting-confirm`)은 core 프레임에서 버튼만 만들고 링크 대상 프레임은 비워 둔다.

P1 (`contact-import`, `guest-my-invites`, `meeting-members-edit`): 미작성.

## 까다로운 상황 6개 배치 확인

| 상황 (PRD §3)   | mock-data `edgeCases`         | 배치된 화면 · 블록                                                                                                             |
| --------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 중복 소속       | `multiGroupPerson` p03        | `contacts-list` 6(칩 2개) · `contact-edit` 5(복수 선택) · `meeting-create` 8("'직장 팀' 모임에 편성됨")                        |
| 늦은 회신       | `lateReplier` p11 / m01       | `meeting-detail` 2·3·스티키 · `home-meetings` 2·3 · `calendar-overview` 3 · `meeting-confirm` 5 · `meeting-dates` 6(마감 필수) |
| 겹치는 모임     | `overlappingMeetings` m04·m05 | `meeting-dates` 3(1차) · `meeting-confirm` 6(2차) · `calendar-overview` 6·8·9 · `home-meetings` 6 · `meeting-detail` 4         |
| 1:1 (직장 상사) | `oneOnOne` m07                | `contact-edit` 7 · `meeting-create` 8·9 · `contacts-list` 6 · `home-meetings` 4                                                |
| 상견례 (양가)   | `bothSides` m09               | `meeting-create` 3(공동 상태) · `calendar-overview` 1·8 · `home-meetings` 1·6 · `contact-edit` 4                               |
| 급한 모임       | `urgent` m12                  | `meeting-dates` urgent 상태 · `calendar-overview` 3 · `home-meetings` 4 · `guest-response` 1                                   |
