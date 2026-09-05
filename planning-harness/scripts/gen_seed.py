#!/usr/bin/env python3
"""ia.yaml 엔티티 정의에서 seed-data.json 뼈대를 생성한다.

사용법:
    python scripts/gen_seed.py {산출물디렉토리}

이 스크립트는 값을 지어내지 않는다. 필드 구조와 필수 케이스 자리만 만들고,
실제 값은 하네스(LLM)가 STEP 7에서 채운다. 도메인 맥락을 모르는 스크립트가
생성한 더미는 화면 설계 검증에 쓸모가 없기 때문이다.

PyYAML이 있으면 정확히 파싱하고, 없으면 정규식 폴백으로 동작한다.
"""

import json
import re
import sys
from pathlib import Path

REQUIRED_CASES = [
    ("empty_group", "RISK-07", "빈 상태를 보여줄 수 있는 항목 하나"),
    ("partial_completion", "RISK-08", "부분 완료 건 (예: 6명 중 4명 회신)"),
    ("resource_conflict", "RISK-03", "같은 시점에 겹치는 건 2개"),
    ("multi_membership", "RISK-01", "한 대상이 두 분류에 동시 소속"),
    ("deadline_edge", "RISK-02", "마감 임박 1건 + 마감 초과 1건"),
    ("onboarding_incomplete", "RISK-07", "온보딩 미완료 사용자 1명 (필수 단계 일부만 마쳐 첫 화면이 빈 상태)"),
]


def parse_with_yaml(text):
    try:
        import yaml  # type: ignore
    except ImportError:
        return None
    try:
        data = yaml.safe_load(text) or {}
    except Exception:
        return None
    out = []
    for e in data.get("entities") or []:
        out.append({
            "id": e.get("id", ""),
            "name": e.get("name", ""),
            "fields": [
                {"name": f.get("name", ""), "type": f.get("type", "string"),
                 "required": bool(f.get("required"))}
                for f in (e.get("fields") or [])
            ],
        })
    return out


def parse_fallback(text):
    """PyYAML 없이 entities 블록만 얕게 파싱."""
    entities = []
    section = text.split("screens:")[0]
    blocks = re.split(r"\n\s*-\s+id:\s*(ENT-\d{2,3})", section)
    for i in range(1, len(blocks), 2):
        eid, body = blocks[i], blocks[i + 1]
        name_m = re.search(r"name:\s*(.+)", body)
        fields = []
        for fm in re.finditer(r"-\s*name:\s*(.+?)\n\s*type:\s*(\w+)\n\s*required:\s*(\w+)", body):
            fields.append({
                "name": fm.group(1).strip().strip('"'),
                "type": fm.group(2).strip(),
                "required": fm.group(3).strip().lower() == "true",
            })
        entities.append({
            "id": eid,
            "name": name_m.group(1).strip().strip('"') if name_m else "",
            "fields": fields,
        })
    return entities


def sample(ftype):
    return {
        "string": "", "number": 0, "bool": False,
        "date": "YYYY-MM-DD", "datetime": "YYYY-MM-DDTHH:MM:SS",
        "enum": "", "ref": "",
    }.get(ftype, "")


def main():
    if len(sys.argv) < 2:
        print("사용법: python scripts/gen_seed.py {산출물디렉토리}")
        return 2

    root = Path(sys.argv[1])
    ia_path = root / "ia.yaml"
    if not ia_path.exists():
        print(f"[오류] {ia_path} 없음. STEP 2를 먼저 수행하세요.")
        return 2

    text = ia_path.read_text(encoding="utf-8")
    entities = parse_with_yaml(text)
    mode = "PyYAML"
    if entities is None:
        entities = parse_fallback(text)
        mode = "정규식 폴백 (pip install pyyaml 권장)"

    if not entities:
        print("[오류] ia.yaml에서 엔티티를 찾지 못했습니다.")
        return 1

    seed = {
        "_meta": {
            "generated_by": "scripts/gen_seed.py",
            "note": "구조만 생성됨. 값은 STEP 7에서 하네스가 채운다.",
            "required_cases": [
                {"key": k, "risk": r, "description": d} for k, r, d in REQUIRED_CASES
            ],
        }
    }

    for e in entities:
        key = (e["id"] or "entity").lower().replace("-", "_")
        seed[key] = {
            "_entity": e["id"],
            "_name": e["name"],
            "_target_count": "TBD: project-profile.yaml의 data_scale 참조",
            "records": [
                {f["name"]: sample(f["type"]) for f in e["fields"]}
            ] if e["fields"] else [],
        }

    out = root / "seed-data.json"
    out.write_text(json.dumps(seed, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"파싱 모드: {mode}")
    print(f"엔티티 {len(entities)}개 → {out}\n")
    print("다음으로 하네스가 채울 것:")
    print("  1. _target_count를 실제 최대 건수로 교체하고 그만큼 레코드 생성")
    print("  2. 아래 필수 케이스 6종을 반드시 포함")
    for k, r, d in REQUIRED_CASES:
        print(f"     - {k} ({r}): {d}")
    print("  3. 이름·텍스트 길이·날짜를 현실적인 분포로")
    return 0


if __name__ == "__main__":
    sys.exit(main())
