#!/bin/bash

source ./scripts/helpers.sh

active_env

coverage run -m pytest -v
coverage report --include=src/**
