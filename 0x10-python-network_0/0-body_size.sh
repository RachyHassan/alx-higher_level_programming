#!/bin/bash
# A bash script that takes in a URL, sends a request to the
# URL, and displays the size of the body of the response.

if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

url=$1
size=$(curl -sI "$url" | grep -i 'content-length' | awk '{print $2}' | tr -d '\r')

if [ -z "$size" ]; then
	echo "Can't determine the size of the response body for $url."
else
	echo "Size of the response body for $url: ${size} bytes"
fi
