#!/usr/bin/env bash
if [ -d "./.venv" ]; then
    ./.venv/bin/isort --virtual-env .venv --check
    rc=$?
    if [[ $rc != 0 ]]
    then
         exit 1
    fi

    ./.venv/bin/black --check .
    rc=$?
    if [[ $rc != 0 ]]
    then
         exit 1
    fi
fi
