#!/usr/bin/env bash
DIR=$(dirname "$0")
pytest $DIR/../src/Tests/test_abc.py --alluredir=$DIR/../results && $DIR/generate_reports.sh