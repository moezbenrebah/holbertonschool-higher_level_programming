#!/bin/bash
# sends a JSON request POST and display the body of the response.
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
