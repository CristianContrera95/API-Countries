#!/bin/bash

source ./scripts/helpers.sh

if [[ "$1" == "docker" ]]; then
    docker run -it -p 8000:80 aivo-api:latest;
else
    active_env
    python src/main.py
fi
