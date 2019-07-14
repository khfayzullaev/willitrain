#!/usr/bin/env bash
git stash -q --keep-index

./run_tests.sh
rc=$?

git stash pop -q
if [[ $rc != 0 ]]
then
 exit 1
fi

exit 0
