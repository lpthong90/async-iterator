#!/bin/sh -e
set -x

ruff async_iterator tests scripts --fix
ruff format async_iterator tests scripts