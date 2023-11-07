#!/usr/bin/python3
""" A function that creates an object from a JSON file. """
import json


def load_from_json_file(filename):
    with open(filename) as f:
        return (json.load(f))
