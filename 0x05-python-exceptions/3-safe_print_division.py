#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the result of simple division problem"""
    try:
        results = a / b
    except (TypeError, ZeroDivisionError):
        results = None
    finally:
        print("Inside result:{}".format(results))
    return (results)
