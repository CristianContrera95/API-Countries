#!/bin/bash

source ./scripts/helpers.sh

# Check if virtualenv is installed
virtualenv --version > /dev/null 2>&1
if [[ $? -ne 0 ]]
then
    printf "\nPlease install virtualenv:\n[ https://virtualenv.pypa.io/en/latest/installation.html ]\n";
fi

if [[ ! -d "venv" ]]; then
    virtualenv -p python3 venv
fi

active_env

# # Check if pip is installed
# pip --version > /dev/null 2>&1
# if [[ $? -ne 0 ]]
# then
#     printf "\nPlease install pip:\n[ https://pip.pypa.io/en/stable/installing/# ]\n";
#     exit 0;
# fi

# Check if requirements exists
if [[ ! -f "requirements.txt" ]]; then
    echo "requirements.txt file does not exist.";
    exit 1;
fi
pip install -r requirements.txt

if [[ "$1" == "dev" ]]; then
    if [[ ! -f "requirements-dev.txt" ]]; then
        echo "requirements-dev.txt file does not exist.";
        exit 1;
    fi
    pip install -r requirements-dev.txt
fi
