#!/usr/bin/env bash

set -o nounset
set -o errexit
set -o xtrace

if [ -d "./.venv" ]; then
    ./.venv/bin/pytest .
fi

if [ "${CI+x}" = "x" ] && [ "$CI" == "circleci" ]; then
    poetry run pytest .
fi
