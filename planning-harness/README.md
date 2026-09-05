# planning-harness

PRD·RFP·구두 브리프를 받아 **에이전시 납품 수준의 상위 기획 산출물**을 만드는 하네스.
도메인 무관 범용 구조. 주제가 바뀌어도 파일 구조와 스키마는 그대로 쓴다.

> 상태: **초고(draft)**. 실전 검증 전. 돌려보고 걸리는 지점을 이슈로 남겨주세요.

## 무엇을 만드는가

화면설계서(스토리보드) **직전까지**의 기획 문서 8종.

| 파일 | 내용 |
|---|---|
| `project-profile.yaml` | 프로젝트 설정 (사람이 작성) |
| `definition.md` | 배경·목표·스코프·요구사항 |
| `users.md` | 역할·권한·진입 경로 |
| `ia.yaml` | 엔티티·화면목록·내비게이션 |
| `flows.yaml` | 상태 전이·유저 플로우 |
| `policy.md` | 권한·예외·데이터·알림 정책 |
| `validation.csv` | 요구사항 커버리지·리스크 판정 |
| `seed-data.json` | 더미 데이터 |
| `_handoff.md` | 다음 단계 인계 요약 |

레이아웃·컴포넌트·컬러·타이포는 만들지 않는다. 그건 다음 하네스의 몫이다.

## 설계 원칙 세 가지

**1. 모든 것에 ID를 붙이고 ID로 참조한다**
"모임 상세 화면에서 처리한다"가 아니라 "`SCR-07`에서 처리한다". 이렇게 써야 스크립트가 누락을 잡아내고, 다음 하네스가 문서를 파싱할 수 있다. → `references/id-convention.md`

**2. 범용 리스크 패턴 12개를 매번 순회한다**
"중복 소속", "늦은 응답", "일정 겹침" 같은 건 도메인 특수 사정이 아니라 **어디서나 반복되는 패턴**이다. 12개를 고정해두고 매 프로젝트마다 "이 도메인에서는 무엇으로 나타나는가"를 채우게 하면, 주제가 바뀌어도 기획 깊이가 유지된다. → `references/risk-patterns.md`

**3. 검증을 LLM 자기평가에 맡기지 않는다**
ID 참조 무결성과 요구사항 커버리지는 스크립트로 검사한다. 실패하면 이전 스텝으로 되돌아간다. → `scripts/`

## 폴더 구조

```
planning-harness/
├── SKILL.md              진입점 — 6스텝 라우팅
├── config/               프로젝트 프로필 템플릿
├── references/           스텝별 지침 (스텝 진입 시에만 로드)
├── templates/            산출물 뼈대
├── schemas/              JSON Schema (검증 기준)
├── scripts/              ID·커버리지 검사, 시드 생성
├── tests/                검사 스크립트 자체 테스트
└── examples/             완주 예시 = 품질 기준선
```

## 쓰는 법

### Claude Code에서

1. 이 폴더를 스킬로 등록한다 (`~/.claude/skills/planning-harness/` 아래에 두거나 프로젝트 루트에 배치)
2. `config/project-profile.template.yaml`을 복사해 채운다
3. 원본 PRD와 함께 요청한다

```
{프로젝트}/01-planning/project-profile.yaml 채웠어.
원본은 input/prd.md야. 상위 기획 시작해줘.
```

### 스크립트만 따로

```bash
python scripts/validate_ids.py   wedding-scheduler/01-planning
python scripts/check_coverage.py wedding-scheduler/01-planning
python scripts/gen_seed.py       wedding-scheduler/01-planning
```

표준 라이브러리만 쓴다. `gen_seed.py`는 PyYAML이 있으면 더 정확하게 파싱한다 (`pip install pyyaml`, 없어도 동작).

스크립트를 고쳤으면 먼저 이걸 돌린다.

```bash
bash tests/run_tests.sh
```

## 6스텝

```
STEP 0  프로필 작성      → project-profile.yaml
STEP 1  정의·역할        → definition.md, users.md
STEP 2  정보구조         → ia.yaml          (엔티티 먼저, 화면은 나중)
STEP 3  플로우·상태      → flows.yaml       (상태 먼저, 플로우는 나중)
STEP 4  정책             → policy.md
STEP 5  검증  ←──┐      → validation.csv   (실패 시 2~4로 되돌아감)
STEP 6  시드·인계 ─┘     → seed-data.json, _handoff.md
```

STEP 5가 이 하네스의 핵심이다. 통과할 때까지 반복하는 구조라서, 여기가 느슨하면 나머지가 다 무의미해진다.

---

## git 사용법 (git이 처음이라면)

용어부터.

| 용어 | 뜻 |
|---|---|
| **repository (repo)** | 프로젝트 폴더 하나. 변경 이력이 통째로 저장된다 |
| **clone** | 원격 저장소를 내 컴퓨터로 복제해오는 것. 최초 1회만 |
| **pull** | 남이 올린 최신 변경을 내 컴퓨터로 받아오는 것 |
| **commit** | 변경사항을 "이력 한 칸"으로 확정하는 것. 아직 내 컴퓨터에만 있음 |
| **push** | 내 commit들을 원격 저장소로 올리는 것 |
| **branch** | 평행 작업선. `main`을 건드리지 않고 따로 작업할 때 씀 |

### 최초 1회

```bash
git clone {저장소주소}
cd planning-harness
```

### 작업할 때마다

```bash
git pull                      # 1. 남의 변경 먼저 받아온다 (안 하면 충돌 남)
                              # 2. 파일 수정
git add .                     # 3. 변경한 파일 전부를 commit 대상에 올린다
git commit -m "step2 지침 보완"  # 4. 이력 한 칸으로 확정. -m 뒤는 무엇을 했는지 메모
git push                      # 5. 원격 저장소로 올린다
```

`git status`를 중간에 찍어보면 지금 무엇이 바뀌었고 어디까지 진행됐는지 보여준다. 헷갈리면 일단 이걸 쳐본다.

### 각자 따로 돌려볼 때 (권장)

`main`을 직접 고치면 서로 덮어쓰게 된다. 브랜치를 파고 작업한다.

```bash
git checkout -b test/소현    # 새 브랜치를 만들고 그리로 이동
# ... 작업 ...
git add .
git commit -m "청첩장 케이스 실행 결과"
git push -u origin test/소현  # 첫 push만 -u origin {브랜치명} 을 붙인다
```

이후 GitHub에서 Pull Request를 열면 무엇이 달라졌는지 비교해서 볼 수 있다.

### 실행 결과는 커밋하지 않는다

`.gitignore`에 산출물 폴더를 넣어뒀다. 하네스 자체(지침·템플릿·스크립트)만 버전 관리하고, 각자 돌린 결과물은 올리지 않는다.
단, `examples/` 아래 예시는 품질 기준선이므로 예외로 커밋한다.

## 남은 작업

- [ ] `examples/wedding-scheduler/output/` 완주본 채우기 (품질 기준선)
- [ ] 다른 도메인 1건으로 범용성 검증 (커머스 또는 예약 권장)
- [ ] `check_coverage.py`의 목록 화면 판정이 한국어 화면명 키워드 매칭이라 거칠다 — 개선 필요
- [ ] 클라이언트 제출용 PPT·PDF 렌더링은 별도 하네스로 분리 예정
