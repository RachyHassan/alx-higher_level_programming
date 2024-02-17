#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a Post request
and displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys


def post_request(url, email):
    """
    A function to encode email parameter.
    parameters:
        url (str): The URLto send the POST request
        email (str): email included in the parameter.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')

    print(body)
