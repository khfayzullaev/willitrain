#!/usr/bin/env bash
if [ -d "./.venv" ]; then
    ./.venv/bin/isort --virtual-env .venv --apply
    ./.venv/bin/black .
    git add -u # stage the modified files
fi
