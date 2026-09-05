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
    6. onboarding.yaml — 모든 ROLE에 온보딩 경로(ONB)가 있는가,
       entry_state·first_value.screen·completion.criteria가 채워졌는가,
       required: true 단계에 required_reason이, required: false 단계에 skip_to가 있는가
    7. 모든 ONB가 validation.csv에 covered로 있는가 (partial·gap이면 실패)

표준 라이브러리만 사용한다.
"""

import csv
import re
import sys
from pathlib import Path

VALID_STATUS = {"covered", "partial", "gap", "not-applicable"}
FIXED_RISKS = [f"RISK-{i:02d}" for i in range(1, 13)]
VALID_ENTRY_STATE = {"empty", "shared", "invited"}
EMPTY_VALUES = {"", "null", "~", '""', "''"}


def yaml_value(block: str, key: str) -> str:
    """블록 안에서 `key:` 의 첫 값을 꺼낸다. 비었거나 null 이면 빈 문자열."""
    m = re.search(rf"^\s*{re.escape(key)}:\s*(.*?)\s*$", block, re.M)
    if not m:
        return ""
    v = m.group(1).split("#", 1)[0].strip().strip('"').strip("'").strip()
    return "" if v in EMPTY_VALUES else v


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
    onboarding = read(root, "onboarding.yaml")

    csv_path = root / "validation.csv"
    if not csv_path.exists():
        print("[실패] validation.csv 없음. STEP 6을 수행하세요.")
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
    screens_with_empty = set()
    if ia:
        for block in re.split(r"\n\s*-\s+id:\s*SCR-", ia)[1:]:
            sid = "SCR-" + block.split("\n")[0].strip()
            name_m = re.search(r"name:\s*(.+)", block)
            name = name_m.group(1).strip().strip('"') if name_m else ""
            if re.search(r"type:\s*empty\b", block):
                screens_with_empty.add(sid)
            looks_like_list = any(k in name for k in ("목록", "리스트", "조망", "관리", "내역"))
            if looks_like_list and sid not in screens_with_empty:
                warnings.append(f"{sid} {name} — 목록 성격인데 빈 상태(empty) 정의 없음 (RISK-07)")

    # 6. 온보딩 경로
    onb_ids = []
    if not onboarding:
        errors.append("onboarding.yaml 없음 → STEP 4(온보딩)를 수행하세요")
    else:
        roles_with_onb = set()
        blocks = re.split(r"\n\s*-\s+id:\s*(ONB-\d{2,3})\s*$", "\n" + onboarding, flags=re.M)
        for i in range(1, len(blocks), 2):
            oid, body = blocks[i], blocks[i + 1]
            onb_ids.append(oid)

            role_m = re.search(r"^\s*role:\s*(ROLE-\d{2,3})", body, re.M)
            if role_m:
                roles_with_onb.add(role_m.group(1))
            else:
                errors.append(f"{oid} — role이 없음")

            entry_state = yaml_value(body, "entry_state")
            if entry_state not in VALID_ENTRY_STATE:
                errors.append(f"{oid} — entry_state는 empty / shared / invited 중 하나여야 함 (현재 '{entry_state}')")

            if not re.search(r"first_value:\s*\n\s*screen:\s*SCR-\d{2,3}(?:\.\d+)?", body):
                errors.append(f"{oid} — first_value.screen이 없음 (첫 가치가 일어나는 화면을 먼저 정한다)")

            steps_m = re.search(r"^\s*steps:\s*\n(.*?)(?=^\s*completion:|\Z)", body, re.M | re.S)
            steps_text = steps_m.group(1) if steps_m else ""
            step_blocks = re.split(r"\n\s*-\s+screen:", "\n" + steps_text)[1:]
            if not step_blocks:
                errors.append(f"{oid} — steps가 비어 있음 (각 단계는 screen 키로 시작해야 함)")
            for n, sb in enumerate(step_blocks, 1):
                req = yaml_value(sb, "required").lower()
                if req not in {"true", "false"}:
                    errors.append(f"{oid} 단계 {n} — required가 true/false로 지정되지 않음")
                    continue
                if req == "true" and not yaml_value(sb, "required_reason"):
                    errors.append(
                        f"{oid} 단계 {n} — required: true인데 required_reason이 비어 있음 "
                        f"(없으면 첫 가치 화면이 동작하지 않는가? 아니면 required: false)"
                    )
                if req == "false" and not yaml_value(sb, "skip_to"):
                    errors.append(f"{oid} 단계 {n} — required: false인데 skip_to가 비어 있음")
                resolves = yaml_value(sb, "resolves_empty_state")
                if resolves and screens_with_empty and resolves not in screens_with_empty:
                    warnings.append(
                        f"{oid} 단계 {n} — {resolves}의 빈 상태를 해소한다고 했으나 ia.yaml에 그 화면의 empty 상태가 없음"
                    )

            if not yaml_value(body, "criteria"):
                errors.append(f"{oid} — completion.criteria가 비어 있음 (데이터로 판정 가능한 완료 조건)")

        if not onb_ids:
            errors.append("onboarding.yaml에 ONB 경로가 하나도 없음 → STEP 4")
        for r in sorted(roles - roles_with_onb):
            errors.append(f"{r} — 이 역할의 온보딩 경로(ONB)가 없음 → STEP 4")

    # 7. 온보딩 커버리지 (validation.csv)
    for oid in onb_ids:
        row = by_id.get(oid)
        if row is None:
            errors.append(f"{oid} — onboarding.yaml에 있으나 validation.csv에 행이 없음")
            continue
        status = (row.get("status") or "").strip().lower()
        if status not in VALID_STATUS:
            errors.append(f"{oid} — status 값이 비었거나 잘못됨: '{status}'")
        elif status in {"partial", "gap"}:
            errors.append(f"{oid} — {status}. 온보딩 경로가 이어지는 화면·플로우가 없음 → STEP 2/3/4로 되돌아가세요")
        elif status == "covered":
            if not (row.get("covered_by_screen") or "").strip():
                errors.append(f"{oid} — covered인데 covered_by_screen이 비어 있음")
            if not (row.get("covered_by_flow") or "").strip():
                errors.append(f"{oid} — covered인데 covered_by_flow가 비어 있음 (첫 가치 뒤에 이어지는 FLW)")

    print(f"검사 대상: {root}")
    print(f"요구사항 {len(req_in_csv)}건 / 역할 {len(roles)}개 / 온보딩 경로 {len(onb_ids)}개\n")

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
