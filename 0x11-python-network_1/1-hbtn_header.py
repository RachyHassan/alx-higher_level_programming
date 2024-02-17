#!/usr/bin/python3
"""
A script that takes in a URL, sends a request and displays response value
"""
import urllib.request
import sys

# fetch the url from command line
url = sys.argv[1]
# send a request to url and retrieve a response
with urllib.request.urlopen(url) as response:
    # extract the value of X-Request-Id
    x_request_id = response.getheader('X-Request-Id')
# print variable
print(x_request_id)
