#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        retu_rn = fct(*args)
    except Exception as err:
        retu_rn = None
        print("Exception: {}".format(err), file=sys.stderr)
    finally:
        return
