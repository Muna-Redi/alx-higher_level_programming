#!/bin/bash
# sends JSON POST request to a given URL passed as the first argument
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
