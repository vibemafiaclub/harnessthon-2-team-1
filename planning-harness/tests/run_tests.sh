#!/usr/bin/env bash
# 검증 스크립트가 정상 동작하는지 확인한다.
# fixture-fail 은 반드시 실패해야 하고, fixture-pass 는 반드시 통과해야 한다.
set -u
cd "$(dirname "$0")/.."
fail=0

echo "── fixture-fail (실패해야 정상) ─────────────"
python3 scripts/validate_ids.py   tests/fixture-fail > /dev/null 2>&1 && { echo "  X validate_ids 가 오류를 못 잡음"; fail=1; } || echo "  O validate_ids 오류 검출"
python3 scripts/check_coverage.py tests/fixture-fail > /dev/null 2>&1 && { echo "  X check_coverage 가 오류를 못 잡음"; fail=1; } || echo "  O check_coverage 오류 검출"

echo "── fixture-pass (통과해야 정상) ─────────────"
python3 scripts/validate_ids.py   tests/fixture-pass > /dev/null 2>&1 && echo "  O validate_ids 통과" || { echo "  X validate_ids 오탐"; fail=1; }
python3 scripts/check_coverage.py tests/fixture-pass > /dev/null 2>&1 && echo "  O check_coverage 통과" || { echo "  X check_coverage 오탐"; fail=1; }

echo
[ $fail -eq 0 ] && echo "전체 통과" || echo "실패 있음"
exit $fail
