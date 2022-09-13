#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as s:
        import sys
        print("Exception: {}".format(s), file=sys.stderr)
        return None
