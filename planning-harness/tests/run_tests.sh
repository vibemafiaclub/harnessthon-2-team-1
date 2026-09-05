#!/usr/bin/env bash
# 검증 스크립트가 정상 동작하는지 확인한다.
# fixture-fail 은 반드시 실패해야 하고, fixture-pass 는 반드시 통과해야 한다.
# fixture-fail-onboarding 은 참조는 정상이지만 온보딩 규칙만 깨져 있어, check_coverage 가 온보딩 오류를 잡아야 한다.
# fixture-wf-pass / fixture-wf-fail 은 STEP 8 와이어프레임 입력 패키지 검사기(check_wireframe_input) 용이다.
set -u
cd "$(dirname "$0")/.."
fail=0

echo "── fixture-fail (실패해야 정상) ─────────────"
python3 scripts/validate_ids.py   tests/fixture-fail > /dev/null 2>&1 && { echo "  X validate_ids 가 오류를 못 잡음"; fail=1; } || echo "  O validate_ids 오류 검출"
python3 scripts/check_coverage.py tests/fixture-fail > /dev/null 2>&1 && { echo "  X check_coverage 가 오류를 못 잡음"; fail=1; } || echo "  O check_coverage 오류 검출"

echo "── fixture-pass (통과해야 정상) ─────────────"
python3 scripts/validate_ids.py   tests/fixture-pass > /dev/null 2>&1 && echo "  O validate_ids 통과" || { echo "  X validate_ids 오탐"; fail=1; }
python3 scripts/check_coverage.py tests/fixture-pass > /dev/null 2>&1 && echo "  O check_coverage 통과" || { echo "  X check_coverage 오탐"; fail=1; }

echo "── fixture-fail-onboarding (온보딩 검사만 실패해야 정상) ──"
python3 scripts/validate_ids.py   tests/fixture-fail-onboarding > /dev/null 2>&1 && echo "  O validate_ids 통과 (참조는 정상)" || { echo "  X validate_ids 오탐"; fail=1; }
out=$(python3 scripts/check_coverage.py tests/fixture-fail-onboarding 2>&1); rc=$?
if [ $rc -ne 0 ] && echo "$out" | grep -q "ROLE-02 — 이 역할의 온보딩 경로" \
                  && echo "$out" | grep -q "required_reason이 비어 있음" \
                  && echo "$out" | grep -q "ONB-01 — partial"; then
  echo "  O check_coverage 온보딩 오류 3종 검출 (역할 누락 / 필수 근거 없음 / partial)"
else
  echo "  X check_coverage 가 온보딩 오류를 못 잡음"; echo "$out" | sed 's/^/      /'; fail=1
fi

echo "── STEP 8 패키지: fixture-wf-pass (통과해야 정상) ──"
python3 scripts/check_wireframe_input.py tests/fixture-wf-pass/planning tests/fixture-wf-pass/package > /dev/null 2>&1 \
  && echo "  O check_wireframe_input 통과" || { echo "  X check_wireframe_input 오탐"; fail=1; }

echo "── STEP 8 패키지: fixture-wf-fail (실패해야 정상) ──"
out=$(python3 scripts/check_wireframe_input.py tests/fixture-wf-fail/planning tests/fixture-wf-fail/package 2>&1); rc=$?
if [ $rc -ne 0 ] && echo "$out" | grep -q "절 '## 5. 온보딩 경로' 이 없음" \
                  && echo "$out" | grep -q "SCR-99 — 패키지에만 있는 ID" \
                  && echo "$out" | grep -q "ONB-01 — 상위기획에 있는데 패키지에 없음" \
                  && echo "$out" | grep -q "RISK-12 — constraints.md" \
                  && echo "$out" | grep -q "채우지 않은 자리표시자"; then
  echo "  O check_wireframe_input 오류 5종 검출 (절 삭제 / 신규 ID / 누락 ID / RISK 행 / 자리표시자)"
else
  echo "  X check_wireframe_input 이 패키지 오류를 못 잡음"; echo "$out" | sed 's/^/      /'; fail=1
fi

echo
[ $fail -eq 0 ] && echo "전체 통과" || echo "실패 있음"
exit $fail
