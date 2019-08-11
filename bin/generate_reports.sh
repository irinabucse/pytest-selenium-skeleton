#!/usr/bin/env bash
DIR=$(dirname "$0")
allure generate $DIR/../results --clean
