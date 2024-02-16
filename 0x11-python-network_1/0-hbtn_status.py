#!/usr/bin/python3
# A python script to fetch the status
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    utf8_body = body.decode('utf-8')
# display the file
print('Body response:')
print('\t- type:', type(body))
print('\t- content:', body)
print('\t- utf8 content:', utf8_body)
