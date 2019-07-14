#!/usr/bin/env bash
if [ -d "./.venv" ]; then
    ./.venv/bin/isort --check-only
    rc=$?
    if [[ $rc != 0 ]]; then echo "Fix import sorting!" && exit 1; fi
    echo $?

    ./.venv/bin/black --check .
    rc=$?
    if [[ $rc != 0 ]]; then echo "Code needs to be reformatted!" && exit 1; fi

    ./.venv/bin/pytest .
else
    echo "Virtual environment does not exist"
fi
