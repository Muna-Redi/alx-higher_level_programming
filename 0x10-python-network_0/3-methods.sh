#!/bin/bash
# Displays all HTTP methods the server accepts
curl -Is "$1" | grep Allow | cut -c 8-
