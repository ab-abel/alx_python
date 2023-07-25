#!/usr/bin/python3
# raise an exception with a message


def raise_exception_msg(msg):
    try:
        raise NameError(msg)
    except NameError as ne:
        print(ne)
