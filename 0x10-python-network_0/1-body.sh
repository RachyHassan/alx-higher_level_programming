#!/bin/bash
# A script that takes in a URL, sends a GET request and displays the body.
curl -s -w "%{http_code}" "$1" | awk '/^200/{getline; print}'
