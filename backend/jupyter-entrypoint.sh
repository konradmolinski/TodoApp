#!/usr/bin/env bash
set -e

## Running passed command
if [[ "$1" ]]; then
	eval "$@"
else
	jupyter notebook --port 8500 --host 0.0.0.0
fi
