#!/bin/bash
# A script that sends a delete request to the URL passed as the first argument.
curl -X DELETE -s "$1"
