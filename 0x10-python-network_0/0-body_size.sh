#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | head -n -3 | tail -n +3 | cut '-d ' '-f2'
