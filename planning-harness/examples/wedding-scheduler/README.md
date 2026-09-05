# 예시 — 청첩장모임 스케줄러

이 하네스의 **품질 기준선**. 산출물의 밀도가 헷갈리면 여기를 본다.

- `input/prd.md` — 원본 PRD (greenfield, 화면 설계 자유)
- `project-profile.yaml` — 채워진 프로필 예시
- `output/` — 완주 산출물 9종
- 저장소 루트의 `wireframes/input/` — 같은 케이스의 STEP 8 입력 패키지 예시 (형식 기준선)

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

온보딩(STEP 4)도 이 케이스가 보기 좋다. `RISK-04` 공동 소유 때문에 **먼저 가입해 커플을 만드는 사람(`ONB-01`, 빈 공간에서 시작)과 초대 코드로 합류하는 배우자(`ONB-02`, 이미 모임이 있는 공간에 합류)의 첫 화면이 다르다.** 여기에 계정 없는 초대받은 지인(`ONB-03`)까지 세 종류의 첫 진입이 한 서비스에 공존한다. STEP 4를 돌리면서 "결혼 예정일을 입력받는 화면이 없다"는 누락이 드러나 `SCR-11`이 추가됐다.

## STEP 8 패키지 예시

저장소 루트의 `wireframes/input/`이 이 케이스의 입력 패키지 예시다. `prd.md`·`user-flow.md`·`ia.md`·`constraints.md`의 절 구성과 밀도를 여기서 본다.

단, 이 폴더는 STEP 4(온보딩)가 하네스에 추가되기 전에 만들어져 `SCR-11`과 `ONB-01`~`ONB-03`, `user-flow.md` 5절이 빠져 있다. **형식 기준선으로만 쓰고, 내용 완결성 기준선으로 쓰지 않는다.** 확인은 아래 명령으로 한다.

## 실행

```bash
python scripts/validate_ids.py   examples/wedding-scheduler/output
python scripts/check_coverage.py examples/wedding-scheduler/output
python scripts/check_wireframe_input.py examples/wedding-scheduler/output wireframes/input
```

마지막 명령은 위에 적은 이유로 현재 실패한다. 실패 내용이 곧 STEP 8 검사기가 무엇을 잡는지 보여주는 예시다.
