# 실행 요약: <YYYYMMDD>-<slug>

> `wireframe` 스킬 실행 한 번의 기록이다. 이 폴더 안의 파일이 이 실행의 산출물 전부다.

| 항목 | 값 |
| --- | --- |
| 실행일 | YYYY년 MM월 DD일 |
| 범위 | 예: 전체 10개 화면 / SCR-06 한 화면, State 2개 |
| 입력 폴더 | `wireframes/input/` |
| 입력 커밋 | `git rev-parse --short HEAD` 결과 |
| 반영한 평가 | 예: `../20260905-scr06-smoke/review.md` 필수 3건. 없으면 "없음" |
| 출력 매체 | Markdown (`wireframe.md`) |
| Figma 변환 | 미변환. 변환 후 파일 링크와 날짜를 적는다 |

## 적은 프레임

| 프레임 | 화면 | State | 기준 |
| --- | --- | --- | --- |
| `06 모임 상세 / Default` | SCR-06 | 확정대기 | 전체 트리 |
| `06 모임 상세 / Partial` | SCR-06 | 회신중 | Default 차이 |

## 읽는 순서

1. [spec.md](spec.md) 가정 로그. 사용자 확인이 필요한 항목
2. [wireframe.md](wireframe.md) 맨 아래 "Figma 핸드오프". 만들 것의 전체 목록
3. [components.md](components.md) Component 정의

## Figma 변환

```
wireframes/output/<YYYYMMDD>-<slug>/wireframe.md 를 읽고 Figma 핸드오프 절의 순서대로 <Figma 파일 링크>에 프레임을 만들어줘.
```

## 이 실행에서 남긴 것

- 사용자 확인이 필요한 항목: spec.md 가정 로그 참고
- 다음 실행에서 이어서 할 것:
