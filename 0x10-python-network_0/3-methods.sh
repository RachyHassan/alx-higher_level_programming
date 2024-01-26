#!/bin/bash
# A script that takes in a URL and displays all HTTP methods the server will accept
curl -s -X OPTIONS -I "$1" | awk -F ": " '/Allow/{print $2}'
