#!/usr/bin/env bash

./run_format_check.sh
rc=$?
if [[ $rc != 0 ]]
then
     exit 1
fi

./run_tests.sh
rc=$?
if [[ $rc != 0 ]]
then
    exit 1
fi

exit 0
