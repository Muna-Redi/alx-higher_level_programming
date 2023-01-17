#!/usr/bin/env bash
# Getting the body size of a request
curl -Is "$1" | grep Content-Length | cut -f2 -d' '
