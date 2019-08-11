#!/usr/bin/env bash
DIR=$(dirname "$0")
rm -rf $DIR/../results/*.json  && rm -rf $DIR/../results/*.txt && $DIR/run_tests.sh
