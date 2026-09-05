# 예시 — 청첩장모임 스케줄러

이 하네스의 **품질 기준선**. 산출물의 밀도가 헷갈리면 여기를 본다.

- `input/prd.md` — 원본 PRD (greenfield, 화면 설계 자유)
- `project-profile.yaml` — 채워진 프로필 예시
- `output/` — 완주 산출물 8종

## 이 케이스를 예시로 고른 이유

12개 리스크 패턴 중 **9개가 동시에 해당**한다. 범용 패턴이 실제로 어떻게 발현되는지 보기 좋다.

| 패턴 | 이 도메인에서의 발현 |
|---|---|
| RISK-01 다대다 귀속 | 한 지인이 대학 동기이자 직장 동료 |
| RISK-02 응답 타임아웃 | 날짜 후보를 보냈는데 며칠째 무응답 |
| RISK-03 리소스 충돌 | 같은 날 저녁에 모임 두 건 |
| RISK-04 공동 소유 | 신랑·신부가 각자 지인 풀 관리, 일정은 공유 |
| RISK-05 플로우 우회 | 결혼식 2주 전 급하게 잡는 모임 |
| RISK-06 대량 데이터 | 지인 최대 100명 |
| RISK-07 빈 상태 | 최초 진입 시 지인 0명 |
| RISK-08 부분 완료 | 6명 중 4명만 회신 |
| RISK-12 이력·아카이브 | 이미 다녀온 모임 |

`RISK-10`(미인증 진입)은 초대받은 지인의 회신 방식에 따라 갈린다 — 이 판단이 화면 수를 크게 바꾸므로 STEP 1에서 반드시 확정해야 한다.

## 실행

```bash
python scripts/validate_ids.py   examples/wedding-scheduler/output
python scripts/check_coverage.py examples/wedding-scheduler/output
```
