#!/usr/bin/env bash
# Part 1 — run the Playwright E2E tests and open the HTML report.
# Works from any directory: uses absolute paths.
set -e

PROJECT="/Users/olesiamykhailyshyn/Documents/KSE/SE660 Software Quality Assurance and Testing/Labs/qa-lab3"
TESTS="$PROJECT/saucedemo-tests-olesia"

cd "$TESTS"
npx playwright test
npx playwright show-report
