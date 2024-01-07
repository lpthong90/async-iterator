#!/usr/bin/env bash

set -e
set -x

mypy async_iterator
ruff async_iterator tests scripts
ruff format async_iterator tests scripts --check