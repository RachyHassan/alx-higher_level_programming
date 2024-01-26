#!/bin/bash
# A script that takes in a URL, sends a GET request and displays the body.
curl -s -w "%{http_code}" -L "$1" | head -c 7 | awk '{getline; print}'
