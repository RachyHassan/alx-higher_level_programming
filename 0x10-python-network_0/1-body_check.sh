#!/bin/bash
#just checking
curl -s -w "%{http_code}" -L "$1" | tail -c 4
