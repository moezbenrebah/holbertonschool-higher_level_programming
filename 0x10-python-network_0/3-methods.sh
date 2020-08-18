#!/bin/bash
# Bash script to display all HTTP methods the server will accpet.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
