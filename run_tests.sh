#!/usr/bin/env bash
if [ -d "./.venv" ]; then
    ./.venv/bin/pytest .
else
    echo "Virtual environment does not exist"
fi
