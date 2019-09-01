#!/usr/bin/env bash

set -o nounset
set -o errexit
set -o pipefail

if [ -d "./.venv" ]; then
    echo "running isort check"
    ./.venv/bin/isort --virtual-env .venv --check --diff
    ic=$?

    echo "running black check"
    ./.venv/bin/black --check --diff .
    bc=$?

    echo "running mypy check"
    ./.venv/bin/mypy .
    mc=$?

    if [[ $ic != 0 || $bc != 0 || $mc != 0 ]]
    then
        echo "one (or more) of the checks falied"
        exit 1
    fi
fi

if [ "${CI+x}" = "x" ] && [ "$CI" == "circleci" ]; then
    echo "running isort check"
    poetry run isort --check --diff
    ic=$?

    echo "running black check"
    poetry run black --check --diff .
    bc=$?

    echo "running mypy check"
    poetry run mypy .
    mc=$?

    if [[ $ic != 0 || $bc != 0 || $mc != 0 ]]
    then
        echo "one (or more) of the checks falied"
        exit 1
    fi
fi
