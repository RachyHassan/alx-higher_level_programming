#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        func = fct(*args)
        return func
    except Exception as exc:
        print("Exception: {}".format(exc), file=sys.stderr)
        return None
