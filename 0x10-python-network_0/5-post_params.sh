#!/bin/bash
# Bash script to display the body of the response
curl -sd "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
