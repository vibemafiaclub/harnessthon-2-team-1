#!/usr/bin/env python3
"""STEP 8 와이어프레임 입력 패키지 검사.

사용법:
    python scripts/check_wireframe_input.py {상위기획디렉토리} [{패키지디렉토리}]
    예) python scripts/check_wireframe_input.py wedding-scheduler/01-planning wireframes/input

패키지디렉토리를 생략하면 wireframes/input 을 본다.

검사 항목
    1. 파일 5종이 모두 있는가
    2. 템플릿의 절 제목이 모두 살아 있는가
    3. 상위기획의 REQ·ROLE·SCR·ONB가 패키지에서 누락되지 않았는가
    4. 상위기획에 없는 ID를 패키지가 새로 만들지 않았는가
    5. RISK-01~12가 constraints.md에 전부 있고, 미완성 자리표시자가 남지 않았는가

표준 라이브러리만 사용한다.
"""

import re
import sys
from pathlib import Path

DEFAULT_PACKAGE_DIR = "wireframes/input"

# 패키지 파일 -> 반드시 남아 있어야 하는 절 제목 (앞부분 일치)
REQUIRED_SECTIONS = {
    "prd.md": [
        "## 1. 배경",
        "## 2. 목표",
        "## 3. 핵심 유저 스토리",
        "## 4. 사용자 상황",
        "## 5. 사용자 역할",
        "## 6. 스코프",
        "## 7. 기능 요구사항",
        "## 8. 비기능 요구사항",
        "## 9. 성공 기준",
    ],
    "user-flow.md": [
        "## 1. 핵심 경로",
        "## 2.",
        "## 3. 유저 플로우",
        "## 4. 역할별 플로우 매핑",
        "## 5. 온보딩 경로",
    ],
    "ia.md": [
        "## 1. 엔티티",
        "## 2. 화면 목록",
        "## 3. 화면별 핵심 정보",
        "## 4. 내비게이션 구조",
        "## 5. 화면-요구사항 커버리지",
    ],
    "constraints.md": [
        "## 1. 제약사항",
        "## 2. 권한 정책",
        "## 3. 상태·예외 정책",
        "## 4. 데이터 정책",
        "## 5. 알림 정책",
        "## 6. 리스크 패턴",
        "## 7. 화면별 설계 주의점",
        "## 8. 더미 콘텐츠 소스",
        "## 9. 가정 로그 초안",
    ],
    "README.md": [
        "## 스킬 입력 항목 매핑",
        "## 실행 방법",
        "## 화면 범위에 대한 참고",
        "## 미결 사항",
    ],
}

PACKAGE_FILES = list(REQUIRED_SECTIONS)

# 상위기획 산출물에서 ID를 읽어오는 파일
SOURCE_OF = {
    "REQ": "definition.md",
    "ROLE": "users.md",
    "SCR": "ia.yaml",
    "ONB": "onboarding.yaml",
}

ID_RE = re.compile(r"\b(REQ|ROLE|ENT|SCR|FLW|ST|ONB|POL|RISK)-(\d{2,3})(?:\.(\d+))?\b")
FIXED_RISKS = [f"RISK-{i:02d}" for i in range(1, 13)]

# 채우지 않은 흔적
PLACEHOLDER_RE = re.compile(r"\{프로젝트명\}|\{YYYY-MM-DD\}|\{역할군\}|\{화면명\}|\{플로우명\}"
                            r"|SCR-NN|REQ-NN|ROLE-NN|ENT-NN|POL-NN|FLW-NN|RISK-NN|ONB-NN")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)

# 패키지가 상위기획보다 좁아도 되는 접두사
#   ENT·FLW·ST·POL 은 화면 설계에 불필요한 것을 덜어낼 수 있다.
#   REQ·ROLE·SCR·ONB 은 하나라도 빠지면 다음 하네스가 그 부분을 상상해서 채운다.
MUST_CARRY = ["REQ", "ROLE", "SCR", "ONB"]


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (FileNotFoundError, IsADirectoryError):
        return ""


def ids_in(text: str, prefix: str) -> set:
    return {m.group(0) for m in ID_RE.finditer(text) if m.group(1) == prefix}


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2

    planning = Path(sys.argv[1])
    package = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(DEFAULT_PACKAGE_DIR)

    if not planning.is_dir():
        print(f"[실패] 상위기획 디렉토리가 없음: {planning}")
        return 1

    errors, warnings = [], []

    # 1. 파일 존재
    contents = {}
    for name in PACKAGE_FILES:
        text = read(package / name)
        if not text.strip():
            errors.append(f"{name} — 없거나 비어 있음 ({package / name})")
        contents[name] = text

    if errors:
        print(f"검사 대상: {package}")
        print(f"[실패] 오류 {len(errors)}건")
        for e in errors:
            print(f"  - {e}")
        print("\ntemplates/wireframe-input/ 을 복사해 채우세요.")
        return 1

    # 2. 절 제목
    for name, sections in REQUIRED_SECTIONS.items():
        for sec in sections:
            if sec not in contents[name]:
                errors.append(f"{name} — 절 '{sec}' 이 없음 (템플릿의 절을 지우지 않는다)")

    # 3·4. ID 누락과 신규 생성
    joined = "\n".join(contents.values())
    for prefix in MUST_CARRY:
        src = read(planning / SOURCE_OF[prefix])
        if not src.strip():
            warnings.append(f"{SOURCE_OF[prefix]} 없음 — {prefix} 대조를 건너뜀")
            continue
        planned = ids_in(src, prefix)
        packaged = ids_in(joined, prefix)
        for missing in sorted(planned - packaged):
            errors.append(f"{missing} — 상위기획에 있는데 패키지에 없음 ({SOURCE_OF[prefix]})")
        for invented in sorted(packaged - planned):
            errors.append(f"{invented} — 패키지에만 있는 ID. STEP 8은 새 ID를 만들지 않는다")

    # 5. RISK 12개 + 자리표시자
    for r in FIXED_RISKS:
        if r not in contents["constraints.md"]:
            errors.append(f"{r} — constraints.md 6절에 행이 없음 (해당 없으면 근거를 적고 행은 남긴다)")

    for name, text in contents.items():
        stripped = COMMENT_RE.sub("", text)
        left = sorted(set(PLACEHOLDER_RE.findall(stripped)))
        if left:
            errors.append(f"{name} — 채우지 않은 자리표시자: {', '.join(left)}")
        if COMMENT_RE.search(text):
            warnings.append(f"{name} — 템플릿 주석(<!-- -->)이 남아 있음. 채운 뒤 지운다")

    print(f"검사 대상: {package}  (기준: {planning})")
    print(f"패키지 파일 {len(PACKAGE_FILES)}종 / 대조한 ID 접두사 {', '.join(MUST_CARRY)}\n")

    if errors:
        print(f"[실패] 오류 {len(errors)}건")
        for e in errors:
            print(f"  - {e}")
    if warnings:
        print(f"\n[경고] {len(warnings)}건")
        for w in warnings:
            print(f"  - {w}")

    if not errors:
        print("[통과] 패키지가 상위기획을 빠짐없이 옮겼음")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
