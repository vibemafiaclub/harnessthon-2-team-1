#!/usr/bin/env python3
"""ID 참조 무결성 검사.

사용법:
    python scripts/validate_ids.py {산출물디렉토리}
    예) python scripts/validate_ids.py wedding-scheduler/01-planning

검사 항목
    1. 정의되지 않은 ID를 참조하는가 (broken reference)
    2. 정의만 되고 아무 데서도 참조되지 않는가 (orphan)
    3. 같은 ID가 중복 정의되었는가
    4. ID 형식이 규칙에 맞는가

표준 라이브러리만 사용한다.
"""

import re
import sys
from pathlib import Path

# 접두사별 정의 파일 — 이 파일 안에 등장하는 해당 접두사 ID를 '정의'로 본다
OWNER = {
    "REQ": "definition.md",
    "ROLE": "users.md",
    "ENT": "ia.yaml",
    "SCR": "ia.yaml",
    "FLW": "flows.yaml",
    "ST": "flows.yaml",
    "POL": "policy.md",
    "EC": "validation.csv",
}

# 고정 상수 — 프로젝트에서 정의하지 않는다
FIXED = {f"RISK-{i:02d}" for i in range(1, 13)}

ID_RE = re.compile(r"\b(REQ|ROLE|ENT|SCR|FLW|ST|POL|EC|RISK)-(\d{2,3})(?:\.(\d+))?\b")
YAML_DEF_RE = re.compile(r"^\s*-?\s*id:\s*([A-Z]+-\d{2,3}(?:\.\d+)?)\s*$", re.M)

# 고아여도 경고하지 않는 접두사 (최종 산출물이라 참조될 필요가 없음)
ORPHAN_EXEMPT = {"EC"}


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def scan(root: Path):
    """정의와 참조를 분리해 수집한다.

    YAML은 'id:' 키만 정의로 인정하고, 그 줄을 제거한 나머지에서 참조를 찾는다.
    마크다운·CSV는 소유 파일 안에 등장한 해당 접두사 ID를 정의로 본다
    (같은 파일 안 중복 등장은 표 재언급일 수 있으므로 한 번만 센다).
    """
    files = {p.name: read(p) for p in root.iterdir() if p.is_file()}
    defined = {}      # id -> [정의된 파일]
    referenced = {}   # id -> {참조한 파일}

    for fname, text in files.items():
        own_prefixes = {p for p, f in OWNER.items() if f == fname}

        if fname.endswith(".yaml"):
            # 정의: id: 키 (중복 정의를 잡기 위해 list 그대로)
            for full in YAML_DEF_RE.findall(text):
                if full.split("-")[0] in own_prefixes:
                    defined.setdefault(full, []).append(fname)
            # 참조: 정의 줄을 제거한 나머지
            ref_text = YAML_DEF_RE.sub("", text)
        else:
            seen = set()
            for m in ID_RE.finditer(text):
                prefix, num, sub = m.group(1), m.group(2), m.group(3)
                full = f"{prefix}-{num}" + (f".{sub}" if sub else "")
                if prefix in own_prefixes and full not in seen:
                    seen.add(full)
                    defined.setdefault(full, []).append(fname)
            ref_text = text

        for m in ID_RE.finditer(ref_text):
            prefix, num, sub = m.group(1), m.group(2), m.group(3)
            full = f"{prefix}-{num}" + (f".{sub}" if sub else "")
            if fname.endswith(".yaml") or prefix not in own_prefixes:
                referenced.setdefault(full, set()).add(fname)

    return files, defined, referenced


def main():
    if len(sys.argv) < 2:
        print("사용법: python scripts/validate_ids.py {산출물디렉토리}")
        return 2

    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"[오류] 디렉토리를 찾을 수 없습니다: {root}")
        return 2

    files, defined, referenced = scan(root)
    errors, warnings = [], []

    missing_files = [f for f in set(OWNER.values()) if f not in files]
    if missing_files:
        errors.append(f"산출물 누락: {', '.join(sorted(missing_files))}")

    # 1. 깨진 참조
    for rid, srcs in sorted(referenced.items()):
        if rid.startswith("RISK-"):
            if rid not in FIXED:
                errors.append(f"{rid} — RISK는 RISK-01~RISK-12만 사용 ({', '.join(sorted(srcs))})")
            continue
        base = rid.split(".")[0]
        if rid not in defined and base not in defined:
            owner = OWNER.get(rid.split("-")[0], "?")
            errors.append(f"{rid} 참조 — {owner}에 정의 없음 (참조: {', '.join(sorted(srcs))})")

    # 2. 중복 정의
    for did, srcs in sorted(defined.items()):
        if len(srcs) > 1:
            errors.append(f"{did} 중복 정의 ({len(srcs)}회)")

    # 3. 고아
    for did in sorted(defined):
        prefix = did.split("-")[0]
        if prefix in ORPHAN_EXEMPT:
            continue
        if did not in referenced and did.split(".")[0] not in referenced:
            warnings.append(f"{did} — 정의만 되고 아무 데서도 참조되지 않음")

    # 4. RISK 12개 전부 등장
    if "validation.csv" in files:
        for r in sorted(FIXED):
            if r not in files["validation.csv"]:
                errors.append(f"{r} — validation.csv에 행이 없음")

    print(f"검사 대상: {root}")
    print(f"정의된 ID {len(defined)}개 / 참조 {len(referenced)}개\n")

    if errors:
        print(f"[실패] 오류 {len(errors)}건")
        for e in errors:
            print(f"  - {e}")
    if warnings:
        print(f"\n[경고] {len(warnings)}건")
        for w in warnings:
            print(f"  - {w}")

    if not errors:
        print("[통과] 깨진 참조 없음")
        if warnings:
            print("경고는 의도된 것인지 확인하세요. 불필요한 화면·정책일 수 있습니다.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
