#!/bin/bash
# Get The body  size
curl -sI "$1" | grep 'Content-Length:' | cut -c 17-
