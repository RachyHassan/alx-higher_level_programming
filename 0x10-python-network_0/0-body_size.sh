#!/bin/bash
# A bash script that takes in a URL, and sends a request..
curl -sI "$1" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r')
