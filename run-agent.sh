#!/usr/bin/env bash
# Part 2 — run the AI agent (browser-use + Mistral).
# Works from any directory: uses absolute paths and the project's venv.
set -e

PROJECT="/Users/olesiamykhailyshyn/Documents/KSE/SE660 Software Quality Assurance and Testing/Labs/qa-lab3"
AGENTS="$PROJECT/agents"

cd "$AGENTS"
source .venv/bin/activate
python end_to_end_runner-olesia.py
