#!/usr/bin/env python3
"""요구사항·리스크 커버리지 검사.

사용법:
    python scripts/check_coverage.py {산출물디렉토리}

검사 항목
    1. definition.md의 모든 REQ가 validation.csv에 있는가
    2. 모든 REQ의 status가 covered인가 (partial·gap이면 실패)
    3. RISK-01~12가 전부 판정되었는가 (빈칸이면 실패)
    4. 모든 ROLE에 최소 하나의 FLW가 있는가
    5. 목록 성격 화면에 빈 상태(empty)가 정의되었는가

표준 라이브러리만 사용한다.
"""

import csv
import re
import sys
from pathlib import Path

VALID_STATUS = {"covered", "partial", "gap", "not-applicable"}
FIXED_RISKS = [f"RISK-{i:02d}" for i in range(1, 13)]


def read(root: Path, name: str) -> str:
    p = root / name
    return p.read_text(encoding="utf-8") if p.exists() else ""


def main():
    if len(sys.argv) < 2:
        print("사용법: python scripts/check_coverage.py {산출물디렉토리}")
        return 2

    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"[오류] 디렉토리를 찾을 수 없습니다: {root}")
        return 2

    errors, warnings = [], []

    definition = read(root, "definition.md")
    users = read(root, "users.md")
    flows = read(root, "flows.yaml")
    ia = read(root, "ia.yaml")

    csv_path = root / "validation.csv"
    if not csv_path.exists():
        print("[실패] validation.csv 없음. STEP 5를 수행하세요.")
        return 1

    with csv_path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        print("[실패] validation.csv가 비어 있습니다.")
        return 1

    by_id = {(r.get("id") or "").strip(): r for r in rows}

    # 1~2. 요구사항 커버리지
    req_in_def = set(re.findall(r"\bREQ-\d{2,3}\b", definition))
    req_in_csv = {i for i in by_id if i.startswith("REQ-")}

    for missing in sorted(req_in_def - req_in_csv):
        errors.append(f"{missing} — definition.md에 있으나 validation.csv에 행이 없음")
    for extra in sorted(req_in_csv - req_in_def):
        warnings.append(f"{extra} — validation.csv에만 있고 definition.md에 없음")

    for rid in sorted(req_in_csv):
        row = by_id[rid]
        status = (row.get("status") or "").strip().lower()
        if status not in VALID_STATUS:
            errors.append(f"{rid} — status 값이 비었거나 잘못됨: '{status}'")
        elif status in {"partial", "gap"}:
            errors.append(
                f"{rid} — {status}. "
                f"{'화면 또는 플로우 누락' if status == 'partial' else '어느 화면에서도 다루지 않음'} "
                f"→ STEP 2/3으로 되돌아가세요"
            )
        elif status == "covered":
            if not (row.get("covered_by_screen") or "").strip():
                errors.append(f"{rid} — covered인데 covered_by_screen이 비어 있음")
            if not (row.get("covered_by_flow") or "").strip():
                errors.append(f"{rid} — covered인데 covered_by_flow가 비어 있음")

    # 3. 리스크 12패턴 판정
    for risk in FIXED_RISKS:
        row = by_id.get(risk)
        if row is None:
            errors.append(f"{risk} — validation.csv에 행이 없음 (12패턴 전부 판정 필요)")
            continue
        status = (row.get("status") or "").strip().lower()
        if status not in VALID_STATUS:
            errors.append(f"{risk} — 판정되지 않음. 해당되면 covered, 아니면 not-applicable")
        elif status == "covered" and not (row.get("covered_by_screen") or "").strip():
            errors.append(f"{risk} — covered인데 대응 화면이 비어 있음")

    # 4. 역할별 플로우
    roles = set(re.findall(r"\bROLE-\d{2,3}\b", users))
    roles_with_flow = set(re.findall(r"role:\s*(ROLE-\d{2,3})", flows))
    for r in sorted(roles - roles_with_flow):
        errors.append(f"{r} — 이 역할의 플로우(FLW)가 없음 → STEP 3")

    # 5. 목록 화면 빈 상태
    if ia:
        for block in re.split(r"\n\s*-\s+id:\s*SCR-", ia)[1:]:
            sid = "SCR-" + block.split("\n")[0].strip()
            name_m = re.search(r"name:\s*(.+)", block)
            name = name_m.group(1).strip().strip('"') if name_m else ""
            looks_like_list = any(k in name for k in ("목록", "리스트", "조망", "관리", "내역"))
            if looks_like_list and "empty" not in block:
                warnings.append(f"{sid} {name} — 목록 성격인데 빈 상태(empty) 정의 없음 (RISK-07)")

    print(f"검사 대상: {root}")
    print(f"요구사항 {len(req_in_csv)}건 / 역할 {len(roles)}개\n")

    if errors:
        print(f"[실패] 오류 {len(errors)}건")
        for e in errors:
            print(f"  - {e}")
    if warnings:
        print(f"\n[경고] {len(warnings)}건")
        for w in warnings:
            print(f"  - {w}")
    if not errors:
        print("[통과] 커버리지 이상 없음")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
